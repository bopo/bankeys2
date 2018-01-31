var mRefreshPluginTimer = -1;
// 日志记录类型，在日志信息栏内显示不同的颜色
var LOG_TYPE_NORMAL = 0;
var LOG_TYPE_API = 1;
var LOG_TYPE_EVENT = 2;
var LOG_TYPE_ERROR = 3;
var currentAgentID = -1;  //当前座席ID
// var offerUser = {username:"admin"}
// var ServerAddr = '10.7.7.100'
// var ServerPort = '8906'
var AUDIT_SWITCH = null;
var AUDIT_SWITCH1 = null;
var AUDIT_SWITCH2 = null;
var queuesUserCounts = null;//排队人数
//座席与用户当前所处的状态
var mCurrentStatus = 0; 
var servantName=-1;//坐席名称 
var	mSelfUserId = -1;
var	roomId = -1;
var	dwPriority = 4;
var dwAgentFlags=-1;//身份标识(用户，坐席)
var mRefreshVolumeTimer = -1;// 实时音量大小定时器
var USER_TYPE_CLIENT = 1;
var USER_TYPE_AGNET = 2;
var userType = USER_TYPE_AGNET;


var currentScope = null;
var startServiceTag=false;//开始服务点击按钮事件
var CLIENT_STATUS_AREA = 1;
var CLIENT_STATUS_QUEUE = 2;
var CLIENT_STATUS_QUEUEING = 3;
var CLIENT_STATUS_CHATTING = 4;

var AGENT_STATUS_AREA = 1;
var AGENT_STATUS_SERVICE = 2;

//服务区域(营业厅)ID数组
var areaIdArray = null;
var areaArrayIdx = 0;
var hallbuinessNum;

