function showAuto(){n=n>=count-1?0:++n,$("#banner_switch .xb li").eq(n).trigger("click")}function checkbrowse(){var e=navigator.userAgent.toLowerCase(),t=(e.match(/\b(chrome|opera|safari|msie|firefox)\b/)||["","mozilla"])[1],n="(?:"+t+"|version)[\\/: ]([\\d.]+)",o=(e.match(new RegExp(n))||[])[1];return jQuery.browser.is=t,jQuery.browser.ver=o,{is:jQuery.browser.is,ver:jQuery.browser.ver}}function getCookie(e){return $.cookie(e)}function setCookie(e,t,n){$.cookie(e,t,{expires:n,path:"/",domain:"biyao.com"})}function setSupported(e){$("#support_"+e).find("p").addClass("checked"),$("#support_"+e).find("p").find("span.supportTxt").text("已赞")}function isSupported(e){return getCookie("mysupports")?$.inArray(e,getCookie("mysupports").split(","))>-1:!1}function addSupport(e){if(!getCookie("mysupports"))return void setCookie("mysupports",e);var t=getCookie("mysupports").split(","),n=new Array;t.push(e);for(var o=0;o<t.length;o++)-1==$.inArray(t[o],n)&&n.push(t[o]);setCookie("mysupports",n.join(","))}function processSupport(e,t){if(!t)return alert("支持失败，请稍后再试！"),void $("#support_"+e).one("click",support);if(1!=t.success)return alert("支持失败，请稍后再试！"),void $("#support_"+e).one("click",support);var n=parseInt($("#cnt_"+e).text());n+=1,$("#cnt_"+e).text(n),setSupported(e),addSupport(e)}function support(){var e=getCookie("uuid"),t=$(this).attr("id").split("_")[1];if(isSupported(t))setSupported(t);else{var n="/home/testSupport.html?uuid="+e+"&ballot_id="+t;$.ajax({type:"get",cache:!1,async:!1,url:n,dataType:"json",success:function(e){processSupport(t,e)}}),$.cookie("addtel")||$(this).dialogFn({type:"confirm",title:"感谢您的支持",height:"212",width:"510",btnText:[""],content:$("#addTelDiv").html(),btnshow:!1,showAfter:function(){$("#submittel").one("click",function(){addtel()})},callback:function(){}})}}function processAddtel(e){e?setCookie("addtel",!0):(alert("提交失败，请稍候再试！"),$("#submittel").one("click",addtel))}function addtel(){$("#addtel_msg").text("").hide();var e=$("#tel").val();if(!e)return $("#addtel_msg").text("请输入您的手机号码！").show(),$("#submittel").one("click",addtel),!1;if(!/^1\d{10}$/.test(e))return $("#addtel_msg").text("请正确输入您的手机号码！").show(),$("#submittel").one("click",addtel),!1;var t=$.cookie("uuid"),n="/home/testTel.html?uuid="+t+"&tel="+e;$.ajax({type:"get",cache:!1,async:!1,url:n,dataType:"json",success:function(e){processAddtel(e)}}),$(".pop_close").trigger("click"),$(this).dialogFn({type:"confirm",title:"感谢您的支持",height:"",width:"510",btnText:[""],content:$("#addTelTip").html(),btnshow:!1,showAfter:function(){$("#tel_btn").one("click",function(){$(".pop_close").trigger("click")})},callback:function(){}})}function startMove(e,t,n){clearInterval(e.timer),e.timer=setInterval(function(){var o=!0;for(var i in t){var r=0;r="opacity"==i?0==Math.round(100*parseFloat(getStyle(e,i)))?Math.round(100*parseFloat(getStyle(e,i))):Math.round(100*parseFloat(getStyle(e,i)))||100:parseInt(getStyle(e,i))||0;var s=(t[i]-r)/8;s=s>0?Math.ceil(s):Math.floor(s),r!=t[i]&&(o=!1),"opacity"==i?(e.style.filter="alpha(opacity="+(r+s)+")",e.style.opacity=(r+s)/100):e.style[i]=r+s+"px"}o&&(clearInterval(e.timer),n&&n.call(e))},30)}function getStyle(e,t){return e.currentStyle?e.currentStyle[t]:getComputedStyle(e,!1)[t]}var t=n=0,count;$(function(){var e=checkbrowse(),o="";if(o="msie"==e.is&&e.ver<8?"show":"fadeIn",jQuery(document).ready(function(e){e("img").lazyload({placeholder:"pc/common/img/grey.gif",effect:o,failurelimit:10})}),count=$("#banner_switch_list li").length,$("#banner_switch_list li:not(:first-child)").hide(),$("#banner_switch .xb li").click(function(){var e=$(this).text()-1;n=e,e>=count||($("#banner_switch_list li").filter(":visible").fadeOut().parent().children().eq(e).fadeIn(),$(this).toggleClass("checked"),$(this).siblings().removeClass("checked"))}),t=setInterval("showAuto()",3e3),$("#banner_switch ").hover(function(){clearInterval(t)},function(){t=setInterval("showAuto()",3e3)}),LT.home(),$(".vote_n_btn").one("click",support),getCookie("mysupports"))for(var i=getCookie("mysupports").split(","),r=0;r<i.length;r++){var s=i[r];setSupported(s)}}),LT.namespace("LT.home"),LT.home=function(){var e,t;t={bindEvent:function(){},focusImg:function(){for(var e,t=$("div["+sSelector+"=J_bannerBox]"),n=t.find("ol li"),o=t.find("ul li"),i=window.screen.availWidth,r=0,s=1,a=function(e,t){e.stop(),e.animate({left:t},800)},l=function(e,t){n.removeClass("checked"),$(e).addClass("checked"),t>r?(o.eq(t).css({left:i}),a(o.eq(r),-i)):r>t&&(o.eq(t).css({left:-i}),a(o.eq(r),i)),a(o.eq(t),0),r=t},c=1;c<o.length;c++)o.eq(c).css({left:i});n.each(function(e){$(this).mouseover(function(){l(this,e)})});var u=function(){e=setInterval(function(){s==n.length&&(s=0),l(n.eq(s),s),s++},5e3)};u(),$(".bannerBox").hover(function(){clearInterval(e)},function(){s=r,u()})},navSelect:function(){$($(".nav_a")[0]).addClass("nav_checked")}},e=function(){for(var e in t)-1==e.indexOf("_")&&t[e]()}()},$(function(){function e(){l==o.length-1?(o[0].style.position="relative",o[0].style.left=o.length*a+"px",l=0):l++,c++;for(var e=0;e<s.length;e++)s[e].className="sm_icon";s[l].className="sm_icon active",startMove(n,{left:-c*a},function(){0==l&&(o[0].style.position="static",n.style.left=0,c=0)})}var t=document.getElementById("banner_item");if(null!=t){var n=t.getElementsByTagName("ul")[0],o=n.getElementsByTagName("li"),i=n.getElementsByTagName("img");if(!(i.length<=0)){var r=document.getElementById("px_ul_btn"),s=r.getElementsByTagName("a"),a=987,l=0,c=0;n.style.width=i.length*a+"px";for(var u=0;u<s.length;u++)s[u].index=u,s[u].onclick=function(){for(var e=0;e<s.length;e++)s[e].className="sm_icon";this.className="sm_icon active",startMove(n,{left:-this.index*a})};window.intervalId=setInterval(e,3e3),$("ul.banner_ul").bind("mouseenter",function(){clearInterval(window.intervalId)}),$("ul.banner_ul").bind("mouseleave",function(){window.intervalId=setInterval(e,3e3)})}}});