//初始化本地对象信息
function InitClientObjectInfo(mSelfUserId, dwAgentFlags, dwPriority) {
    AddLog("Initialize Client Object Information", LOG_TYPE_NORMAL);

    //初始化服务区域Id数组
    areaArrayIdx = 0;
    areaIdArray = new Array();

    var dwValue = 0;
    // 设置本地视频采集的宽度
    dwValue = 320;
    BRAC_SetSDKOption(BRAC_SO_LOCALVIDEO_WIDTHCTRL,dwValue);
    // 设置本地视频采集的高度
    dwValue = 240;
    BRAC_SetSDKOption(BRAC_SO_LOCALVIDEO_HEIGHTCTRL,dwValue);
    // 设置本地视频编码的码率
    dwValue = 60 * 1000;    // 60 kbps
    BRAC_SetSDKOption(BRAC_SO_LOCALVIDEO_BITRATECTRL,dwValue);
    // 设置本地视频编码的质量因子
    // dwValue = 4;
    // BRAC_SetSDKOption(BRAC_SO_LOCALVIDEO_QUALITYCTRL,dwValue);
    // 设置本地视频编码的关键帧间隔
    dwValue = 20;
    BRAC_SetSDKOption(BRAC_SO_LOCALVIDEO_GOPCTRL,dwValue);
    // 设置本地视频编码的帧率
    dwValue = 8;
    BRAC_SetSDKOption(BRAC_SO_LOCALVIDEO_FPSCTRL,dwValue);
    // 设置本地视频编码的预设参数
    dwValue = 3;
    BRAC_SetSDKOption(BRAC_SO_LOCALVIDEO_PRESETCTRL,dwValue);
    // 使参数设置生效
    var bUseAppParam = true;
    BRAC_SetSDKOption(BRAC_SO_LOCALVIDEO_APPLYPARAM,bUseAppParam);

	//业务对象身份初始化
	BRAC_SetSDKOption(BRAC_SO_OBJECT_INITFLAGS, dwAgentFlags);

    //视频录制配置
    BRAC_SetSDKOption(BRAC_SO_RECORD_FILETYPE, 0);    // 录制为MP4格式
    var dwFlags = ANYCHAT_RECORD_FLAGS_VIDEO + ANYCHAT_RECORD_FLAGS_AUDIO + ANYCHAT_RECORD_FLAGS_MIXVIDEO + ANYCHAT_RECORD_FLAGS_MIXAUDIO;
    BRAC_StreamRecordCtrlEx(mSelfUserId, 1,  dwFlags, 0, "Hello");


	//客户端用户对象优先级
	BRAC_ObjectSetValue(ANYCHAT_OBJECT_TYPE_CLIENTUSER, mSelfUserId, ANYCHAT_OBJECT_INFO_PRIORITY, dwPriority);
	var dwAttribute = -1;
	BRAC_ObjectSetValue(ANYCHAT_OBJECT_TYPE_CLIENTUSER, mSelfUserId, ANYCHAT_OBJECT_INFO_ATTRIBUTE, dwAttribute);
	//向服务器发送数据同步请求指令
	BRAC_ObjectControl(ANYCHAT_OBJECT_TYPE_AREA, ANYCHAT_INVALID_OBJECT_ID, ANYCHAT_OBJECT_CTRL_SYNCDATA, mSelfUserId, 0, 0, 0, "");

	AddLog("Initialize Client Object Information end", LOG_TYPE_NORMAL);
}
//设置cookie
function setCookie(c_name, value, expiredays) {
    var exdate = new Date();
    exdate.setDate(exdate.getDate() + expiredays);
    document.cookie = c_name + "=" + value + ((expiredays == null) ? "" : ";expires=" + exdate.toGMTString());
}
//设置登录信息，包括用户名、服务器IP、服务器端口、应用ID
function setLoginInfo() {
    setCookie('username', currentScope.offerUser.username, 30);
    setCookie('ServerAddr', currentScope.ServerAddr, 30);
    setCookie('ServerPort', currentScope.ServerAddr, 30);

    setCookie('askSelect', $("#askSelect").get(0).selectedIndex, 30);
    setCookie('PrioritySelect', $("#dwPrioritySelect").get(0).selectedIndex, 30);    
}
//获取当前时间  (00:00:00)
function GetTheTime() {
	var TheTime = new Date();
	return TheTime.toLocaleTimeString();
}
// 添加日志并显示，根据不同的类型显示不同的颜色
function AddLog(message, type) {
    if (type == LOG_TYPE_API) {			// API调用日志，绿色
        message = message.fontcolor("Green");
	} else if(type == LOG_TYPE_EVENT) {	// 回调事件日志，黄色
        message = message.fontcolor("#CC6600");
	} else if(type == LOG_TYPE_ERROR) {	// 出错日志，红色
        message = message.fontcolor("#FF0000");
	} else {							// 普通日志，灰色
        message = message.fontcolor("#333333");
	}
    console.log("message log "+message + "&nbsp" + GetTheTime().fontcolor("#333333"))
    //GetID("LOG_DIV_CONTENT").innerHTML += message + "&nbsp" + GetTheTime().fontcolor("#333333") + "<br />";
	//GetID("LOG_DIV_CONTENT").scrollTop = GetID("LOG_DIV_CONTENT").scrollHeight;
}
function GetID(id) {
	if (document.getElementById) {
		return document.getElementById(id);
	} else if (window[id]) {
		return window[id];
	}
	return null;
}
// onload默认运行
function LogicInit() {
	setTimeout(
			function() {
                // 判断是否支持插件和插件长度（插件检测）
                if (navigator.plugins && navigator.plugins.length) {
                    window.navigator.plugins.refresh(false);
                }
                // 检查是否安装了插件
                var NEED_ANYCHAT_APILEVEL = "0"; // 定义业务层需要的AnyChat
                // API Level
                var errorcode = BRAC_InitSDK(NEED_ANYCHAT_APILEVEL); // 初始化插件（返回成功(0)或插件版本号太低的编号）
                AddLog("BRAC_InitSDK(" + NEED_ANYCHAT_APILEVEL + ")=" + errorcode, LOG_TYPE_API);
                if (errorcode == GV_ERR_SUCCESS) {// 安装成功的情况下
                    // BRAC_SetSDKOption(BRAC_SO_CORESDK_SCREENCAMERACTRL,1);//显示桌面
                    if (mRefreshPluginTimer != -1)// 检查插件是否安装完成定时器
                        clearInterval(mRefreshPluginTimer); // 清除插件安装检测定时器(下面else有定义)
                    //GetID("loginDiv").style.display = "block";
                    //GetID("prompt_div").style.display = "none"; // 隐藏插件安装提示界面
					//BRAC_SetSDKOption(BRAC_SO_VIDEOBKIMAGE, "./img/videobk.jpg");
                    AddLog("AnyChat Plugin Version:" + BRAC_GetVersion(0), LOG_TYPE_NORMAL);
                    AddLog("AnyChat SDK Version:" + BRAC_GetVersion(1), LOG_TYPE_NORMAL);
                    AddLog("Build Time:" + BRAC_GetSDKOptionString(BRAC_SO_CORESDK_BUILDTIME), LOG_TYPE_NORMAL);



    				/* AnyChat可以连接自主部署的服务器、也可以连接AnyChat视频云平台；
			         * 连接自主部署服务器的地址为自设的服务器IP地址或域名、端口；
			         * 连接AnyChat视频云平台的服务器地址为：cloud.anychat.cn；端口为：8906
			         */
			        BRAC_Connect(currentScope.ServerAddr, currentScope.ServerPort);
					
					var errorcode = -1;
					
					/*
			         * AnyChat支持多种用户身份验证方式，包括更安全的签名登录，
			         * 详情请参考：http://bbs.anychat.cn/forum.php?mod=viewthread&tid=2211&highlight=%C7%A9%C3%FB
			         */		
					errorcode = BRAC_Login(currentScope.offerUser.username, "demo", 0);
			    	AddLog("BRAC_Login(" + currentScope.offerUser.username + ")=" + errorcode, LOG_TYPE_API);
			    




                } else { // 没有安装插件，或是插件版本太旧，显示插件下载界面

                    GetID("loginDiv").style.display = "none";
                    GetID("prompt_div").style.display = "block";// 显示插件安装提示界面
                    if (errorcode == GV_ERR_PLUGINNOINSTALL)// 第2个参数指 插件没有安装(编码)
                        GetID("prompt_div_line1").innerHTML = "首次进入需要安装插件，请点击下载按钮进行安装！";
                    else if (errorcode == GV_ERR_PLUGINOLDVERSION)// 第2个参数指
                        // 插件版本太低(编码)
                        GetID("prompt_div_line1").innerHTML = "检测到当前插件的版本过低，请下载安装最新版本！";

                    if (mRefreshPluginTimer == -1) {// 检查插件是否安装完成定时器
                        mRefreshPluginTimer = setInterval(function() {
                            LogicInit();
                        }, 500);
                    }
                }
				
			}, 500);
}

//设置音量感应计时器
function setVolumeTimer(){
	mRefreshVolumeTimer = setInterval(
			function() {
				var LocalAudioVolume= GetID("localVideoPos").offsetHeight * BRAC_QueryUserStateInt(mSelfUserId,BRAC_USERSTATE_SPEAKVOLUME) / 100 + "px";//本地音量大小百分比
				GetID("localAudioVolume").style.width = LocalAudioVolume==0?"0px":LocalAudioVolume;
				if (mTargetUserId != -1) {
				var RemoteAudioVolume=GetID("remoteVideoPos").offsetHeight * BRAC_QueryUserStateInt(mTargetUserId,BRAC_USERSTATE_SPEAKVOLUME) / 100 + "px";//远程音量大小百分比
				GetID("remoteAudioVolume").style.width = RemoteAudioVolume==0?"0px":RemoteAudioVolume;
			    }
	}, 100);
}


// 控制视频打开关闭
function startVideo(uid, videoID, videoType, state) {
	/**视频操作*/
    var errorcode = BRAC_UserCameraControl(uid, state);
    AddLog("BRAC_UserCameraControl(" + uid + "," + state + ")=" + errorcode, LOG_TYPE_API);

	/**语音操作*/
    errorcode = BRAC_UserSpeakControl(uid, state);
    AddLog("BRAC_UserSpeakControl(" + uid + "," + state + ")=" + errorcode, LOG_TYPE_API);

	/**设置视频显示位置*/
    BRAC_SetVideoPos(uid, videoID, videoType);
}

function refreshQueueInfoDisplay(queueID)
{
    //获取当前队列人数
    var queueUserNum = BRAC_ObjectGetIntValue(ANYCHAT_OBJECT_TYPE_QUEUE, queueID, ANYCHAT_QUEUE_INFO_LENGTH);

    $('#poptip li[queueid=' + queueID + '] strong:eq(0)').text(queueUserNum + " 人"); //队列中当前排队人数填充
}


//刷新用户进入队列后，排队等待时的显示信息
function refreshUserWaitingInfo(queueID) {
    var queueUserNum; //当前队列人数
    var beforeUserNum; //排在自己前面的队列人数

    /**获取当前队列人数*/
    queueUserNum = BRAC_ObjectGetIntValue(ANYCHAT_OBJECT_TYPE_QUEUE, queueID, ANYCHAT_QUEUE_INFO_LENGTH);
    $('#queueMsg1 strong:eq(0)').text(queueUserNum);

    /**获取排在自己前面的用户数*/
    beforeUserNum = BRAC_ObjectGetIntValue(ANYCHAT_OBJECT_TYPE_QUEUE, queueID, ANYCHAT_QUEUE_INFO_BEFOREUSERNUM);
    beforeUserNum = beforeUserNum < 0 ? 0 : beforeUserNum;
    beforeUserNum++;

    $('#queueMsg1 strong:eq(0)').text(queueUserNum);
    $('#queueMsg1 strong:eq(1)').text(beforeUserNum);
    queuesUserCounts = queueUserNum;
    $('#sum').text("当前排队总人数:" + queueUserNum + "人").show();

    AddLog("当前队列人数(" + queueUserNum+")");

    //$('#selectList li a[queueid=' + queueID + ']').prev().text(queueUserNum); //队列中当前排队人数填充


}
//刷新坐席进入服务区域后的显示信息
function refreshAgentServiceInfo() {
    if (userType == USER_TYPE_AGNET) {
        var queueCount = BRAC_ObjectGetIntValue(ANYCHAT_OBJECT_TYPE_AREA, hallbuinessNum, ANYCHAT_AREA_INFO_QUEUECOUNT);
        var queuesUserCount = BRAC_ObjectGetIntValue(ANYCHAT_OBJECT_TYPE_AREA, hallbuinessNum, ANYCHAT_AREA_INFO_QUEUEUSERCOUNT);

        //累计服务时长
        var serviceTotalTime = BRAC_ObjectGetIntValue(ANYCHAT_OBJECT_TYPE_AGENT, currentAgentID, ANYCHAT_AGENT_INFO_SERVICETOTALTIME);

        //累计服务的用户数
        var serviceUserCount = BRAC_ObjectGetIntValue(ANYCHAT_OBJECT_TYPE_AGENT, currentAgentID, ANYCHAT_AGENT_INFO_SERVICETOTALNUM);

        AddLog("当前队列人数queueCount(" + queueCount+")");
        AddLog("当前队列人数queuesUserCount(" + queuesUserCount+")");
        AddLog("客服人数(" + serviceUserCount+")");
        AddLog("服务时间(" + serviceTotalTime+")");
        queuesUserCounts = queuesUserCount;
        $('#sum').text("当前排队总人数:" + queuesUserCount + "人").show();

        $('#clientList strong:eq(0)').text(queueCount + "个");
        $('#clientList strong:eq(1)').text(queuesUserCount + "人");
        $('#clientList strong:eq(2)').text(serviceUserCount + "人");
        $('#clientList strong:eq(3)').text(serviceTotalTime + "秒");
    }
}
//刷新当前接通服务的用户信息
//如果userID = -1，则表示清空用户信息
function refreshServicedUserInfo(userID) {

    //当前服务的用户ID
    var serviceUserID = BRAC_ObjectGetIntValue(ANYCHAT_OBJECT_TYPE_AGENT, currentAgentID, ANYCHAT_AGENT_INFO_SERVICEUSERID);

    //用户登录名
    var userName = BRAC_GetUserInfo(userID, USERINFO_NAME); 
    AddLog("服务userName(" + userName+")");
    if (userID == -1) {
        $('#currentServicedUserInfo strong:eq(0)').text("");
    } else {
        $('#currentServicedUserInfo strong:eq(0)').text(userName);
    }
}


//是否显示返回按钮
function isShowReturnBtn(isShow) {
    if (isShow)
        $("#roomOut").show();
    else {
        $("#roomOut").hide();
    }
}
function loadAnyChat(scope){
    currentScope = scope;
	//检测插件
	function check() {
	     //刷新网页加载插件列表
	    if (navigator.plugins && navigator.plugins.length) {
	            window.navigator.plugins.refresh(false);
	    }
	    var errorcode=BRAC_InitSDK(0);
	    if(errorcode==0){
			//初始化成功，清除插件安装检测定时器 
			if(mRefreshPluginTimer != -1){
	                clearInterval(mRefreshPluginTimer);
			} else{
	        	if(errorcode==GV_ERR_PLUGINNOINSTALL){
					//初始化失败，需要安装插件,提供插件下载链接给客户
					alert("初始化失败，需要安装插件,提供插件下载链接给客户");
	 			}else if(errorcode==GV_ERR_PLUGINOLDVERSION){
					//初始化失败，当前插件的版本过低，请下载安装最新版本
					alert("初始化失败，当前插件的版本过低，请下载安装最新版本");
	 			}
	            if(mRefreshPluginTimer == -1) {
	               mRefreshPluginTimer = setInterval(function(){ LogicInit();
	               }, 1000); 
	            }
	        }
	    }
    }


        //日志显示按钮
    $(".showBox").click(function () {
        $("#LOG_DIV_BODY").show();
        $(".showBox").hide();
        $("#LOG_DIV_BODY").animate({
            bottom: 0
        }, "slow");

    });
    // 日志隐藏按钮
    $("#LOG_DIV_TITLE").click(function () {
        $("#LOG_DIV_BODY").animate({
            bottom: -210, display: "none"
        }, "slow");
        $(".showBox").show();
    });
    setTimeout(check,500);
}
