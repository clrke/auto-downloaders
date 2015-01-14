# -*- coding: utf-8 -*-

import os, re, glob
import urllib.request
from bs4 import BeautifulSoup

domain = 'https://www.scribd.com/'
download_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'rizal_book/')

def getSoup(url):
	return BeautifulSoup("""<div class="outer_page_container">



  <div class="outer_page only_ie6_border  not_visible" id="outer_page_1" style="width: 1270px; height: 982px;">
      <div class="newpage" id="page1" style="width: 1167px; height: 902px; -webkit-transform: scale(0.7617823479006); -webkit-transform-origin: 0% 0%; display: none;">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/1-f7afcccbfa.jpg">
</div>
</div>
</div>



  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  </div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 1};

        pageParams.containerElem = document.getElementById("outer_page_1");
          pageParams.innerPageElem = document.getElementById("page1");
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_1" class="between_page_ads is_filled" style="display: block; height: 60px;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(1);
      </script><div id="between_page_ads_inner_1" style="position: absolute; width: 468px; height: 60px;"><div id="google_ads_iframe_/1024966/Doc_Between_Top_FullBanner_468x60_0__container__" style="border: 0pt none;"><iframe id="google_ads_iframe_/1024966/Doc_Between_Top_FullBanner_468x60_0" name="google_ads_iframe_/1024966/Doc_Between_Top_FullBanner_468x60_0" width="468" height="60" scrolling="no" marginwidth="0" marginheight="0" frameborder="0" src="javascript:&quot;<html><body style='background:transparent'></body></html>&quot;" style="border: 0px; vertical-align: bottom;"></iframe></div><iframe id="google_ads_iframe_/1024966/Doc_Between_Top_FullBanner_468x60_0__hidden__" name="google_ads_iframe_/1024966/Doc_Between_Top_FullBanner_468x60_0__hidden__" width="0" height="0" scrolling="no" marginwidth="0" marginheight="0" frameborder="0" src="javascript:&quot;<html><body style='background:transparent'></body></html>&quot;" style="border: 0px; vertical-align: bottom; visibility: hidden; display: none;"></iframe></div>
    </div>




  <div class="outer_page only_ie6_border  not_visible" id="outer_page_2" style="width: 1270px; height: 982px;">
      <div class="newpage" id="page2" style="width: 1167px; height: 902px; -webkit-transform: scale(0.7617823479006); -webkit-transform-origin: 0% 0%; display: none;">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/2-a987cf8259.jpg">
</div>
</div>
</div>



  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  </div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 2};

        pageParams.containerElem = document.getElementById("outer_page_2");
          pageParams.innerPageElem = document.getElementById("page2");
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_2" class="between_page_ads is_filled" style="display: block; height: 90px;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(2);
      </script><div id="between_page_ads_inner_2" style="position: absolute; width: 728px; height: 90px;"><div id="google_ads_iframe_/1024966/Doc_Between_Leaderboard_BTF_728x90_2_0__container__" style="border: 0pt none; display: inline-block; width: 728px; height: 90px;"><iframe frameborder="0" src="https://tpc.googlesyndication.com/safeframe/1-0-1/html/container.html#xpc=sf-gdn-exp-1&amp;p=https%3A//www.scribd.com" id="google_ads_iframe_/1024966/Doc_Between_Leaderboard_BTF_728x90_2_0" name="1-0-1;78924;<!doctype html><html><head><link href=&quot;https://fonts.googleapis.com/css?family=Ubuntu:300&amp;amp;lang=en&quot; rel=&quot;stylesheet&quot; type=&quot;text/css&quot;><style>a{color:#3d81ee}body,table,div,ul,li{margin:0;padding:0}body{background-color:transparent;font-family:&quot;Ubuntu&quot;,arial,sans-serif;font-weight:300;}</style><script>(function(){var d=this,f=function(a){var b=typeof a;if(&quot;object&quot;==b)if(a){if(a instanceof Array)return&quot;array&quot;;if(a instanceof Object)return b;var c=Object.prototype.toString.call(a);if(&quot;[object Window]&quot;==c)return&quot;object&quot;;if(&quot;[object Array]&quot;==c||&quot;number&quot;==typeof a.length&amp;&amp;&quot;undefined&quot;!=typeof a.splice&amp;&amp;&quot;undefined&quot;!=typeof a.propertyIsEnumerable&amp;&amp;!a.propertyIsEnumerable(&quot;splice&quot;))return&quot;array&quot;;if(&quot;[object Function]&quot;==c||&quot;undefined&quot;!=typeof a.call&amp;&amp;&quot;undefined&quot;!=typeof a.propertyIsEnumerable&amp;&amp;!a.propertyIsEnumerable(&quot;call&quot;))return&quot;function&quot;}else return&quot;null&quot;;else if(&quot;function&quot;==b&amp;&amp;&quot;undefined&quot;==typeof a.call)return&quot;object&quot;;return b};var g;e:{var h=d.navigator;if(h){var k=h.userAgent;if(k){g=k;break e}}g=&quot;&quot;};var l=-1!=g.indexOf(&quot;Opera&quot;)||-1!=g.indexOf(&quot;OPR&quot;),n=-1!=g.indexOf(&quot;Trident&quot;)||-1!=g.indexOf(&quot;MSIE&quot;),p=-1!=g.indexOf(&quot;Gecko&quot;)&amp;&amp;-1==g.toLowerCase().indexOf(&quot;webkit&quot;)&amp;&amp;!(-1!=g.indexOf(&quot;Trident&quot;)||-1!=g.indexOf(&quot;MSIE&quot;)),q=-1!=g.toLowerCase().indexOf(&quot;webkit&quot;);(function(){var a=&quot;&quot;,b;if(l&amp;&amp;d.opera)return a=d.opera.version,&quot;function&quot;==f(a)?a():a;p?b=/rv\:([^\);]+)(\)|;)/:n?b=/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/:q&amp;&amp;(b=/WebKit\/(\S+)/);b&amp;&amp;(a=(a=b.exec(g))?a[1]:&quot;&quot;);return n&amp;&amp;(b=(b=d.document)?b.documentMode:void 0,b>parseFloat(a))?String(b):a})();var r={};window.ss=function(a){void 0!==r[a]?r[a]++:r[a]=1;var b=document.getElementById(a),c=r[a];if(window.css)css(a,&quot;nm&quot;,c,void 0,void 0);else if(b){a=b.href;var e=a.indexOf(&quot;&amp;nm=&quot;);if(0>e)c=a+&quot;&amp;nm=&quot;+c;else var e=e+4,m=a.indexOf(&quot;&amp;&quot;,e),c=0<=m?a.substring(0,e)+c+a.substring(m):a.substring(0,e)+c;b.href=2E3<c.length?a:c}};})();function su(id) {var a = document.getElementById(id);var b = (new Date()).getTime();if (a &amp;&amp; a.myt &amp;&amp; b) {var t = b - a.myt;if (window.css) {css(id,'clkt',t);return;}var bi = a.href.indexOf(&quot;&amp;clkt=&quot;);if (bi > 0) {var c = a.href.substring(0, bi+6); var d = a.href.substring(bi+6, a.href.length);var ei = d.indexOf(&quot;&amp;&quot;);var r = '';if (ei >= 0)r = d.substring(ei, d.length);a.href = c + t + r; } else {a.href += &quot;&amp;clkt=&quot; + t;}}}(function(){var c=this,e=function(a){var b=typeof a;if(&quot;object&quot;==b)if(a){if(a instanceof Array)return&quot;array&quot;;if(a instanceof Object)return b;var d=Object.prototype.toString.call(a);if(&quot;[object Window]&quot;==d)return&quot;object&quot;;if(&quot;[object Array]&quot;==d||&quot;number&quot;==typeof a.length&amp;&amp;&quot;undefined&quot;!=typeof a.splice&amp;&amp;&quot;undefined&quot;!=typeof a.propertyIsEnumerable&amp;&amp;!a.propertyIsEnumerable(&quot;splice&quot;))return&quot;array&quot;;if(&quot;[object Function]&quot;==d||&quot;undefined&quot;!=typeof a.call&amp;&amp;&quot;undefined&quot;!=typeof a.propertyIsEnumerable&amp;&amp;!a.propertyIsEnumerable(&quot;call&quot;))return&quot;function&quot;}else return&quot;null&quot;;else if(&quot;function&quot;==b&amp;&amp;&quot;undefined&quot;==typeof a.call)return&quot;object&quot;;return b};var f;e:{var g=c.navigator;if(g){var h=g.userAgent;if(h){f=h;break e}}f=&quot;&quot;};var k=-1!=f.indexOf(&quot;Opera&quot;)||-1!=f.indexOf(&quot;OPR&quot;),l=-1!=f.indexOf(&quot;Trident&quot;)||-1!=f.indexOf(&quot;MSIE&quot;),p=-1!=f.indexOf(&quot;Gecko&quot;)&amp;&amp;-1==f.toLowerCase().indexOf(&quot;webkit&quot;)&amp;&amp;!(-1!=f.indexOf(&quot;Trident&quot;)||-1!=f.indexOf(&quot;MSIE&quot;)),q=-1!=f.toLowerCase().indexOf(&quot;webkit&quot;);(function(){var a=&quot;&quot;,b;if(k&amp;&amp;c.opera)return a=c.opera.version,&quot;function&quot;==e(a)?a():a;p?b=/rv\:([^\);]+)(\)|;)/:l?b=/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/:q&amp;&amp;(b=/WebKit\/(\S+)/);b&amp;&amp;(a=(a=b.exec(f))?a[1]:&quot;&quot;);return l&amp;&amp;(b=(b=c.document)?b.documentMode:void 0,b>parseFloat(a))?String(b):a})();var r={},t=function(a,b){void 0!==r[a]||(r[a]=[]);var d=r[a][b];d||(r[a][b]=!0);if(!d)if(d=document.getElementById(a),window.css)css(a,&quot;nb&quot;,b,!0,void 0);else if(d){var m=d.href,n=m+(&quot;&amp;nb=&quot;+b);d.href=2E3<n.length?m:n}};window.cll=function(a,b){t(a,b||1)};window.clb=function(a){t(a,2)};window.clh=function(a,b){t(a,b||0)};})();(function(){var d=this,g=function(a){var b=typeof a;if(&quot;object&quot;==b)if(a){if(a instanceof Array)return&quot;array&quot;;if(a instanceof Object)return b;var c=Object.prototype.toString.call(a);if(&quot;[object Window]&quot;==c)return&quot;object&quot;;if(&quot;[object Array]&quot;==c||&quot;number&quot;==typeof a.length&amp;&amp;&quot;undefined&quot;!=typeof a.splice&amp;&amp;&quot;undefined&quot;!=typeof a.propertyIsEnumerable&amp;&amp;!a.propertyIsEnumerable(&quot;splice&quot;))return&quot;array&quot;;if(&quot;[object Function]&quot;==c||&quot;undefined&quot;!=typeof a.call&amp;&amp;&quot;undefined&quot;!=typeof a.propertyIsEnumerable&amp;&amp;!a.propertyIsEnumerable(&quot;call&quot;))return&quot;function&quot;}else return&quot;null&quot;;else if(&quot;function&quot;==b&amp;&amp;&quot;undefined&quot;==typeof a.call)return&quot;object&quot;;return b};var h;e:{var k=d.navigator;if(k){var l=k.userAgent;if(l){h=l;break e}}h=&quot;&quot;};var m=-1!=h.indexOf(&quot;Opera&quot;)||-1!=h.indexOf(&quot;OPR&quot;),n=-1!=h.indexOf(&quot;Trident&quot;)||-1!=h.indexOf(&quot;MSIE&quot;),p=-1!=h.indexOf(&quot;Gecko&quot;)&amp;&amp;-1==h.toLowerCase().indexOf(&quot;webkit&quot;)&amp;&amp;!(-1!=h.indexOf(&quot;Trident&quot;)||-1!=h.indexOf(&quot;MSIE&quot;)),q=-1!=h.toLowerCase().indexOf(&quot;webkit&quot;);(function(){var a=&quot;&quot;,b;if(m&amp;&amp;d.opera)return a=d.opera.version,&quot;function&quot;==g(a)?a():a;p?b=/rv\:([^\);]+)(\)|;)/:n?b=/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/:q&amp;&amp;(b=/WebKit\/(\S+)/);b&amp;&amp;(a=(a=b.exec(h))?a[1]:&quot;&quot;);return n&amp;&amp;(b=(b=d.document)?b.documentMode:void 0,b>parseFloat(a))?String(b):a})();var r=function(a,b,c,e){if(window.css)css(b,c,e,void 0,void 0);else if(a){b=a.href;var f=&quot;&amp;&quot;+c+&quot;=&quot;;c=b.indexOf(f);0>c?e=b+f+e:(c+=f.length,f=b.indexOf(&quot;&amp;&quot;,c),e=0<=f?b.substring(0,c)+e+b.substring(f):b.substring(0,c)+e);a.href=2E3<e.length?b:e}};var t=null,u=function(a){t=a};document.addEventListener&amp;&amp;document.addEventListener(&quot;mousedown&quot;,u,!0);window.xy=function(a,b,c){c=c||b;if((a=a||t)&amp;&amp;b&amp;&amp;c){var e=Math.round(a.clientY-c.offsetTop),f=b.id;r(b,f,&quot;nx&quot;,Math.round(a.clientX-c.offsetLeft));r(b,f,&quot;ny&quot;,e)}};})();(function(){var d=this,f=function(a){var b=typeof a;if(&quot;object&quot;==b)if(a){if(a instanceof Array)return&quot;array&quot;;if(a instanceof Object)return b;var c=Object.prototype.toString.call(a);if(&quot;[object Window]&quot;==c)return&quot;object&quot;;if(&quot;[object Array]&quot;==c||&quot;number&quot;==typeof a.length&amp;&amp;&quot;undefined&quot;!=typeof a.splice&amp;&amp;&quot;undefined&quot;!=typeof a.propertyIsEnumerable&amp;&amp;!a.propertyIsEnumerable(&quot;splice&quot;))return&quot;array&quot;;if(&quot;[object Function]&quot;==c||&quot;undefined&quot;!=typeof a.call&amp;&amp;&quot;undefined&quot;!=typeof a.propertyIsEnumerable&amp;&amp;!a.propertyIsEnumerable(&quot;call&quot;))return&quot;function&quot;}else return&quot;null&quot;;else if(&quot;function&quot;==b&amp;&amp;&quot;undefined&quot;==typeof a.call)return&quot;object&quot;;return b};var g;e:{var h=d.navigator;if(h){var k=h.userAgent;if(k){g=k;break e}}g=&quot;&quot;};var l=-1!=g.indexOf(&quot;Opera&quot;)||-1!=g.indexOf(&quot;OPR&quot;),n=-1!=g.indexOf(&quot;Trident&quot;)||-1!=g.indexOf(&quot;MSIE&quot;),p=-1!=g.indexOf(&quot;Gecko&quot;)&amp;&amp;-1==g.toLowerCase().indexOf(&quot;webkit&quot;)&amp;&amp;!(-1!=g.indexOf(&quot;Trident&quot;)||-1!=g.indexOf(&quot;MSIE&quot;)),q=-1!=g.toLowerCase().indexOf(&quot;webkit&quot;);(function(){var a=&quot;&quot;,b;if(l&amp;&amp;d.opera)return a=d.opera.version,&quot;function&quot;==f(a)?a():a;p?b=/rv\:([^\);]+)(\)|;)/:n?b=/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/:q&amp;&amp;(b=/WebKit\/(\S+)/);b&amp;&amp;(a=(a=b.exec(g))?a[1]:&quot;&quot;);return n&amp;&amp;(b=(b=d.document)?b.documentMode:void 0,b>parseFloat(a))?String(b):a})();var r=[0,2,1],t=null;document.addEventListener&amp;&amp;document.addEventListener(&quot;mousedown&quot;,function(a){t=a},!0);window.mb=function(a){if(a){var b=window.event||t;if(b){var c;(c=b.which?1<<r[b.which-1]:b.button)&amp;&amp;b.shiftKey&amp;&amp;(c|=8);c&amp;&amp;b.altKey&amp;&amp;(c|=16);c&amp;&amp;b.ctrlKey&amp;&amp;(c|=32);if(c)if(window.css)css(a.id,&quot;mb&quot;,c,void 0,void 0);else if(a){var b=a.href,e=b.indexOf(&quot;&amp;mb=&quot;);if(0>e)c=b+&quot;&amp;mb=&quot;+c;else{var e=e+4,m=b.indexOf(&quot;&amp;&quot;,e);c=0<=m?b.substring(0,e)+c+b.substring(m):b.substring(0,e)+c}a.href=2E3<c.length?b:c}}}};})();(function(){var c=function(a,e,h){var b=document;b.addEventListener?b.addEventListener(a,e,h||!1):b.attachEvent&amp;&amp;b.attachEvent(&quot;on&quot;+a,e)};var d,f=!1,g=!1;c(&quot;mousedown&quot;,function(){f=!0});c(&quot;keydown&quot;,function(){g=!0});document.addEventListener&amp;&amp;c(&quot;click&quot;,function(a){d=a},!0);window.accbk=function(){var a=d?d:window.event;return a?f||g?!1:(a.preventDefault?a.preventDefault():a.returnValue=!1,!0):!1};})();function st(id) {var a = document.getElementById(id);if (a) {a.myt = (new Date()).getTime();xy(window.event, a);mb(a);}}function ha(a,x){  clh(a,x);if (accbk()) return;su(a);}function ca(a) {clb(a,x);su(a);top.location.href=document.getElementById(a).href;}function ia(a,e,x) {if (accbk()) return;cll(a,x);su(a);}function ga(o,e,x) {if (document.getElementById) {var a=o.id.substring(1),p=&quot;&quot;,r=&quot;&quot;,g=e.target,t,f,h;if (g) {t=g.id;f=g.parentNode;if (f) {p=f.id;h=f.parentNode;if (h)r=h.id;}} else {h=e.srcElement;f=h.parentNode;if (f)p=f.id;t=h.id;}if (t==a||p==a||r==a)return true;ia(a,e,x);top.location.href=document.getElementById(a).href;}}</script><script>(function(){var h,k=this,aa=function(a){var b=typeof a;if(&quot;object&quot;==b)if(a){if(a instanceof Array)return&quot;array&quot;;if(a instanceof Object)return b;var c=Object.prototype.toString.call(a);if(&quot;[object Window]&quot;==c)return&quot;object&quot;;if(&quot;[object Array]&quot;==c||&quot;number&quot;==typeof a.length&amp;&amp;&quot;undefined&quot;!=typeof a.splice&amp;&amp;&quot;undefined&quot;!=typeof a.propertyIsEnumerable&amp;&amp;!a.propertyIsEnumerable(&quot;splice&quot;))return&quot;array&quot;;if(&quot;[object Function]&quot;==c||&quot;undefined&quot;!=typeof a.call&amp;&amp;&quot;undefined&quot;!=typeof a.propertyIsEnumerable&amp;&amp;!a.propertyIsEnumerable(&quot;call&quot;))return&quot;function&quot;}else return&quot;null&quot;;else if(&quot;function&quot;==b&amp;&amp;&quot;undefined&quot;==typeof a.call)return&quot;object&quot;;return b},m=function(a){return&quot;string&quot;==typeof a},p=function(a){return&quot;function&quot;==aa(a)},ba=function(a,b,c){return a.call.apply(a.bind,arguments)},da=function(a,b,c){if(!a)throw Error();if(2<arguments.length){var d=Array.prototype.slice.call(arguments,2);return function(){var c=Array.prototype.slice.call(arguments);Array.prototype.unshift.apply(c,d);return a.apply(b,c)}}return function(){return a.apply(b,arguments)}},q=function(a,b,c){q=Function.prototype.bind&amp;&amp;-1!=Function.prototype.bind.toString().indexOf(&quot;native code&quot;)?ba:da;return q.apply(null,arguments)},ea=function(a,b){var c=Array.prototype.slice.call(arguments,1);return function(){var b=c.slice();b.push.apply(b,arguments);return a.apply(this,b)}},r=function(a,b){var c=a.split(&quot;.&quot;),d=k;c[0]in d||!d.execScript||d.execScript(&quot;var &quot;+c[0]);for(var e;c.length&amp;&amp;(e=c.shift());)c.length||void 0===b?d=d[e]?d[e]:d[e]={}:d[e]=b},u=function(a,b){function c(){}c.prototype=b.prototype;a.$a=b.prototype;a.prototype=new c;a.sb=function(a,c,f){for(var g=Array(arguments.length-2),l=2;l<arguments.length;l++)g[l-2]=arguments[l];return b.prototype[c].apply(a,g)}};var fa=String.prototype.trim?function(a){return a.trim()}:function(a){return a.replace(/^[\s\xa0]+|[\s\xa0]+$/g,&quot;&quot;)},v=function(a,b){return-1!=a.indexOf(b)},ja=function(a,b){return a<b?-1:a>b?1:0};var ka=function(a){this.g=a||[]},la=function(a){this.g=a||[]},ma=function(a){this.g=a||[]},w=function(a){a=a.g[3];return null!=a?a:!1};ka.prototype.getEscapedQemQueryId=function(){var a=this.g[6];return null!=a?a:&quot;&quot;};ka.prototype.getEscapedGwsQueryId=function(){var a=this.g[7];return null!=a?a:&quot;&quot;};var na=new la,x=function(a){return(a=a.g[5])?new la(a):na},oa=function(a){a=a.g[4];return null!=a?a:&quot;&quot;};var y=Array.prototype,pa=y.indexOf?function(a,b,c){return y.indexOf.call(a,b,c)}:function(a,b,c){c=null==c?0:0>c?Math.max(0,a.length+c):c;if(m(a))return m(b)&amp;&amp;1==b.length?a.indexOf(b,c):-1;for(;c<a.length;c++)if(c in a&amp;&amp;a[c]===b)return c;return-1},qa=y.forEach?function(a,b,c){y.forEach.call(a,b,c)}:function(a,b,c){for(var d=a.length,e=m(a)?a.split(&quot;&quot;):a,f=0;f<d;f++)f in e&amp;&amp;b.call(c,e[f],f,a)},ra=function(a){return y.concat.apply(y,arguments)},sa=function(a){var b=a.length;if(0<b){for(var c=Array(b),d=0;d<b;d++)c[d]=a[d];return c}return[]};var ta=function(a){ta[&quot; &quot;](a);return a};ta[&quot; &quot;]=function(){};var ua=function(a,b){for(var c in a)b.call(void 0,a[c],c,a)},va=&quot;constructor hasOwnProperty isPrototypeOf propertyIsEnumerable toLocaleString toString valueOf&quot;.split(&quot; &quot;),wa=function(a,b){for(var c,d,e=1;e<arguments.length;e++){d=arguments[e];for(c in d)a[c]=d[c];for(var f=0;f<va.length;f++)c=va[f],Object.prototype.hasOwnProperty.call(d,c)&amp;&amp;(a[c]=d[c])}},xa=function(a){var b=arguments.length;if(1==b&amp;&amp;&quot;array&quot;==aa(arguments[0]))return xa.apply(null,arguments[0]);for(var c={},d=0;d<b;d++)c[arguments[d]]=!0;return c};var z;i:{var ya=k.navigator;if(ya){var za=ya.userAgent;if(za){z=za;break i}}z=&quot;&quot;};var Aa=v(z,&quot;Opera&quot;)||v(z,&quot;OPR&quot;),A=v(z,&quot;Trident&quot;)||v(z,&quot;MSIE&quot;),B=v(z,&quot;Gecko&quot;)&amp;&amp;!v(z.toLowerCase(),&quot;webkit&quot;)&amp;&amp;!(v(z,&quot;Trident&quot;)||v(z,&quot;MSIE&quot;)),C=v(z.toLowerCase(),&quot;webkit&quot;),Ba=v(z,&quot;Android&quot;),Ca=function(){var a=k.document;return a?a.documentMode:void 0},Da=function(){var a=&quot;&quot;,b;if(Aa&amp;&amp;k.opera)return a=k.opera.version,p(a)?a():a;B?b=/rv\:([^\);]+)(\)|;)/:A?b=/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/:C&amp;&amp;(b=/WebKit\/(\S+)/);b&amp;&amp;(a=(a=b.exec(z))?a[1]:&quot;&quot;);return A&amp;&amp;(b=Ca(),b>parseFloat(a))?String(b):a}(),Ea={},D=function(a){var b;if(!(b=Ea[a])){b=0;for(var c=fa(String(Da)).split(&quot;.&quot;),d=fa(String(a)).split(&quot;.&quot;),e=Math.max(c.length,d.length),f=0;0==b&amp;&amp;f<e;f++){var g=c[f]||&quot;&quot;,l=d[f]||&quot;&quot;,n=RegExp(&quot;(\\d*)(\\D*)&quot;,&quot;g&quot;),t=RegExp(&quot;(\\d*)(\\D*)&quot;,&quot;g&quot;);do{var X=n.exec(g)||[&quot;&quot;,&quot;&quot;,&quot;&quot;],Y=t.exec(l)||[&quot;&quot;,&quot;&quot;,&quot;&quot;];if(0==X[0].length&amp;&amp;0==Y[0].length)break;b=ja(0==X[1].length?0:parseInt(X[1],10),0==Y[1].length?0:parseInt(Y[1],10))||ja(0==X[2].length,0==Y[2].length)||ja(X[2],Y[2])}while(0==b)}b=Ea[a]=0<=b}return b},Fa=k.document,Ga=Fa&amp;&amp;A?Ca()||(&quot;CSS1Compat&quot;==Fa.compatMode?parseInt(Da,10):5):void 0;var Ha=!A||A&amp;&amp;9<=Ga,Ia=A&amp;&amp;!D(&quot;9&quot;);!C||D(&quot;528&quot;);B&amp;&amp;D(&quot;1.9b&quot;)||A&amp;&amp;D(&quot;8&quot;)||Aa&amp;&amp;D(&quot;9.5&quot;)||C&amp;&amp;D(&quot;528&quot;);B&amp;&amp;!D(&quot;8&quot;)||A&amp;&amp;D(&quot;9&quot;);var Ja=function(){this.Qa=this.Qa;this.cb=this.cb};Ja.prototype.Qa=!1;var E=function(a,b){this.type=a;this.currentTarget=this.target=b;this.defaultPrevented=this.Q=!1;this.Ga=!0};E.prototype.preventDefault=function(){this.defaultPrevented=!0;this.Ga=!1};var F=function(a,b){E.call(this,a?a.type:&quot;&quot;);this.relatedTarget=this.currentTarget=this.target=null;this.charCode=this.keyCode=this.button=this.screenY=this.screenX=this.clientY=this.clientX=this.offsetY=this.offsetX=0;this.metaKey=this.shiftKey=this.altKey=this.ctrlKey=!1;this.G=this.state=null;if(a){this.G=a;var c=this.type=a.type;this.target=a.target||a.srcElement;this.currentTarget=b;var d=a.relatedTarget;if(d){if(B){var e;i:{try{ta(d.nodeName);e=!0;break i}catch(f){}e=!1}e||(d=null)}}else&quot;mouseover&quot;==c?d=a.fromElement:&quot;mouseout&quot;==c&amp;&amp;(d=a.toElement);this.relatedTarget=d;Object.defineProperties?Object.defineProperties(this,{offsetX:{configurable:!0,enumerable:!0,get:this.Na,set:this.Ya},offsetY:{configurable:!0,enumerable:!0,get:this.Oa,set:this.Za}}):(this.offsetX=this.Na(),this.offsetY=this.Oa());this.clientX=void 0!==a.clientX?a.clientX:a.pageX;this.clientY=void 0!==a.clientY?a.clientY:a.pageY;this.screenX=a.screenX||0;this.screenY=a.screenY||0;this.button=a.button;this.keyCode=a.keyCode||0;this.charCode=a.charCode||(&quot;keypress&quot;==c?a.keyCode:0);this.ctrlKey=a.ctrlKey;this.altKey=a.altKey;this.shiftKey=a.shiftKey;this.metaKey=a.metaKey;this.state=a.state;a.defaultPrevented&amp;&amp;this.preventDefault()}};u(F,E);h=F.prototype;h.preventDefault=function(){F.$a.preventDefault.call(this);var a=this.G;if(a.preventDefault)a.preventDefault();else if(a.returnValue=!1,Ia)try{if(a.ctrlKey||112<=a.keyCode&amp;&amp;123>=a.keyCode)a.keyCode=-1}catch(b){}};h.Na=function(){return C||void 0!==this.G.offsetX?this.G.offsetX:this.G.layerX};h.Ya=function(a){Object.defineProperties(this,{offsetX:{writable:!0,enumerable:!0,configurable:!0,value:a}})};h.Oa=function(){return C||void 0!==this.G.offsetY?this.G.offsetY:this.G.layerY};h.Za=function(a){Object.defineProperties(this,{offsetY:{writable:!0,enumerable:!0,configurable:!0,value:a}})};var G=&quot;closure_listenable_&quot;+(1E6*Math.random()|0),Ka=0;var La=function(a,b,c,d,e){this.K=a;this.aa=null;this.src=b;this.type=c;this.X=!!d;this.Z=e;this.key=++Ka;this.M=this.Y=!1},Ma=function(a){a.M=!0;a.K=null;a.aa=null;a.src=null;a.Z=null};var H=function(a){this.src=a;this.o={};this.ea=0};H.prototype.add=function(a,b,c,d,e){var f=a.toString();a=this.o[f];a||(a=this.o[f]=[],this.ea++);var g=Na(a,b,d,e);-1<g?(b=a[g],c||(b.Y=!1)):(b=new La(b,this.src,f,!!d,e),b.Y=c,a.push(b));return b};H.prototype.remove=function(a,b,c,d){a=a.toString();if(!(a in this.o))return!1;var e=this.o[a];b=Na(e,b,c,d);return-1<b?(Ma(e[b]),y.splice.call(e,b,1),0==e.length&amp;&amp;(delete this.o[a],this.ea--),!0):!1};var Oa=function(a,b){var c=b.type;if(c in a.o){var d=a.o[c],e=pa(d,b),f;(f=0<=e)&amp;&amp;y.splice.call(d,e,1);f&amp;&amp;(Ma(b),0==a.o[c].length&amp;&amp;(delete a.o[c],a.ea--))}};H.prototype.wa=function(a,b,c,d){a=this.o[a.toString()];var e=-1;a&amp;&amp;(e=Na(a,b,c,d));return-1<e?a[e]:null};var Na=function(a,b,c,d){for(var e=0;e<a.length;++e){var f=a[e];if(!f.M&amp;&amp;f.K==b&amp;&amp;f.X==!!c&amp;&amp;f.Z==d)return e}return-1};var Pa=&quot;closure_lm_&quot;+(1E6*Math.random()|0),Qa={},Ra=0,Sa=function(a,b,c,d,e){if(&quot;array&quot;==aa(b))for(var f=0;f<b.length;f++)Sa(a,b[f],c,d,e);else if(c=Ta(c),a&amp;&amp;a[G])a.listen(b,c,d,e);else{if(!b)throw Error(&quot;Invalid event type&quot;);var f=!!d,g=Ua(a);g||(a[Pa]=g=new H(a));c=g.add(b,c,!1,d,e);c.aa||(d=Va(),c.aa=d,d.src=a,d.K=c,a.addEventListener?a.addEventListener(b.toString(),d,f):a.attachEvent(Wa(b.toString()),d),Ra++)}},Va=function(){var a=Xa,b=Ha?function(c){return a.call(b.src,b.K,c)}:function(c){c=a.call(b.src,b.K,c);if(!c)return c};return b},Ya=function(a,b,c,d,e){if(&quot;array&quot;==aa(b))for(var f=0;f<b.length;f++)Ya(a,b[f],c,d,e);else c=Ta(c),a&amp;&amp;a[G]?a.unlisten(b,c,d,e):a&amp;&amp;(a=Ua(a))&amp;&amp;(b=a.wa(b,c,!!d,e))&amp;&amp;Za(b)},Za=function(a){if(&quot;number&quot;!=typeof a&amp;&amp;a&amp;&amp;!a.M){var b=a.src;if(b&amp;&amp;b[G])Oa(b.P,a);else{var c=a.type,d=a.aa;b.removeEventListener?b.removeEventListener(c,d,a.X):b.detachEvent&amp;&amp;b.detachEvent(Wa(c),d);Ra--;(c=Ua(b))?(Oa(c,a),0==c.ea&amp;&amp;(c.src=null,b[Pa]=null)):Ma(a)}}},Wa=function(a){return a in Qa?Qa[a]:Qa[a]=&quot;on&quot;+a},ab=function(a,b,c,d){var e=!0;if(a=Ua(a))if(b=a.o[b.toString()])for(b=b.concat(),a=0;a<b.length;a++){var f=b[a];f&amp;&amp;f.X==c&amp;&amp;!f.M&amp;&amp;(f=$a(f,d),e=e&amp;&amp;!1!==f)}return e},$a=function(a,b){var c=a.K,d=a.Z||a.src;a.Y&amp;&amp;Za(a);return c.call(d,b)},Xa=function(a,b){if(a.M)return!0;if(!Ha){var c;if(!(c=b))i:{c=[&quot;window&quot;,&quot;event&quot;];for(var d=k,e;e=c.shift();)if(null!=d[e])d=d[e];else{c=null;break i}c=d}e=c;c=new F(e,this);d=!0;if(!(0>e.keyCode||void 0!=e.returnValue)){i:{var f=!1;if(0==e.keyCode)try{e.keyCode=-1;break i}catch(g){f=!0}if(f||void 0==e.returnValue)e.returnValue=!0}e=[];for(f=c.currentTarget;f;f=f.parentNode)e.push(f);for(var f=a.type,l=e.length-1;!c.Q&amp;&amp;0<=l;l--){c.currentTarget=e[l];var n=ab(e[l],f,!0,c),d=d&amp;&amp;n}for(l=0;!c.Q&amp;&amp;l<e.length;l++)c.currentTarget=e[l],n=ab(e[l],f,!1,c),d=d&amp;&amp;n}return d}return $a(a,new F(b,this))},Ua=function(a){a=a[Pa];return a instanceof H?a:null},bb=&quot;__closure_events_fn_&quot;+(1E9*Math.random()>>>0),Ta=function(a){if(p(a))return a;a[bb]||(a[bb]=function(b){return a.handleEvent(b)});return a[bb]};var I=function(){Ja.call(this);this.P=new H(this);this.Ua=this;this.Pa=null};u(I,Ja);I.prototype[G]=!0;h=I.prototype;h.addEventListener=function(a,b,c,d){Sa(this,a,b,c,d)};h.removeEventListener=function(a,b,c,d){Ya(this,a,b,c,d)};h.dispatchEvent=function(a){var b,c=this.Pa;if(c)for(b=[];c;c=c.Pa)b.push(c);var c=this.Ua,d=a.type||a;if(m(a))a=new E(a,c);else if(a instanceof E)a.target=a.target||c;else{var e=a;a=new E(d,c);wa(a,e)}var e=!0,f;if(b)for(var g=b.length-1;!a.Q&amp;&amp;0<=g;g--)f=a.currentTarget=b[g],e=J(f,d,!0,a)&amp;&amp;e;a.Q||(f=a.currentTarget=c,e=J(f,d,!0,a)&amp;&amp;e,a.Q||(e=J(f,d,!1,a)&amp;&amp;e));if(b)for(g=0;!a.Q&amp;&amp;g<b.length;g++)f=a.currentTarget=b[g],e=J(f,d,!1,a)&amp;&amp;e;return e};h.listen=function(a,b,c,d){return this.P.add(String(a),b,!1,c,d)};h.unlisten=function(a,b,c,d){return this.P.remove(String(a),b,c,d)};var J=function(a,b,c,d){b=a.P.o[String(b)];if(!b)return!0;b=b.concat();for(var e=!0,f=0;f<b.length;++f){var g=b[f];if(g&amp;&amp;!g.M&amp;&amp;g.X==c){var l=g.K,n=g.Z||g.src;g.Y&amp;&amp;Oa(a.P,g);e=!1!==l.call(n,d)&amp;&amp;e}}return e&amp;&amp;0!=d.Ga};I.prototype.wa=function(a,b,c,d){return this.P.wa(String(a),b,c,d)};var cb=function(a,b,c,d){a.addEventListener?a.addEventListener(b,c,d||!1):a.attachEvent&amp;&amp;a.attachEvent(&quot;on&quot;+b,c)},db=function(a,b,c,d){a.removeEventListener?a.removeEventListener(b,c,d||!1):a.detachEvent&amp;&amp;a.detachEvent(&quot;on&quot;+b,c)};var eb=function(a,b){var c=window;c.google_image_requests||(c.google_image_requests=[]);var d=c.document.createElement(&quot;img&quot;);if(b){var e=function(a){b(a);db(d,&quot;load&quot;,e);db(d,&quot;error&quot;,e)};cb(d,&quot;load&quot;,e);cb(d,&quot;error&quot;,e)}d.src=a;c.google_image_requests.push(d)};var fb=window;var gb=function(a,b,c,d,e,f){var g;if(document.createEvent)g=document.createEvent(&quot;MouseEvents&quot;),g.initMouseEvent(b,!0,!0,null,0,0,0,0,0,d,!1,e,f,c,null);else if(document.createEventObject)g=document.createEventObject(),g.va=&quot;on&quot;+b,g.button=c,g.ctrlKey=d,g.shiftKey=e,g.metaKey=f;else return!1;document.createEvent?a.dispatchEvent(g):a.fireEvent(g.va,g);return!0},ib=function(a){a.preventDefault?a.preventDefault():a.returnValue=!1};var jb=function(a){k.setTimeout(function(){throw a;},0)},kb,lb=function(){var a=k.MessageChannel;&quot;undefined&quot;===typeof a&amp;&amp;&quot;undefined&quot;!==typeof window&amp;&amp;window.postMessage&amp;&amp;window.addEventListener&amp;&amp;(a=function(){var a=document.createElement(&quot;iframe&quot;);a.style.display=&quot;none&quot;;a.src=&quot;&quot;;document.documentElement.appendChild(a);var b=a.contentWindow,a=b.document;a.open();a.write(&quot;&quot;);a.close();var c=&quot;callImmediate&quot;+Math.random(),d=&quot;file:&quot;==b.location.protocol?&quot;*&quot;:b.location.protocol+&quot;//&quot;+b.location.host,a=q(function(a){if((&quot;*&quot;==d||a.origin==d)&amp;&amp;a.data==c)this.port1.onmessage()},this);b.addEventListener(&quot;message&quot;,a,!1);this.port1={};this.port2={postMessage:function(){b.postMessage(c,d)}}});if(&quot;undefined&quot;!==typeof a&amp;&amp;!v(z,&quot;Trident&quot;)&amp;&amp;!v(z,&quot;MSIE&quot;)){var b=new a,c={},d=c;b.port1.onmessage=function(){if(void 0!==c.next){c=c.next;var a=c.Sa;c.Sa=null;a()}};return function(a){d.next={Sa:a};d=d.next;b.port2.postMessage(0)}}return&quot;undefined&quot;!==typeof document&amp;&amp;&quot;onreadystatechange&quot;in document.createElement(&quot;script&quot;)?function(a){var b=document.createElement(&quot;script&quot;);b.onreadystatechange=function(){b.onreadystatechange=null;b.parentNode.removeChild(b);b=null;a();a=null};document.documentElement.appendChild(b)}:function(a){k.setTimeout(a,0)}};var sb=function(a,b){nb||ob();pb||(nb(),pb=!0);qb.push(new rb(a,b))},nb,ob=function(){if(k.Promise&amp;&amp;k.Promise.resolve){var a=k.Promise.resolve();nb=function(){a.then(tb)}}else nb=function(){var a=tb;!p(k.setImmediate)||k.Window&amp;&amp;k.Window.prototype.setImmediate==k.setImmediate?(kb||(kb=lb()),kb(a)):k.setImmediate(a)}},pb=!1,qb=[],tb=function(){for(;qb.length;){var a=qb;qb=[];for(var b=0;b<a.length;b++){var c=a[b];try{c.qb.call(c.scope)}catch(d){jb(d)}}}pb=!1},rb=function(a,b){this.qb=a;this.scope=b};var K=function(a,b){this.C=0;this.Fa=void 0;this.D=this.Ha=null;this.ba=this.sa=!1;try{var c=this;a.call(b,function(a){ub(c,2,a)},function(a){ub(c,3,a)})}catch(d){ub(this,3,d)}},vb=function(a){return new K(function(b,c){a.length||b(void 0);for(var d=0,e;e=a[d];d++)e.then(b,c)})},wb=function(a){return new K(function(b,c){var d=a.length,e=[];if(d)for(var f=function(a,c){d--;e[a]=c;0==d&amp;&amp;b(e)},g=function(a){c(a)},l=0,n;n=a[l];l++)n.then(ea(f,l),g);else b(e)})};K.prototype.then=function(a,b,c){return xb(this,p(a)?a:null,p(b)?b:null,c)};K.prototype.then=K.prototype.then;K.prototype.$goog_Thenable=!0;var zb=function(a,b){a.D&amp;&amp;a.D.length||2!=a.C&amp;&amp;3!=a.C||yb(a);a.D||(a.D=[]);a.D.push(b)},xb=function(a,b,c,d){var e={da:null,Ia:null,Ja:null};e.da=new K(function(a,g){e.Ia=b?function(c){try{var e=b.call(d,c);a(e)}catch(t){g(t)}}:a;e.Ja=c?function(b){try{var e=c.call(d,b);a(e)}catch(t){g(t)}}:g});e.da.Ha=a;zb(a,e);return e.da};K.prototype.La=function(a){this.C=0;ub(this,2,a)};K.prototype.Ma=function(a){this.C=0;ub(this,3,a)};var ub=function(a,b,c){if(0==a.C){if(a==c)b=3,c=new TypeError(&quot;Promise cannot resolve to itself&quot;);else{var d;if(c)try{d=!!c.$goog_Thenable}catch(e){d=!1}else d=!1;if(d){a.C=1;c.then(a.La,a.Ma,a);return}d=typeof c;if(&quot;object&quot;==d&amp;&amp;null!=c||&quot;function&quot;==d)try{var f=c.then;if(p(f)){Ab(a,c,f);return}}catch(g){b=3,c=g}}a.Fa=c;a.C=b;yb(a);3!=b||Bb(a,c)}},Ab=function(a,b,c){a.C=1;var d=!1,e=function(b){d||(d=!0,a.La(b))},f=function(b){d||(d=!0,a.Ma(b))};try{c.call(b,e,f)}catch(g){f(g)}},yb=function(a){a.sa||(a.sa=!0,sb(a.bb,a))};K.prototype.bb=function(){for(;this.D&amp;&amp;this.D.length;){var a=this.D;this.D=[];for(var b=0;b<a.length;b++){var c=a[b],d=this.Fa;if(2==this.C)c.Ia(d);else{if(c.da)for(var e=void 0,e=this;e&amp;&amp;e.ba;e=e.Ha)e.ba=!1;c.Ja(d)}}}this.sa=!1};var Bb=function(a,b){a.ba=!0;sb(function(){a.ba&amp;&amp;Cb.call(null,b)})},Cb=jb;xa(&quot;area base br col command embed hr img input keygen link meta param source track wbr&quot;.split(&quot; &quot;));xa(&quot;action&quot;,&quot;cite&quot;,&quot;data&quot;,&quot;formaction&quot;,&quot;href&quot;,&quot;manifest&quot;,&quot;poster&quot;,&quot;src&quot;);xa(&quot;embed&quot;,&quot;iframe&quot;,&quot;link&quot;,&quot;object&quot;,&quot;script&quot;,&quot;style&quot;,&quot;template&quot;);!B&amp;&amp;!A||A&amp;&amp;A&amp;&amp;9<=Ga||B&amp;&amp;D(&quot;1.9.1&quot;);A&amp;&amp;D(&quot;9&quot;);var Db=function(a,b,c){var d=document;c=c||d;var e=a&amp;&amp;&quot;*&quot;!=a?a.toUpperCase():&quot;&quot;;if(c.querySelectorAll&amp;&amp;c.querySelector&amp;&amp;(e||b))return c.querySelectorAll(e+(b?&quot;.&quot;+b:&quot;&quot;));if(b&amp;&amp;c.getElementsByClassName){a=c.getElementsByClassName(b);if(e){c={};for(var f=d=0,g;g=a[f];f++)e==g.nodeName&amp;&amp;(c[d++]=g);c.length=d;return c}return a}a=c.getElementsByTagName(e||&quot;*&quot;);if(b){c={};for(f=d=0;g=a[f];f++){var e=g.className,l;if(l=&quot;function&quot;==typeof e.split)l=0<=pa(e.split(/\s+/),b);l&amp;&amp;(c[d++]=g)}c.length=d;return c}return a};var Eb=function(a,b,c){var d=&quot;mouseenter_custom&quot;==b,e=L(b);return function(f){f||(f=window.event);if(f.type==e){if(&quot;mouseenter_custom&quot;==b||&quot;mouseleave_custom&quot;==b){var g;if(g=d?f.relatedTarget||f.fromElement:f.relatedTarget||f.toElement)for(var l=0;l<a.length;l++){var n;n=a[l];var t=g;if(n.contains&amp;&amp;1==t.nodeType)n=n==t||n.contains(t);else if(&quot;undefined&quot;!=typeof n.compareDocumentPosition)n=n==t||Boolean(n.compareDocumentPosition(t)&amp;16);else{for(;t&amp;&amp;n!=t;)t=t.parentNode;n=t==n}if(n)return}}c(f)}}},L=function(a){return&quot;mouseenter_custom&quot;==a?&quot;mouseover&quot;:&quot;mouseleave_custom&quot;==a?&quot;mouseout&quot;:a};var Fb=function(a,b,c,d,e){if(e)c=a+(&quot;&amp;&quot;+b+&quot;=&quot;+c);else{var f=&quot;&amp;&quot;+b+&quot;=&quot;,g=a.indexOf(f);0>g?c=a+f+c:(g+=f.length,f=a.indexOf(&quot;&amp;&quot;,g),c=0<=f?a.substring(0,g)+c+a.substring(f):a.substring(0,g)+c)}return 2E3<c.length?void 0!==d?Fb(a,b,d,void 0,e):a:c};var Gb=&quot;StopIteration&quot;in k?k.StopIteration:Error(&quot;StopIteration&quot;),Hb=function(){};Hb.prototype.next=function(){throw Gb;};Hb.prototype.ob=function(){return this};var M=function(a,b){this.t={};this.l=[];this.$=this.k=0;var c=arguments.length;if(1<c){if(c%2)throw Error(&quot;Uneven number of arguments&quot;);for(var d=0;d<c;d+=2)this.set(arguments[d],arguments[d+1])}else if(a){var e;if(a instanceof M)e=a.S(),d=a.L();else{var c=[],f=0;for(e in a)c[f++]=e;e=c;c=[];f=0;for(d in a)c[f++]=a[d];d=c}for(c=0;c<e.length;c++)this.set(e[c],d[c])}};M.prototype.L=function(){Ib(this);for(var a=[],b=0;b<this.l.length;b++)a.push(this.t[this.l[b]]);return a};M.prototype.S=function(){Ib(this);return this.l.concat()};M.prototype.T=function(a){return N(this.t,a)};M.prototype.remove=function(a){return N(this.t,a)?(delete this.t[a],this.k--,this.$++,this.l.length>2*this.k&amp;&amp;Ib(this),!0):!1};var Ib=function(a){if(a.k!=a.l.length){for(var b=0,c=0;b<a.l.length;){var d=a.l[b];N(a.t,d)&amp;&amp;(a.l[c++]=d);b++}a.l.length=c}if(a.k!=a.l.length){for(var e={},c=b=0;b<a.l.length;)d=a.l[b],N(e,d)||(a.l[c++]=d,e[d]=1),b++;a.l.length=c}};h=M.prototype;h.get=function(a,b){return N(this.t,a)?this.t[a]:b};h.set=function(a,b){N(this.t,a)||(this.k++,this.l.push(a),this.$++);this.t[a]=b};h.forEach=function(a,b){for(var c=this.S(),d=0;d<c.length;d++){var e=c[d],f=this.get(e);a.call(b,f,e,this)}};h.clone=function(){return new M(this)};h.ob=function(a){Ib(this);var b=0,c=this.l,d=this.t,e=this.$,f=this,g=new Hb;g.next=function(){for(;;){if(e!=f.$)throw Error(&quot;The map has changed since the iterator was created&quot;);if(b>=c.length)throw Gb;var g=c[b++];return a?g:d[g]}};return g};var N=function(a,b){return Object.prototype.hasOwnProperty.call(a,b)};var Jb=/^(?:([^:/?#.]+):)?(?:\/\/(?:([^/?#]*)@)?([^/#?]*?)(?::([0-9]+))?(?=[/#?]|$))?([^?#]+)?(?:\?([^#]*))?(?:#(.*))?$/,Lb=function(a){if(Kb){Kb=!1;var b=k.location;if(b){var c=b.href;if(c&amp;&amp;(c=(c=Lb(c)[3]||null)?decodeURI(c):c)&amp;&amp;c!=b.hostname)throw Kb=!0,Error();}}return a.match(Jb)},Kb=C;var Mb=function(a,b){var c;if(a instanceof Mb)this.m=void 0!==b?b:a.m,Nb(this,a.F),c=a.J,O(this),this.J=c,Ob(this,a.H),Pb(this,a.N),c=a.s,O(this),this.s=c,Qb(this,a.w.clone()),c=a.I,O(this),this.I=c;else if(a&amp;&amp;(c=Lb(String(a)))){this.m=!!b;Nb(this,c[1]||&quot;&quot;,!0);var d=c[2]||&quot;&quot;;O(this);this.J=P(d);Ob(this,c[3]||&quot;&quot;,!0);Pb(this,c[4]);d=c[5]||&quot;&quot;;O(this);this.s=P(d,!0);Qb(this,c[6]||&quot;&quot;,!0);c=c[7]||&quot;&quot;;O(this);this.I=P(c)}else this.m=!!b,this.w=new Q(null,0,this.m)};h=Mb.prototype;h.F=&quot;&quot;;h.J=&quot;&quot;;h.H=&quot;&quot;;h.N=null;h.s=&quot;&quot;;h.I=&quot;&quot;;h.rb=!1;h.m=!1;h.toString=function(){var a=[],b=this.F;b&amp;&amp;a.push(Rb(b,Sb,!0),&quot;:&quot;);if(b=this.H){a.push(&quot;//&quot;);var c=this.J;c&amp;&amp;a.push(Rb(c,Sb,!0),&quot;@&quot;);a.push(encodeURIComponent(String(b)).replace(/%25([0-9a-fA-F]{2})/g,&quot;%$1&quot;));b=this.N;null!=b&amp;&amp;a.push(&quot;:&quot;,String(b))}if(b=this.s)this.H&amp;&amp;&quot;/&quot;!=b.charAt(0)&amp;&amp;a.push(&quot;/&quot;),a.push(Rb(b,&quot;/&quot;==b.charAt(0)?Tb:Ub,!0));(b=this.w.toString())&amp;&amp;a.push(&quot;?&quot;,b);(b=this.I)&amp;&amp;a.push(&quot;#&quot;,Rb(b,Vb));return a.join(&quot;&quot;)};h.resolve=function(a){var b=this.clone(),c=!!a.F;c?Nb(b,a.F):c=!!a.J;if(c){var d=a.J;O(b);b.J=d}else c=!!a.H;c?Ob(b,a.H):c=null!=a.N;d=a.s;if(c)Pb(b,a.N);else if(c=!!a.s){if(&quot;/&quot;!=d.charAt(0))if(this.H&amp;&amp;!this.s)d=&quot;/&quot;+d;else{var e=b.s.lastIndexOf(&quot;/&quot;);-1!=e&amp;&amp;(d=b.s.substr(0,e+1)+d)}e=d;if(&quot;..&quot;==e||&quot;.&quot;==e)d=&quot;&quot;;else if(v(e,&quot;./&quot;)||v(e,&quot;/.&quot;)){for(var d=0==e.lastIndexOf(&quot;/&quot;,0),e=e.split(&quot;/&quot;),f=[],g=0;g<e.length;){var l=e[g++];&quot;.&quot;==l?d&amp;&amp;g==e.length&amp;&amp;f.push(&quot;&quot;):&quot;..&quot;==l?((1<f.length||1==f.length&amp;&amp;&quot;&quot;!=f[0])&amp;&amp;f.pop(),d&amp;&amp;g==e.length&amp;&amp;f.push(&quot;&quot;)):(f.push(l),d=!0)}d=f.join(&quot;/&quot;)}else d=e}c?(O(b),b.s=d):c=&quot;&quot;!==a.w.toString();c?Qb(b,P(a.w.toString())):c=!!a.I;c&amp;&amp;(a=a.I,O(b),b.I=a);return b};h.clone=function(){return new Mb(this)};var Nb=function(a,b,c){O(a);a.F=c?P(b,!0):b;a.F&amp;&amp;(a.F=a.F.replace(/:$/,&quot;&quot;))},Ob=function(a,b,c){O(a);a.H=c?P(b,!0):b},Pb=function(a,b){O(a);if(b){b=Number(b);if(isNaN(b)||0>b)throw Error(&quot;Bad port number &quot;+b);a.N=b}else a.N=null},Qb=function(a,b,c){O(a);b instanceof Q?(a.w=b,a.w.ua(a.m)):(c||(b=Rb(b,Wb)),a.w=new Q(b,0,a.m))},O=function(a){if(a.rb)throw Error(&quot;Tried to modify a read-only Uri&quot;);};Mb.prototype.ua=function(a){this.m=a;this.w&amp;&amp;this.w.ua(a);return this};var P=function(a,b){return a?b?decodeURI(a):decodeURIComponent(a):&quot;&quot;},Rb=function(a,b,c){return m(a)?(a=encodeURI(a).replace(b,Xb),c&amp;&amp;(a=a.replace(/%25([0-9a-fA-F]{2})/g,&quot;%$1&quot;)),a):null},Xb=function(a){a=a.charCodeAt(0);return&quot;%&quot;+(a>>4&amp;15).toString(16)+(a&amp;15).toString(16)},Sb=/[#\/\?@]/g,Ub=/[\#\?:]/g,Tb=/[\#\?]/g,Wb=/[\#\?@]/g,Vb=/#/g,Q=function(a,b,c){this.n=a||null;this.m=!!c},R=function(a){if(!a.j&amp;&amp;(a.j=new M,a.k=0,a.n)){var b=q(a.add,a);a=a.n.split(&quot;&amp;&quot;);for(var c=0;c<a.length;c++){var d=a[c].indexOf(&quot;=&quot;),e=null,f=null;0<=d?(e=a[c].substring(0,d),f=a[c].substring(d+1)):e=a[c];b(decodeURIComponent(e.replace(/\+/g,&quot; &quot;)),f?decodeURIComponent(f.replace(/\+/g,&quot; &quot;)):&quot;&quot;)}}};h=Q.prototype;h.j=null;h.k=null;h.add=function(a,b){R(this);this.n=null;a=S(this,a);var c=this.j.get(a);c||this.j.set(a,c=[]);c.push(b);this.k++;return this};h.remove=function(a){R(this);a=S(this,a);return this.j.T(a)?(this.n=null,this.k-=this.j.get(a).length,this.j.remove(a)):!1};h.T=function(a){R(this);a=S(this,a);return this.j.T(a)};h.S=function(){R(this);for(var a=this.j.L(),b=this.j.S(),c=[],d=0;d<b.length;d++)for(var e=a[d],f=0;f<e.length;f++)c.push(b[d]);return c};h.L=function(a){R(this);var b=[];if(m(a))this.T(a)&amp;&amp;(b=ra(b,this.j.get(S(this,a))));else{a=this.j.L();for(var c=0;c<a.length;c++)b=ra(b,a[c])}return b};h.set=function(a,b){R(this);this.n=null;a=S(this,a);this.T(a)&amp;&amp;(this.k-=this.j.get(a).length);this.j.set(a,[b]);this.k++;return this};h.get=function(a,b){var c=a?this.L(a):[];return 0<c.length?String(c[0]):b};h.toString=function(){if(this.n)return this.n;if(!this.j)return&quot;&quot;;for(var a=[],b=this.j.S(),c=0;c<b.length;c++)for(var d=b[c],e=encodeURIComponent(String(d)),d=this.L(d),f=0;f<d.length;f++){var g=e;&quot;&quot;!==d[f]&amp;&amp;(g+=&quot;=&quot;+encodeURIComponent(String(d[f])));a.push(g)}return this.n=a.join(&quot;&amp;&quot;)};h.clone=function(){var a=new Q;a.n=this.n;this.j&amp;&amp;(a.j=this.j.clone(),a.k=this.k);return a};var S=function(a,b){var c=String(b);a.m&amp;&amp;(c=c.toLowerCase());return c};Q.prototype.ua=function(a){a&amp;&amp;!this.m&amp;&amp;(R(this),this.n=null,this.j.forEach(function(a,c){var d=c.toLowerCase();c!=d&amp;&amp;(this.remove(c),this.remove(d),0<a.length&amp;&amp;(this.n=null,this.j.set(S(this,d),sa(a)),this.k+=a.length))},this));this.m=a};var Yb;Yb=!1;var T=z;T&amp;&amp;(-1!=T.indexOf(&quot;Firefox&quot;)||-1!=T.indexOf(&quot;Camino&quot;)||-1!=T.indexOf(&quot;iPad&quot;)||-1!=T.indexOf(&quot;iPhone&quot;)||-1!=T.indexOf(&quot;iPod&quot;)||-1!=T.indexOf(&quot;Chrome&quot;)||-1!=T.indexOf(&quot;Android&quot;)&amp;&amp;(Yb=!0));var Zb=Yb;var U={tb:0,la:1,URL:2,ja:3,fa:4,Ba:5,Aa:7,za:8,ya:9,ka:6,ib:10,kb:11,jb:12,gb:13,xa:14,Ra:15,lb:16,nb:17,eb:18,fb:19,ub:1E3};var $b=function(a,b,c,d){b=c(d,b);if(!(b instanceof Array))return a;qa(b,function(b){if(2!==b.length&amp;&amp;3!==b.length)return a;a=Fb(a,b[0],b[1],b[2],!0)});return a},ac=function(a,b,c){if(window.ona){ib(a);a=b.href;i:{if(window.ona){if(c.match(/itunes[.]apple[.]com/)){if(window.onc)window.onc(a),window.ona(c);else window.ona(a);c=!0;break i}c=a;if(c.match(/market[.]android[.]com|play[.]google[.]com/)&amp;&amp;c.match(/[\?&amp;]sa=L/)&amp;&amp;!c.match(/googleadservices[.]com/)){var d=window.location.host;if(d){b=1;for(var e=d.split(&quot;:&quot;),d=[];0<b&amp;&amp;e.length;)d.push(e.shift()),b--;e.length&amp;&amp;d.push(e.join(&quot;:&quot;));b=d[0];d=d[1];c=new Mb(c);Ob(c,b);Pb(c,d);c=c.toString()}c=c.replace(&quot;?&quot;,&quot;?&quot;+encodeURIComponent(&quot;rct&quot;)+&quot;=&quot;+encodeURIComponent(&quot;j&quot;)+&quot;&amp;&quot;);b=new XMLHttpRequest;b.open(&quot;GET&quot;,c,!1);b.send();b.responseText&amp;&amp;(b=b.responseText.match(/URL=\'([^\']*)\'/),1<b.length&amp;&amp;(c=b[1].replace(/&amp;amp;/g,&quot;&amp;&quot;)));c=Zb||Ba?c.replace(/https?:\/\/(market.android.com|play.google.com\/store\/apps)\//,&quot;market://&quot;):c}else c=null;if(c){window.ona(c);c=!0;break i}}c=!1}if(!c)window.ona(a)}};var V=function(a){this.ma=a;this.pa=[];this.W=[];this.na={};this.i={};this.Ca=1;this.O=&quot;data-original-click-url&quot;;this.qa=&quot;data-landing-url&quot;;this.A={};this.ra=!1;this.V=[]};V.prototype.registerBeaconUrlBuilder=function(a){this.W.push(a)};var bc=function(a,b,c){var d=b=b.getAttribute(a.O);if(d)for(var e=0;e<a.pa.length;e++)d=$b(d,b,a.pa[e],c);return d},cc=function(a,b,c,d){if(0!=a.W.length&amp;&amp;(d.preventDefault?!d.defaultPrevented:!1!==d.returnValue)){ib(d);for(var e=[],f=0;f<a.W.length;f++){var g=a.W[f](c);if(g){var l=new K(function(a){eb(g,a)});e.push(l)}}c=wb(e);e=new K(function(a){window.setTimeout(a,2E3)});vb([c,e]).then(q(V.prototype.ab,a,b,d))}};V.prototype.ab=function(a,b){this.ra=!0;var c=!1;b.target&amp;&amp;(c=gb(b.target,&quot;click&quot;,b.button,b.ctrlKey,b.shiftKey,b.metaKey));a.href&amp;&amp;!c&amp;&amp;(fb.top.location=a.href)};V.prototype.Ta=function(a,b,c,d){if(this.ra)this.ra=!1;else{d||(d=window.event);ua(this.i[c][b],function(a){a(d)});var e=bc(this,a,d.type);e&amp;&amp;(this.A[b]?a.ping=e:a.href=e);&quot;click&quot;==c&amp;&amp;cc(this,a,b,d);dc(this);&quot;click&quot;!=c||(d.preventDefault?d.defaultPrevented:!1===d.returnValue)||ac(d,a,oa(this.ma))}};var ec=function(a,b,c,d){a.i[d]||(a.i[d]={});a.i[d][c]||(a.i[d][c]={});a=q(a.Ta,a,b,c,d);cb(b,d,a,void 0)};h=V.prototype;h.U=function(a,b){for(var c=0;c<a.length;c++){var d=a[c];d.setAttribute(this.O,d.href);ec(this,d,b,&quot;mousedown&quot;);ec(this,d,b,&quot;click&quot;)}this.na[b]=!0};h.usePingClickTracking=function(a,b){this.A[b]=!0;for(var c=0;c<a.length;c++){var d=a[c];d.ping&amp;&amp;(d.setAttribute(this.O,d.ping),d.setAttribute(this.qa,d.href))}};h.disablePingClickTracking=function(a,b){if(!(b in this.A)){this.A[b]=!1;for(var c=0;c<a.length;c++){var d=a[c];d.ping&amp;&amp;(d.setAttribute(this.O,d.ping),d.href=d.ping,d.removeAttribute(&quot;ping&quot;))}}};h.suspendPingClickTracking=function(a,b){if(this.A[b]){this.A[b]=!1;for(var c=0;c<a.length;c++){var d=a[c];d.getAttribute(this.qa)&amp;&amp;(d.href=d.getAttribute(this.O),d.removeAttribute(&quot;ping&quot;))}}};h.restorePingClickTracking=function(a,b){if(b in this.A&amp;&amp;!this.A[b]){this.A[b]=!0;for(var c=0;c<a.length;c++){var d=a[c],e=d.getAttribute(this.qa);e&amp;&amp;(d.ping=d.getAttribute(this.O),d.href=e)}}};h.queueOnObjectAfterClickModifiers=function(a,b,c,d){this.V.push({Va:a,va:b,Xa:c,Wa:d})};var dc=function(a){for(var b=0;b<a.V.length;b++){var c=a.V[b],d=c.Va,e=c.va,f=c.Xa;c.Wa&amp;&amp;(f.preventDefault?f.defaultPrevented:!1===f.returnValue)||d.fireOnObject(e,f)}a.V=[]};var fc=&quot;undefined&quot;!=typeof DOMTokenList,gc=function(a,b){if(fc){var c=a.classList;0==c.contains(b)&amp;&amp;c.toggle(b)}else if(c=a.className){for(var c=c.split(/\s+/),d=!1,e=0;e<c.length&amp;&amp;!d;++e)d=c[e]==b;d||(c.push(b),a.className=c.join(&quot; &quot;))}else a.className=b},hc=function(a,b){if(fc){var c=a.classList;1==c.contains(b)&amp;&amp;c.toggle(b)}else if((c=a.className)&amp;&amp;!(0>c.indexOf(b))){for(var c=c.split(/\s+/),d=0;d<c.length;++d)c[d]==b&amp;&amp;c.splice(d--,1);a.className=c.join(&quot; &quot;)}};var W=function(a,b,c){this.ta=new I;this.h=a;this.h[0]=[b];this.Ea=[];this.R=b.style.display;this.p=new V(c);this.ma=c};h=W.prototype;h.navigationAdPieces=function(){return this.Ea};h.Ka=function(){return!0};h.hide=function(){for(var a=this.h[0],b=0;b<a.length;b++)a[b].style.display=&quot;none&quot;};h.reset=function(){for(var a=this.h[0],b=0;b<a.length;b++)a[b].style.display=this.R};h.has=function(a){return(a=this.h[a])&amp;&amp;0<a.length};h.listen=function(a,b,c){var d=this.h[a];if(d){var e=this.p,f=L(b),g=(&quot;click&quot;==b||&quot;mousedown&quot;==b)&amp;&amp;e.na[a],l=Eb(d,b,ea(c,a,this));e.i[f]||(e.i[f]={});e.i[f][a]||(e.i[f][a]={});var n=e.Ca;e.i[f][a][n]=l;e.Ca=n+1;if(!g)for(e=0;e<d.length;e++)cb(d[e],f,l,void 0);c.B||(c.B={});c.B[b]||(c.B[b]={});c.B[b][a]=n}};h.unlisten=function(a,b,c){var d;if(c.B&amp;&amp;c.B[b]&amp;&amp;c.B[b][a]){var e=c.B[b][a];delete c.B[b][a];d=e}else d=-1;if(c=this.h[a]){var f=this.p,e=L(b);b=(&quot;click&quot;==b||&quot;mousedown&quot;==b)&amp;&amp;f.na[a];if(f.i[e]&amp;&amp;f.i[e][a]){var g=f.i[e][a][d];delete f.i[e][a][d];a=g}else a=null;if(a&amp;&amp;!b)for(b=0;b<c.length;b++)db(c[b],e,a,void 0)}};h.dispatchMouseEvent=function(a,b,c,d,e,f){if(a=this.h[a])for(var g=0;g<a.length;g++){var l=b,l=L(l);gb(a[g],l,c,d,e,f)}};h.registerClickUrlModifier=function(a){this.p.pa.push(a)};h.registerBeaconUrlBuilder=function(a){this.p.registerBeaconUrlBuilder(a)};h.modifyCssClass=function(a,b,c){if(b&amp;&amp;(a=this.h[a]))for(var d=0;d<a.length;d++)(c?hc:gc)(a[d],b)};h.getAttribute=function(a,b){var c=this.h[a];if(c&amp;&amp;b)for(var d=0;d<c.length;d++){var e=c[d].getAttribute(b);if(e)return e}return null};h.setAttribute=function(a,b,c){(a=this.h[a])&amp;&amp;0<a.length&amp;&amp;b&amp;&amp;a[0].setAttribute(b,c)};h.removeAttribute=function(a,b){var c=this.h[a];c&amp;&amp;0<c.length&amp;&amp;b&amp;&amp;c[0].removeAttribute(b)};h.addScroller=function(a,b){var c=this.h[a];if(window.CreateScrollerForElement)for(var d=0;d<c.length;d++){var e=c[d];if(e)for(var d=b,f=e||document,e=f.querySelectorAll&amp;&amp;f.querySelector?f.querySelectorAll(&quot;.&quot;+d):Db(&quot;*&quot;,d,e),d=0;d<e.length;d++)window.CreateScrollerForElement(e[d],!1,!0,!0)}};h.getBoundingClientRect=function(a){return(a=this.h[a])?a[0].getBoundingClientRect():null};h.forEachAdPiece=function(a){var b=this.h;ua(U,function(c){b[c]&amp;&amp;0<b[c].length&amp;&amp;a(c)})};h.U=function(a){this.h[a]&amp;&amp;this.Ka(a)&amp;&amp;(this.Ea.push(a),this.p.U(this.h[a],a))};h.usePingClickTracking=function(a){this.h[a]&amp;&amp;this.p.usePingClickTracking(this.h[a],a)};h.disablePingClickTracking=function(a){this.h[a]&amp;&amp;this.p.disablePingClickTracking(this.h[a],a)};h.suspendPingClickTracking=function(a){this.h[a]&amp;&amp;this.p.suspendPingClickTracking(this.h[a],a)};h.restorePingClickTracking=function(a){this.h[a]&amp;&amp;this.p.restorePingClickTracking(this.h[a],a)};h.hasHref=function(a){a=this.h[a];if(!a)return!1;for(var b=0;b<a.length;b++)if(!a[b].href)return!1;return!0};h.creativeConversionUrl=function(){var a=this.ma.g[5];return null!=a?a:&quot;&quot;};h.listenOnObject=function(a,b){Sa(this.ta,a,b)};h.unlistenOnObject=function(a,b){Ya(this.ta,a,b)};h.fireOnObject=function(a,b){var c=this.ta;c&amp;&amp;c[G]?J(c,a,!1,b):ab(c,a,!1,b)};h.queueOnObjectAfterClickModifiers=function(a,b,c){this.p.queueOnObjectAfterClickModifiers(this,a,b,c)};W.prototype.modifyCssClass=W.prototype.modifyCssClass;W.prototype.has=W.prototype.has;W.prototype.listen=W.prototype.listen;W.prototype.unlisten=W.prototype.unlisten;W.prototype.dispatchMouseEvent=W.prototype.dispatchMouseEvent;W.prototype.registerClickUrlModifier=W.prototype.registerClickUrlModifier;W.prototype.usePingClickTracking=W.prototype.usePingClickTracking;W.prototype.disablePingClickTracking=W.prototype.disablePingClickTracking;W.prototype.suspendPingClickTracking=W.prototype.suspendPingClickTracking;W.prototype.restorePingClickTracking=W.prototype.restorePingClickTracking;W.prototype.registerBeaconUrlBuilder=W.prototype.registerBeaconUrlBuilder;W.prototype.hide=W.prototype.hide;W.prototype.reset=W.prototype.reset;W.prototype.forEachAdPiece=W.prototype.forEachAdPiece;W.prototype.getAttribute=W.prototype.getAttribute;W.prototype.setAttribute=W.prototype.setAttribute;W.prototype.removeAttribute=W.prototype.removeAttribute;W.prototype.getBoundingClientRect=W.prototype.getBoundingClientRect;W.prototype.addScroller=W.prototype.addScroller;W.prototype.hasHref=W.prototype.hasHref;W.prototype.creativeConversionUrl=W.prototype.creativeConversionUrl;W.prototype.listenOnObject=W.prototype.listenOnObject;W.prototype.unlistenOnObject=W.prototype.unlistenOnObject;W.prototype.fireOnObject=W.prototype.fireOnObject;W.prototype.navigationAdPieces=W.prototype.navigationAdPieces;W.prototype.queueOnObjectAfterClickModifiers=W.prototype.queueOnObjectAfterClickModifiers;var jc=function(a,b,c){W.call(this,a,b,c);for(a=0;a<ic.length;a++)this.U(ic[a]);this.listen(4,&quot;mouseover&quot;,q(this.modifyCssClass,this,0,&quot;onhoverbg&quot;,!1));this.listen(4,&quot;mouseout&quot;,q(this.modifyCssClass,this,0,&quot;onhoverbg&quot;,!0))};u(jc,W);var ic=[U.la,U.URL,U.fa,U.Ba,U.Aa,U.za,U.ja,U.ya,U.ka,U.xa,U.Ra],kc={la:&quot;rhtitle&quot;,ja:&quot;rhbody&quot;,URL:&quot;rhurl&quot;,fa:&quot;rhbutton&quot;,za:&quot;rhfavicon&quot;,xa:&quot;rhaddress&quot;,ka:&quot;rhimage&quot;,lb:&quot;rhimagegallery&quot;,ib:&quot;rhimage-container&quot;,kb:&quot;rhexpand-button&quot;,jb:&quot;rhimage-collapsed&quot;,ya:&quot;rhbackground&quot;,gb:&quot;rh-icore-empty&quot;,Ba:&quot;rhsitelink&quot;,Aa:&quot;rhradlink&quot;,nb:&quot;rh-multiframe&quot;,eb:&quot;rh-box-breadcrumbs&quot;};jc.prototype.Ka=function(a){return this.hasHref(a)||4==a||6==a};r(&quot;buildRhTextAd&quot;,function(a){a=new ma(a);var b=a.g[1],c;var d={};if(b=document.getElementById(&quot;taw&quot;+(null!=b?b:0))){d[0]=[b];for(c in kc){var e=U[c],f=d,g=Db(null,kc[c],b);f[e]=[];for(var l=0;l<g.length;l++)f[e].push(g[l])}c=new jc(d,b,a)}else c=null;return c});var Z=function(a,b,c){I.call(this);this.u=a;this.R=&quot;none&quot;;this.u&amp;&amp;(this.R=this.u.style.display);this.v=b;this.g=c;this.i={};this.oa=[];this.Da=!1;this.q=[]};u(Z,I);h=Z.prototype;h.forEachAd=function(a){qa(this.v,a)};h.addAd=function(a){this.v.push(a)};h.pb=function(a){if(a=document.getElementById(a))this.u=a,this.R=this.u.style.display;if(0==this.v.length)window.css=null;else{window.SlideConstructor&amp;&amp;0<this.v.length&amp;&amp;new window.SlideConstructor(this.v[0],this,w(this.g));window.GridConstructor&amp;&amp;0<this.v.length&amp;&amp;new window.GridConstructor(this,w(this.g));window.ImageExpandConstructor&amp;&amp;1==this.v.length&amp;&amp;new window.ImageExpandConstructor(this,w(this.g));window.OneClickConstructor&amp;&amp;0<this.v.length&amp;&amp;new window.OneClickConstructor(this,0);if(window.OnePointFiveClickConstructor&amp;&amp;0<this.v.length){a=x(this.g).g[0];var b=x(this.g).g[1],c=x(this.g).g[2],d=x(this.g).g[4],e=x(this.g).g[3];new window.OnePointFiveClickConstructor(this,null!=a?a:!1,null!=b?b:!1,null!=c?c:!1,null!=e?e:0,null!=d?d:!1)}window.MultiframeConstructor&amp;&amp;new window.MultiframeConstructor(this,w(this.g));if(a=window.ona)a=this.g.g[4],a=!(null!=a&amp;&amp;a);a&amp;&amp;(window.ona=null);for(a=0;a<this.oa.length;++a)this.oa[a]();this.Da=!0}};h.listenOnContainer=function(a,b){var c=Eb([this.u],a,ea(b,this));cb(this.u,L(a),c,void 0);this.i[a]||(this.i[a]={});this.i[a][b]=c};h.unlistenOnContainer=function(a,b){var c;this.i[a]&amp;&amp;this.i[a][b]?(c=this.i[a][b],delete this.i[a][b]):c=null;c&amp;&amp;db(this.u,L(a),c,void 0)};h.listenOnObject=function(a,b){Sa(this,a,b)};h.unlistenOnObject=function(a,b){Ya(this,a,b)};h.fireOnObject=function(a,b){b.vb=this;this&amp;&amp;this[G]?J(this,a,!1,b):ab(this,a,!1,b)};h.registerFinalizeCallback=function(a){this.Da?a():this.oa.push(a)};h.registerWidget=function(a,b){0<=pa(this.q,a)||(this.q[b]=a,a.reset(this))};var lc=function(a){a.u.style.display=&quot;none&quot;;for(var b=0;b<a.q.length;b++)a.q[b]&amp;&amp;a.q[b].hide(a)};Z.prototype.resetAll=function(){this.u.style.display=this.R;for(var a=0;a<this.q.length;a++)this.q[a]&amp;&amp;this.q[a].reset(this)};Z.prototype.showOnly=function(a){var b=this;lc(this);mc(this,a,function(a){a.show(b)})};var mc=function(a,b,c){a.q[b]&amp;&amp;c(a.q[b])};Z.prototype.isMobile=function(){return w(this.g)};Z.prototype.getEscapedQemQueryId=function(){return this.g.getEscapedQemQueryId()};Z.prototype.getEscapedGwsQueryId=function(){return this.g.getEscapedGwsQueryId()};Z.prototype.forEachAd=Z.prototype.forEachAd;Z.prototype.addAd=Z.prototype.addAd;Z.prototype.finalize=Z.prototype.pb;Z.prototype.registerFinalizeCallback=Z.prototype.registerFinalizeCallback;Z.prototype.listenOnContainer=Z.prototype.listenOnContainer;Z.prototype.unlistenOnContainer=Z.prototype.unlistenOnContainer;Z.prototype.registerWidget=Z.prototype.registerWidget;Z.prototype.resetAll=Z.prototype.resetAll;Z.prototype.showOnly=Z.prototype.showOnly;Z.prototype.isMobile=Z.prototype.isMobile;Z.prototype.getEscapedQemQueryId=Z.prototype.getEscapedQemQueryId;Z.prototype.getEscapedGwsQueryId=Z.prototype.getEscapedGwsQueryId;Z.prototype.listenOnObject=Z.prototype.listenOnObject;Z.prototype.unlistenOnObject=Z.prototype.unlistenOnObject;Z.prototype.fireOnObject=Z.prototype.fireOnObject;r(&quot;buildAdSlot&quot;,function(a){a=new Z(null,[],new ka(a));r(&quot;adSlot&quot;,a);return a});var nc=function(a,b,c){var d=[];d[0]=[b];d[15]=[a];W.call(this,d,b,c);this.U(15)};u(nc,W);r(&quot;buildImageAd&quot;,function(a){a=new ma(a);var b=document,c=b.getElementById(&quot;google_image_div&quot;),b=b.getElementById(&quot;aw0&quot;);return c&amp;&amp;b?new nc(b,c,a):null});var pc=function(a,b,c){W.call(this,a,b,c);for(a=0;a<oc.length;a++)this.U(oc[a])};u(pc,W);var oc=[U.la,U.URL,U.fa,U.Ba,U.Aa,U.za,U.ja,U.ya,U.ka,U.xa,U.Ra],qc={la:&quot;headline&quot;,ja:&quot;description&quot;,fa:&quot;button&quot;,fb:&quot;logo&quot;,ka:&quot;product&quot;};r(&quot;buildTemplateAd&quot;,function(a){var b;a=new ma(a);var c={},d=document.getElementById(&quot;adContent&quot;);if(d){c[0]=[d];for(b in qc){var e=U[b],f=c,g=Db(null,qc[b],d);f[e]=[];for(var l=0;l<g.length;l++)f[e].push(g[l])}b=new pc(c,d,a)}else b=null;return b});})();</script><script>buildAdSlot([null,728,90,0,0,null,&quot;CP2a8Izdk8MCFZYZvAodCyMAdQ&quot;,&quot;&quot;]);</script><script></script><script>(function(){var c=this,e=function(a,b){var f=a.split(&quot;.&quot;),d=c;f[0]in d||!d.execScript||d.execScript(&quot;var &quot;+f[0]);for(var g;f.length&amp;&amp;(g=f.shift());)f.length||void 0===b?d=d[g]?d[g]:d[g]={}:d[g]=b},h=function(a,b){var f=Array.prototype.slice.call(arguments,1);return function(){var b=f.slice();b.push.apply(b,arguments);return a.apply(this,b)}};var k=function(){this.g=[];this.h={}};k.prototype.report=function(){for(var a=[],b=0;b<this.g.length;++b)a.push(l(this.g[b]));return a};var l=function(a){var b=[a.key,a.value];void 0!==a.i&amp;&amp;b.push(a.i);return b},m={};var n=function(a,b,f,d,g){&quot;true&quot;===d.getAttribute(f,&quot;data-is-action-button-expanded&quot;)&amp;&amp;(b=12);ia(a,g,b)},p=function(a){return function(){a()}},q=function(a){return a.report()};e(&quot;registerAd&quot;,function(a,b){void 0!==m[b]||(m[b]=new k);a.registerClickUrlModifier(h(q,m[b]));a.listen(0,&quot;mouseover&quot;,p(h(ss,b)));a.listen(0,&quot;focus&quot;,p(h(ss,b)));a.listen(1,&quot;click&quot;,p(h(ha,b)));a.listen(1,&quot;focus&quot;,p(h(ss,b)));a.listen(1,&quot;mousedown&quot;,p(h(st,b)));a.listen(1,&quot;mouseover&quot;,p(h(ss,b)));a.listen(2,&quot;click&quot;,h(n,b,null));a.listen(2,&quot;mousedown&quot;,p(h(st,b)));a.listen(4,&quot;click&quot;,h(n,b,8));a.listen(4,&quot;mousedown&quot;,p(h(st,b)));a.listen(8,&quot;click&quot;,h(n,b,11));a.listen(8,&quot;mousedown&quot;,p(h(st,b)));a.listen(6,&quot;click&quot;,h(n,b,9));a.listen(6,&quot;mousedown&quot;,p(h(st,b)));a.listen(9,&quot;click&quot;,h(n,b,2));a.listen(9,&quot;mousedown&quot;,p(h(st,b)));a.listen(15,&quot;click&quot;,p(h(ha,b)));a.listen(15,&quot;mousedown&quot;,p(h(st,b)));a.listen(5,&quot;click&quot;,h(n,b,6));a.listen(5,&quot;mousedown&quot;,p(h(st,b)));return a});e(&quot;css&quot;,function(a,b,f,d,g){a=m[a];void 0!==a&amp;&amp;(void 0===a.h[b]||d?(d=a.g.length,a.h[b]=d,a.g[d]={key:b,value:f,i:g}):(b=a.g[a.h[b]],b.value=f,b.i=g))});})();(function(){var g=function(a,e,b){a.addEventListener?a.addEventListener(e,b,!1):a.attachEvent&amp;&amp;a.attachEvent(&quot;on&quot;+e,b)};var k=function(a,e){var b=h;b.google_image_requests||(b.google_image_requests=[]);var c=b.document.createElement(&quot;img&quot;);if(e){var d=function(a){e(a);a=d;c.removeEventListener?c.removeEventListener(&quot;load&quot;,a,!1):c.detachEvent&amp;&amp;c.detachEvent(&quot;onload&quot;,a);a=d;c.removeEventListener?c.removeEventListener(&quot;error&quot;,a,!1):c.detachEvent&amp;&amp;c.detachEvent(&quot;onerror&quot;,a)};g(c,&quot;load&quot;,d);g(c,&quot;error&quot;,d)}c.src=a;b.google_image_requests.push(c)};var h=window;var l=Array.prototype,m=l.forEach?function(a,e,b){l.forEach.call(a,e,b)}:function(a,e,b){for(var c=a.length,d=&quot;string&quot;==typeof a?a.split(&quot;&quot;):a,f=0;f<c;f++)f in d&amp;&amp;e.call(b,d[f],f,a)};var p=function(a){this.j=a;this.i=[6,14];this.h=[];this.g=[];this.k=&quot;data-redirect-ping&quot;;n(this)},n=function(a){a.j.forEachAd(function(e,b){a.h[b]=!1;a.g[b]=!1;m(a.i,function(c){e.listen(c,&quot;click&quot;,q(a,b))})})},r=function(a,e,b,c,d){return function(){a.g[c]||(a.g[c]=!0,b.dispatchMouseEvent(e,&quot;click&quot;,d.button,d.ctrlKey,d.shiftKey,d.metaKey))}},q=function(a,e){return function(b,c,d){if(d.preventDefault?d.defaultPrevented:!1===d.returnValue)return!1;if(a.h[e]&amp;&amp;a.g[e])return!0;if(!a.h[e]){var f=c.getAttribute(b,a.k);if(f)b=r(a,b,c,e,d),a.h[e]=!0,k(f,b),h.setTimeout(b,5E3);else return!0}d.preventDefault?d.preventDefault():d.returnValue=!1;return!1}};var t=function(a){return a?new p(a):null},u=[&quot;registerAdLocationExtensionRedirectPing&quot;],v=this;u[0]in v||!v.execScript||v.execScript(&quot;var &quot;+u[0]);for(var w;u.length&amp;&amp;(w=u.shift());){var x;if(x=!u.length)x=void 0!==t;x?v[w]=t:v=v[w]?v[w]:v[w]={}};})();(function(){var f=this,g=function(a){var b=typeof a;if(&quot;object&quot;==b)if(a){if(a instanceof Array)return&quot;array&quot;;if(a instanceof Object)return b;var d=Object.prototype.toString.call(a);if(&quot;[object Window]&quot;==d)return&quot;object&quot;;if(&quot;[object Array]&quot;==d||&quot;number&quot;==typeof a.length&amp;&amp;&quot;undefined&quot;!=typeof a.splice&amp;&amp;&quot;undefined&quot;!=typeof a.propertyIsEnumerable&amp;&amp;!a.propertyIsEnumerable(&quot;splice&quot;))return&quot;array&quot;;if(&quot;[object Function]&quot;==d||&quot;undefined&quot;!=typeof a.call&amp;&amp;&quot;undefined&quot;!=typeof a.propertyIsEnumerable&amp;&amp;!a.propertyIsEnumerable(&quot;call&quot;))return&quot;function&quot;}else return&quot;null&quot;;else if(&quot;function&quot;==b&amp;&amp;&quot;undefined&quot;==typeof a.call)return&quot;object&quot;;return b},h=function(a,b,d){return a.call.apply(a.bind,arguments)},k=function(a,b,d){if(!a)throw Error();if(2<arguments.length){var c=Array.prototype.slice.call(arguments,2);return function(){var d=Array.prototype.slice.call(arguments);Array.prototype.unshift.apply(d,c);return a.apply(b,d)}}return function(){return a.apply(b,arguments)}},l=function(a,b,d){l=Function.prototype.bind&amp;&amp;-1!=Function.prototype.bind.toString().indexOf(&quot;native code&quot;)?h:k;return l.apply(null,arguments)};var m;t:{var n=f.navigator;if(n){var p=n.userAgent;if(p){m=p;break t}}m=&quot;&quot;};var q=-1!=m.indexOf(&quot;Opera&quot;)||-1!=m.indexOf(&quot;OPR&quot;),r=-1!=m.indexOf(&quot;Trident&quot;)||-1!=m.indexOf(&quot;MSIE&quot;),t=-1!=m.indexOf(&quot;Gecko&quot;)&amp;&amp;-1==m.toLowerCase().indexOf(&quot;webkit&quot;)&amp;&amp;!(-1!=m.indexOf(&quot;Trident&quot;)||-1!=m.indexOf(&quot;MSIE&quot;)),u=-1!=m.toLowerCase().indexOf(&quot;webkit&quot;);(function(){var a=&quot;&quot;,b;if(q&amp;&amp;f.opera)return a=f.opera.version,&quot;function&quot;==g(a)?a():a;t?b=/rv\:([^\);]+)(\)|;)/:r?b=/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/:u&amp;&amp;(b=/WebKit\/(\S+)/);b&amp;&amp;(a=(a=b.exec(m))?a[1]:&quot;&quot;);return r&amp;&amp;(b=(b=f.document)?b.documentMode:void 0,b>parseFloat(a))?String(b):a})();var v=function(a,b){this.t=a;this.s=b;this.n=this.m=this.p=this.o=0;this.h=null;this.i=this.j=!1;this.t.forEachAd(l(this.u,this))},w=function(a,b){this.k=a;this.index=0;this.q=b;this.g=&quot;fade&quot;==b||&quot;slide&quot;==b};v.prototype.w=function(a,b,d,c){if(&quot;touchstart&quot;==c.type)c.touches&amp;&amp;0<c.touches.length&amp;&amp;(this.o=c.touches[0].pageX,this.p=c.touches[0].pageY,this.j=!0);else if(&quot;touchmove&quot;==c.type)c.touches&amp;&amp;0<c.touches.length&amp;&amp;(this.m=c.touches[0].pageX,this.n=c.touches[0].pageY,this.i=!0);else if(&quot;touchend&quot;==c.type||&quot;touchcancel&quot;==c.type){if(this.j&amp;&amp;(this.i||a.g)){b=(a.g?c.changedTouches[0].pageX:this.m)-this.o;c=(a.g?c.changedTouches[0].pageY:this.n)-this.p;var e=0;100<b*b+c*c&amp;&amp;(e=Math.abs(b)>Math.abs(c)?0>b?1:-1:0>c?1:-1);0!=e&amp;&amp;(e=a.index+e,-1==e?e=a.k-1:e==a.k&amp;&amp;(e=0),&quot;slide&quot;==a.q?Math.abs(b)>Math.abs(c)&amp;&amp;x(this,a,d,e,0<b):x(this,a,d,e,0<b))}this.i=this.j=!1}};v.prototype.v=function(a,b,d,c){if(b=c.target||c.srcElement)b=parseInt(b.getAttribute(&quot;data-bc-index&quot;),10),a.index!=b&amp;&amp;x(this,a,d,b,b<a.index)};var y=function(a,b){a.modifyCssClass(17,&quot;frame&quot;+b);a.modifyCssClass(18,&quot;bcactive&quot;+b)},z=function(a,b){a.modifyCssClass(17,&quot;frame&quot;+b,!0);a.modifyCssClass(18,&quot;bcactive&quot;+b,!0)},x=function(a,b,d,c,e){0<=c&amp;&amp;c<b.k&amp;&amp;(&quot;slide&quot;==b.q?(e=e?&quot;prev&quot;:&quot;next&quot;,z(d,b.index),y(d,c),a.h&amp;&amp;d.modifyCssClass(17,a.h,!0),a.h=&quot;frame&quot;+c+e,d.modifyCssClass(17,a.h)):(z(d,b.index),y(d,c)),b.index=c)};v.prototype.u=function(a){if(a.has(17)){var b=new w(parseInt(a.getAttribute(17,&quot;data-num-frames&quot;),10),a.getAttribute(17,&quot;data-multiframe-type&quot;));y(a,0);this.s&amp;&amp;(b.l=l(this.w,this,b),a.listen(0,&quot;touchstart&quot;,b.l),a.listen(0,b.g?&quot;touchcancel&quot;:&quot;touchmove&quot;,b.l),a.listen(0,&quot;touchend&quot;,b.l));a.has(18)&amp;&amp;a.listen(18,&quot;click&quot;,l(this.v,this,b))}};var A=[&quot;MultiframeConstructor&quot;],B=f;A[0]in B||!B.execScript||B.execScript(&quot;var &quot;+A[0]);for(var C;A.length&amp;&amp;(C=A.shift());){var D;if(D=!A.length)D=void 0!==v;D?B[C]=v:B=B[C]?B[C]:B[C]={}};})();</script></head><body><style>#adunit {background-color: #ffffff;height: 90px;width: 728px;}#ads {height: 90px;left: 0px;position: absolute;top: 0px;width: 728px;}#ads ul{list-style: none;}#ads ul li {clear: both;float: left;line-height: 0;overflow: hidden;position: relative;  }#ads table {border-collapse: collapse;border-spacing: 0;}.separator {border-bottom: 1px solid #d1d1d1;}.rhtitle {color: #3d81ee;text-decoration: none;word-wrap: break-word;}.rhtitle-adbadge {background-color: #EDB802;border-radius: 2px;color: #FFFFFF;font-family: &quot;Arial Regular&quot;, &quot;Arial&quot;, sans;font-size: 13px;font-weight: normal;height: 15px;margin: 0 3px;padding: 0 3px;}a.rhtitle:hover {text-decoration: underline;}.icoret-bullet {vertical-align: top;color: #666;}.icoret-title {border-spacing: 2px;margin-left: -8px;table-layout: fixed;word-break: break-word;}.rh-title-overlay {margin: -100%;padding: 100%;}.rhtitle-fade {background: -moz-linear-gradient(left, rgba(255,255,255,0) 75%, #ffffff 95%);background: -webkit-gradient(linear, left top, right top, color-stop(75%,rgba(255,255,255,0)), color-stop(95%, #ffffff));background: -webkit-linear-gradient(left, rgba(255,255,255,0) 75%, #ffffff 95%);background: -o-linear-gradient(left, rgba(255,255,255,0) 75%, #ffffff 95%);background: -ms-linear-gradient(left, rgba(255,255,255,0) 75%, #ffffff 95%);background: linear-gradient(to right, rgba(255,255,255,0) 75%, #ffffff 95%);display: inline;pointer-events: none;}.rhbody {color: #000000;text-decoration: none;word-wrap: break-word;}a.rhbody:hover {text-decoration: underline;}.rhurlctr {cursor: pointer;overflow: hidden;text-overflow: ellipsis;white-space: nowrap;}.rhurlctr_nc {overflow: hidden;text-overflow: ellipsis;white-space: nowrap;}.rhurl {text-decoration: none;}.rhurl:hover {text-decoration: underline;color: #78b749;}.rhurl span {color: #78b749;}.rhbutton-container {left: -232px;position: relative;text-align: right;visibility: hidden;width: 314px;}.rhbutton {background: #a5a5a5;-webkit-border-radius: 6px;border-radius: 6px;border-width: 0px;cursor: pointer;display: inline-block;height: 61px;min-width: 82px;max-width: 314px;margin: 0;text-align: center;visibility: visible;white-space: nowrap;}.rhbutton:hover {background: #767676;}.onhoverbg {background: #f8f8f8;}.rhbutton .icon-container {display: inline-block;height: 61px;line-height: 61px;vertical-align: middle;width: 28px;}.rhbutton .icon {border-width: 0;height: 28px;margin-left: 2px;margin-top: 16px;}.rhbutton.nobackground,.rhbutton.nobackground:hover {background: none;}.rh-box-breadcrumbs {line-height: 19px;visibility: visible;}.rh-box-breadcrumbs > .target {cursor: pointer;display: inline-block;height: 19px;vertical-align: middle;}.rh-box-breadcrumbs > .target > .unit {border: 1px solid #aaa;border-radius: 50%;display: inline-block;height: 8px;margin: 4px 5px;width: 8px;}.rh-box-breadcrumbs > .target:hover > .unit {background: #aaa;}.rh-box-breadcrumbs > .target.bcfirst > .unit {margin-left: 15px;}.rh-box-breadcrumbs > .target.bclast > .unit {margin-right: 15px;}.rh-box-breadcrumbs.bcactive0 >.target0 {cursor: default;}.rh-box-breadcrumbs.bcactive0 >.target0 > .unit {background: #aaa;}.rh-box-breadcrumbs.bcactive1 >.target1 {cursor: default;}.rh-box-breadcrumbs.bcactive1 >.target1 > .unit {background: #aaa;}#ads ul li{height:90px;width:728px} .rh{display:inline-block;font-size:0;line-height:0;overflow:hidden;padding:0;width:728px} .rh > table{height:100%} .rh1{display:inline-block;font-size:0;line-height:0;overflow:hidden;padding:0;width:518px} .rh1 > table{width:100%} .rh10{display:inline-block;font-size:37px;line-height:44px;overflow:hidden;padding:0 0 0 9px;white-space:nowrap} .rh10c{padding:0} .rh11{display:inline-block;font-size:0;height:27px;line-height:0;overflow:hidden;padding:0;position:relative;width:518px} .rh11.frame0>.rh110{display:inline-block;visibility:visible} .rh11.frame1>.rh111{display:inline-block;visibility:visible} .rh110{display:inline-block;font-size:0;height:27px;line-height:0;overflow:hidden;padding:0;position:absolute} .rh110 > table{height:100%} .rh1100{display:inline-block;font-size:0;line-height:0;overflow:hidden;padding:0;width:518px} .rh1100 > table{width:100%} .rh11000{display:inline-block;font-size:16px;line-height:19px;overflow:hidden;padding:0 0 0 9px} .rh11000c{padding:0} .rh1100c{padding:0;vertical-align:middle;width:518px} .rh111{display:inline-block;font-size:0;height:27px;line-height:0;overflow:hidden;padding:0;position:absolute} .rh111 > table{height:100%} .rh1110{display:inline-block;font-size:16px;line-height:19px;overflow:hidden;padding:4px 0 4px 9px;white-space:nowrap} .rh1110c{padding:0;vertical-align:middle} .rh11>.rh110{display:none;visibility:hidden} .rh11>.rh111{display:none;visibility:hidden} .rh11c{height:27px;padding:0;vertical-align:middle;width:518px} .rh12{display:inline-block;height:19px;overflow:hidden;padding:0;width:518px} .rh12c{height:19px;padding:0;text-align:center;width:518px} .rh1c{padding:0;width:518px} .rh2{display:inline-block;overflow:hidden;padding:0;width:28px} .rh2c{padding:0;width:28px} .rh3{display:inline-block;height:61px;padding:0 75px 0 4px;width:82px} .rh3c{padding:0;vertical-align:middle;width:161px} .rh4{display:inline-block;overflow:hidden;padding:0;width:21px} .rh4c{padding:0;width:21px}</style><div id=adunit><div id=ads ><ul><li id=taw0 lang=&quot;en&quot;><div class=&quot;rh&quot;><table><tr><td class=&quot;rh1c&quot;><div class=&quot;rh1&quot;><table><tr><td class=&quot;rh10c&quot;><div class=&quot;rh-box-title rh-title rh10 collapsed-box&quot;><a class=&quot;rhtitle&quot; href=&quot;http://www.googleadservices.com/pagead/aclk?sa=L&amp;ai=C9A9MgYG2VL3WJZaz8AWLxoCoB7S9hP8F3PPzkeABwI23ARABINCkggpg4bS6hZAaoAHlobLsA8gBAeACAKgDAcgDmwSqBKoBT9AgoVEbpPGzKm7BPPaEWTbnQupOYAXMNP4E8-1SvS18OtW8eU1Dw-xgY9NSwHsJCob6li0qpP1RmnCoOJe4kVk6yX5OxMPIc1kP3hK4_xhZEpTST6BQhI_JgKLu0-oWgriOhLN2Ztya9JhBi8iUSTsBB7aCIG_mz0XHJvPA1pJvDdia--dH8-6O6QPVmiwXUdrvNBZyFG_OnmGAZVZ6dGIBBQVd3DZD8fngBAGIBgGAB_T05iI&amp;num=1&amp;cid=5GjhT6uBLHI2p4QPCXAKGlAD&amp;sig=AOD64_0BdB-YmFgalCLnh8_FLcN_XoHg8A&amp;client=ca-pub-7291399211842501&amp;adurl=http://www.facebook.com/campaign/landing.php%3F%26campaign_id%3D405847549575186%26extra_1%3DcVopPAthe%7Cc%7C60274623380%7C%7Csign%2520in%2520account%7Cwww.scribd.com%7C8095u2d44905%26placement%3Dwww.scribd.com%26creative%3D60274623380%26keyword%3Dsign%2520in%2520account%26partner_id%3Dgooglesem%26extra_2%3Dd%26matchtype%3D%26target%3D%26source%3D%26adposition%3Dnone%26aceid%3D&quot; target=_top title=&quot;facebook.com&quot;><span>Facebook® Account Sign Up</span></a></div></td></tr><tr><td class=&quot;rh11c&quot;><div class=&quot;rh-box-multiframe rh11 rh-multiframe frame0&quot; data-num-frames=&quot;2&quot; data-multiframe-type=&quot;normal&quot;><div class=&quot;rh110&quot;><table><tr><td class=&quot;rh1100c&quot;><div class=&quot;rh1100&quot;><table><tr><td class=&quot;rh11000c&quot;><div class=&quot;rh-body rh-box-body rh11000&quot;><span class=&quot;rhbody&quot;>World&amp;#39;s Largest Online Community. Join for Free &amp;amp; Enjoy the Benefits!</span></div></td></tr></table></div></td></tr></table></div><div class=&quot;rh111&quot;><table><tr><td class=&quot;rh1110c&quot;><div class=&quot;rh-box-url rh-url rh1110&quot;><div class=&quot;rhurlctr&quot; dir=&quot;ltr&quot;><a class=&quot;rhurl&quot; title=&quot;facebook.com&quot; href=&quot;http://www.googleadservices.com/pagead/aclk?sa=L&amp;ai=C9A9MgYG2VL3WJZaz8AWLxoCoB7S9hP8F3PPzkeABwI23ARABINCkggpg4bS6hZAaoAHlobLsA8gBAeACAKgDAcgDmwSqBKoBT9AgoVEbpPGzKm7BPPaEWTbnQupOYAXMNP4E8-1SvS18OtW8eU1Dw-xgY9NSwHsJCob6li0qpP1RmnCoOJe4kVk6yX5OxMPIc1kP3hK4_xhZEpTST6BQhI_JgKLu0-oWgriOhLN2Ztya9JhBi8iUSTsBB7aCIG_mz0XHJvPA1pJvDdia--dH8-6O6QPVmiwXUdrvNBZyFG_OnmGAZVZ6dGIBBQVd3DZD8fngBAGIBgGAB_T05iI&amp;num=1&amp;cid=5GjhT6uBLHI2p4QPCXAKGlAD&amp;sig=AOD64_0BdB-YmFgalCLnh8_FLcN_XoHg8A&amp;client=ca-pub-7291399211842501&amp;adurl=http://www.facebook.com/campaign/landing.php%3F%26campaign_id%3D405847549575186%26extra_1%3DcVopPAthe%7Cc%7C60274623380%7C%7Csign%2520in%2520account%7Cwww.scribd.com%7C8095u2d44905%26placement%3Dwww.scribd.com%26creative%3D60274623380%26keyword%3Dsign%2520in%2520account%26partner_id%3Dgooglesem%26extra_2%3Dd%26matchtype%3D%26target%3D%26source%3D%26adposition%3Dnone%26aceid%3D&quot; target=&quot;_top&quot;><span>facebook.com</span></a></div></div></td></tr></table></div></div></td></tr><tr><td class=&quot;rh12c&quot;><div class=&quot;rh-box-breadcrumbs rh12&quot;><div class=&quot;target target0 bcfirst&quot; data-bc-index=&quot;0&quot;><div class=&quot;unit&quot; data-bc-index=&quot;0&quot;></div></div><div class=&quot;target target1 bclast&quot; data-bc-index=&quot;1&quot;><div class=&quot;unit&quot; data-bc-index=&quot;1&quot;></div></div></div></td></tr></table></div></td><td class=&quot;rh2c&quot;><div class=&quot;rh-box-empty rh2&quot;></div></td><td class=&quot;rh3c&quot;><div class=&quot;rh-box-button rh-nessie-button-flat rh3&quot;><div class=&quot;rhbutton-container&quot;><a class=&quot;rhbutton&quot; href=&quot;http://www.googleadservices.com/pagead/aclk?sa=L&amp;ai=C9A9MgYG2VL3WJZaz8AWLxoCoB7S9hP8F3PPzkeABwI23ARABINCkggpg4bS6hZAaoAHlobLsA8gBAeACAKgDAcgDmwSqBKoBT9AgoVEbpPGzKm7BPPaEWTbnQupOYAXMNP4E8-1SvS18OtW8eU1Dw-xgY9NSwHsJCob6li0qpP1RmnCoOJe4kVk6yX5OxMPIc1kP3hK4_xhZEpTST6BQhI_JgKLu0-oWgriOhLN2Ztya9JhBi8iUSTsBB7aCIG_mz0XHJvPA1pJvDdia--dH8-6O6QPVmiwXUdrvNBZyFG_OnmGAZVZ6dGIBBQVd3DZD8fngBAGIBgGAB_T05iI&amp;num=1&amp;cid=5GjhT6uBLHI2p4QPCXAKGlAD&amp;sig=AOD64_0BdB-YmFgalCLnh8_FLcN_XoHg8A&amp;client=ca-pub-7291399211842501&amp;adurl=http://www.facebook.com/campaign/landing.php%3F%26campaign_id%3D405847549575186%26extra_1%3DcVopPAthe%7Cc%7C60274623380%7C%7Csign%2520in%2520account%7Cwww.scribd.com%7C8095u2d44905%26placement%3Dwww.scribd.com%26creative%3D60274623380%26keyword%3Dsign%2520in%2520account%26partner_id%3Dgooglesem%26extra_2%3Dd%26matchtype%3D%26target%3D%26source%3D%26adposition%3Dnone%26aceid%3D&quot; target=&quot;_top&quot; title=&quot;facebook.com&quot;><div class=&quot;icon-container&quot;><img alt=&quot;&quot; class=&quot;icon&quot; src=&quot;https://tpc.googlesyndication.com/pagead/images/nessie_icon_tiamat_white.png&quot;/></div></a></div></div></td><td class=&quot;rh4c&quot;><div class=&quot;rh-box-empty rh4&quot;></div></td></tr></table></div></li><script>var ad = buildRhTextAd([0,0,728,90,&quot;http://www.facebook.com/campaign/landing.php?\u0026campaign_id=405847549575186\u0026extra_1=cVopPAthe|c|60274623380||sign%20in%20account|www.scribd.com|8095u2d44905\u0026placement=www.scribd.com\u0026creative=60274623380\u0026keyword=sign%20in%20account\u0026partner_id=googlesem\u0026extra_2=d\u0026matchtype=\u0026target=\u0026source=\u0026adposition=none\u0026aceid=&quot;]);registerAd(ad,'taw0');adSlot.addAd(ad);</script></ul></div></div><style>div,ul,li{margin:0;padding:0;}#abgc{height:15px;position:absolute;right:0px;text-rendering:geometricPrecision;top:0;width:19px;z-index:9010;}#abgb{height:100%;}#abgc img{display:block;}#abgc svg{display:block;}#abgs{display:none;height:100%;}#abgl{text-decoration:none;}</style><div id=abgc><div id=abgb></div><div id=abgs><a id=abgl href=&quot;https://www.google.com/url?ct=abg&amp;amp;q=https://www.google.com/adsense/support/bin/request.py%3Fcontact%3Dabg_afc%26url%3Dhttps://www.scribd.com/doc/90484468/Rizal-by-Austin-Coates%26gl%3DPH%26hl%3Den%26client%3Dca-pub-7291399211842501%26ai0%3DC9A9MgYG2VL3WJZaz8AWLxoCoB7S9hP8F3PPzkeABwI23ARABINCkggpg4bS6hZAaoAHlobLsA8gBAeACAKgDAcgDmwSqBKoBT9AgoVEbpPGzKm7BPPaEWTbnQupOYAXMNP4E8-1SvS18OtW8eU1Dw-xgY9NSwHsJCob6li0qpP1RmnCoOJe4kVk6yX5OxMPIc1kP3hK4_xhZEpTST6BQhI_JgKLu0-oWgriOhLN2Ztya9JhBi8iUSTsBB7aCIG_mz0XHJvPA1pJvDdia--dH8-6O6QPVmiwXUdrvNBZyFG_OnmGAZVZ6dGIBBQVd3DZD8fngBAGIBgGAB_T05iI&amp;amp;usg=AFQjCNE1gTmbKUS351GiKOYlVxhSshLvJA&quot; target=_blank></a></div></div><script>var abgp={el:document.getElementById('abgc'),ael:document.getElementById('abgs'),iel:document.getElementById('abgb'),hw:19,sw:77,hh:15,sh:15,himg:'https://tpc.googlesyndication.com'+'/pagead/images/ad_choices_i.png',simg:'https://tpc.googlesyndication.com/pagead/images/ad_choices_en.png',alt:'AdChoices',t:'AdChoices',tw:53,t2:'',t2w:0,tbo:0,att:'adchoices',ff:'img',halign:'right',fe:false,fnb:false,iba:false,uic:false,icd:undefined};</script><script src=&quot;https://tpc.googlesyndication.com/pagead/js/r20150108/r20110914/abg.js&quot;></script><script type=&quot;text/javascript&quot;>(function(){var h=this,m=function(a){var b=typeof a;if(&quot;object&quot;==b)if(a){if(a instanceof Array)return&quot;array&quot;;if(a instanceof Object)return b;var c=Object.prototype.toString.call(a);if(&quot;[object Window]&quot;==c)return&quot;object&quot;;if(&quot;[object Array]&quot;==c||&quot;number&quot;==typeof a.length&amp;&amp;&quot;undefined&quot;!=typeof a.splice&amp;&amp;&quot;undefined&quot;!=typeof a.propertyIsEnumerable&amp;&amp;!a.propertyIsEnumerable(&quot;splice&quot;))return&quot;array&quot;;if(&quot;[object Function]&quot;==c||&quot;undefined&quot;!=typeof a.call&amp;&amp;&quot;undefined&quot;!=typeof a.propertyIsEnumerable&amp;&amp;!a.propertyIsEnumerable(&quot;call&quot;))return&quot;function&quot;}else return&quot;null&quot;;else if(&quot;function&quot;==b&amp;&amp;&quot;undefined&quot;==typeof a.call)return&quot;object&quot;;return b},p=function(a){return&quot;string&quot;==typeof a},aa=function(a,b){var c=Array.prototype.slice.call(arguments,1);return function(){var b=c.slice();b.push.apply(b,arguments);return a.apply(this,b)}},q=Date.now||function(){return+new Date},r=function(a,b){var c=a.split(&quot;.&quot;),d=h;c[0]in d||!d.execScript||d.execScript(&quot;var &quot;+c[0]);for(var e;c.length&amp;&amp;(e=c.shift());)c.length||void 0===b?d=d[e]?d[e]:d[e]={}:d[e]=b};var t=function(a,b,c,d,e){if(e)c=a+(&quot;&amp;&quot;+b+&quot;=&quot;+c);else{var f=&quot;&amp;&quot;+b+&quot;=&quot;,g=a.indexOf(f);0>g?c=a+f+c:(g+=f.length,f=a.indexOf(&quot;&amp;&quot;,g),c=0<=f?a.substring(0,g)+c+a.substring(f):a.substring(0,g)+c)}return 2E3<c.length?void 0!==d?t(a,b,d,void 0,e):a:c};var ba=function(){var a=/[&amp;\?]exk=([^&amp; ]+)/.exec(w.location.href);return a&amp;&amp;2==a.length?a[1]:null};var ca=function(a){var b=a.toString();a.name&amp;&amp;-1==b.indexOf(a.name)&amp;&amp;(b+=&quot;: &quot;+a.name);a.message&amp;&amp;-1==b.indexOf(a.message)&amp;&amp;(b+=&quot;: &quot;+a.message);if(a.stack){a=a.stack;var c=b;try{-1==a.indexOf(c)&amp;&amp;(a=c+&quot;\n&quot;+a);for(var d;a!=d;)d=a,a=a.replace(/((https?:\/..*\/)[^\/:]*:\d+(?:.|\n)*)\2/,&quot;$1&quot;);b=a.replace(/\n */g,&quot;\n&quot;)}catch(e){b=c}}return b},x=function(a,b){a.google_image_requests||(a.google_image_requests=[]);var c=a.document.createElement(&quot;img&quot;);c.src=b;a.google_image_requests.push(c)};var y=document,w=window;var da=String.prototype.trim?function(a){return a.trim()}:function(a){return a.replace(/^[\s\xa0]+|[\s\xa0]+$/g,&quot;&quot;)},ea=function(a,b){return a<b?-1:a>b?1:0};var z=null,fa=function(a,b){for(var c in a)Object.prototype.hasOwnProperty.call(a,c)&amp;&amp;b.call(null,a[c],c,a)};function A(a){return&quot;function&quot;==typeof encodeURIComponent?encodeURIComponent(a):escape(a)}var ga=function(){if(!y.body)return!1;if(!z){var a=y.createElement(&quot;iframe&quot;);a.style.display=&quot;none&quot;;a.id=&quot;anonIframe&quot;;z=a;y.body.appendChild(a)}return!0},ha={};var ia=!0,ja={},ma=function(a,b,c,d){var e=ka,f,g=ia;try{f=b()}catch(k){try{var u=ca(k);b=&quot;&quot;;k.fileName&amp;&amp;(b=k.fileName);var v=-1;k.lineNumber&amp;&amp;(v=k.lineNumber);g=e(a,u,b,v,c)}catch(n){try{var l=ca(n);a=&quot;&quot;;n.fileName&amp;&amp;(a=n.fileName);c=-1;n.lineNumber&amp;&amp;(c=n.lineNumber);ka(&quot;pAR&quot;,l,a,c,void 0,void 0)}catch(wa){la({context:&quot;mRE&quot;,msg:wa.toString()+&quot;\n&quot;+(wa.stack||&quot;&quot;)},void 0)}}if(!g)throw k;}finally{if(d)try{d()}catch(hb){}}return f},ka=function(a,b,c,d,e,f){var g={};if(e)try{e(g)}catch(k){}g.context=a;g.msg=b.substring(0,512);c&amp;&amp;(g.file=c);0<d&amp;&amp;(g.line=d.toString());g.url=y.URL.substring(0,512);g.ref=y.referrer.substring(0,512);na(g);la(g,f);return ia},la=function(a,b){try{if(Math.random()<(b||.01)){var c=&quot;/pagead/gen_204?id=jserror&quot;+oa(a),d=&quot;http&quot;+(&quot;http:&quot;==w.location.protocol?&quot;&quot;:&quot;s&quot;)+&quot;://pagead2.googlesyndication.com&quot;+c,d=d.substring(0,2E3);x(w,d)}}catch(e){}},na=function(a){var b=a||{};fa(ja,function(a,d){b[d]=w[a]})},B=function(a,b,c,d,e){return function(){var f=arguments;return ma(a,function(){return b.apply(c,f)},d,e)}},pa=function(a,b){return B(a,b,void 0,void 0,void 0)},oa=function(a){var b=&quot;&quot;;fa(a,function(a,d){if(0===a||a)b+=&quot;&amp;&quot;+d+&quot;=&quot;+A(a)});return b};var C=Array.prototype,qa=C.indexOf?function(a,b,c){return C.indexOf.call(a,b,c)}:function(a,b,c){c=null==c?0:0>c?Math.max(0,a.length+c):c;if(p(a))return p(b)&amp;&amp;1==b.length?a.indexOf(b,c):-1;for(;c<a.length;c++)if(c in a&amp;&amp;a[c]===b)return c;return-1},ra=C.map?function(a,b,c){return C.map.call(a,b,c)}:function(a,b,c){for(var d=a.length,e=Array(d),f=p(a)?a.split(&quot;&quot;):a,g=0;g<d;g++)g in f&amp;&amp;(e[g]=b.call(c,f[g],g,a));return e};var sa={c:947190538,d:947190541};if(y&amp;&amp;y.URL)var ta=y.URL,ia=!(ta&amp;&amp;(0<ta.indexOf(&quot;?google_debug&quot;)||0<ta.indexOf(&quot;&amp;google_debug&quot;)));var D=function(a,b,c,d){c=B(d||&quot;osd_or_lidar::&quot;+b,c,void 0,void 0,void 0);a.addEventListener?a.addEventListener(b,c,!1):a.attachEvent&amp;&amp;a.attachEvent(&quot;on&quot;+b,c)},ua=function(a){var b=0,c=function(){a();b++;10>b&amp;&amp;w.setTimeout(pa(&quot;osd_listener::ldcl_int&quot;,c),100)};c()};var va=function(){try{w.localStorage.setItem(&quot;__sak&quot;,&quot;1&quot;);var a=w.localStorage.__sak;w.localStorage.removeItem(&quot;__sak&quot;);return&quot;1&quot;==a}catch(b){return!1}},xa=function(a,b,c){a.google_image_requests||(a.google_image_requests=[]);var d=a.document.createElement(&quot;img&quot;);D(d,&quot;load&quot;,c,&quot;osd::ls_img::load&quot;);d.src=b;a.google_image_requests.push(d)};var ya=function(a,b){for(var c in a)b.call(void 0,a[c],c,a)},E=function(a){var b=arguments.length;if(1==b&amp;&amp;&quot;array&quot;==m(arguments[0]))return E.apply(null,arguments[0]);for(var c={},d=0;d<b;d++)c[arguments[d]]=!0;return c};var F;r:{var za=h.navigator;if(za){var Aa=za.userAgent;if(Aa){F=Aa;break r}}F=&quot;&quot;};var Ba=-1!=F.indexOf(&quot;Opera&quot;)||-1!=F.indexOf(&quot;OPR&quot;),G=-1!=F.indexOf(&quot;Trident&quot;)||-1!=F.indexOf(&quot;MSIE&quot;),Ca=-1!=F.indexOf(&quot;Gecko&quot;)&amp;&amp;-1==F.toLowerCase().indexOf(&quot;webkit&quot;)&amp;&amp;!(-1!=F.indexOf(&quot;Trident&quot;)||-1!=F.indexOf(&quot;MSIE&quot;)),Da=-1!=F.toLowerCase().indexOf(&quot;webkit&quot;),Ea=function(){var a=h.document;return a?a.documentMode:void 0},Fa=function(){var a=&quot;&quot;,b;if(Ba&amp;&amp;h.opera)return a=h.opera.version,&quot;function&quot;==m(a)?a():a;Ca?b=/rv\:([^\);]+)(\)|;)/:G?b=/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/:Da&amp;&amp;(b=/WebKit\/(\S+)/);b&amp;&amp;(a=(a=b.exec(F))?a[1]:&quot;&quot;);return G&amp;&amp;(b=Ea(),b>parseFloat(a))?String(b):a}(),Ga={},Ha=function(a){if(!Ga[a]){for(var b=0,c=da(String(Fa)).split(&quot;.&quot;),d=da(String(a)).split(&quot;.&quot;),e=Math.max(c.length,d.length),f=0;0==b&amp;&amp;f<e;f++){var g=c[f]||&quot;&quot;,k=d[f]||&quot;&quot;,u=RegExp(&quot;(\\d*)(\\D*)&quot;,&quot;g&quot;),v=RegExp(&quot;(\\d*)(\\D*)&quot;,&quot;g&quot;);do{var n=u.exec(g)||[&quot;&quot;,&quot;&quot;,&quot;&quot;],l=v.exec(k)||[&quot;&quot;,&quot;&quot;,&quot;&quot;];if(0==n[0].length&amp;&amp;0==l[0].length)break;b=ea(0==n[1].length?0:parseInt(n[1],10),0==l[1].length?0:parseInt(l[1],10))||ea(0==n[2].length,0==l[2].length)||ea(n[2],l[2])}while(0==b)}Ga[a]=0<=b}},Ia=h.document,Ja=Ia&amp;&amp;G?Ea()||(&quot;CSS1Compat&quot;==Ia.compatMode?parseInt(Fa,10):5):void 0;var H=function(a,b){this.b=a||0;this.a=b||&quot;&quot;},Ka=function(a,b){a.b&amp;&amp;(b[4]=a.b);a.a&amp;&amp;(b[12]=a.a)};H.prototype.match=function(a){return(this.b||this.a)&amp;&amp;(a.b||a.a)?this.a||a.a?this.a==a.a:this.b||a.b?this.b==a.b:!1:!1};H.prototype.toString=function(){var a=&quot;&quot;+this.b;this.a&amp;&amp;(a+=&quot;-&quot;+this.a);return a};var La=function(){var a=I,b=[];a.b&amp;&amp;b.push(&quot;adk=&quot;+a.b);a.a&amp;&amp;b.push(&quot;exk=&quot;+a.a);return b},Ma=function(a){var b=[];ya(a,function(a,d){var e=A(d),f=a;p(f)&amp;&amp;(f=A(f));b.push(e+&quot;=&quot;+f)});return b.join(&quot;\n&quot;)},J=0,Na=0,Oa=function(a){var b=0,c=w;if(c&amp;&amp;c.Goog_AdSense_getAdAdapterInstance)return c;try{for(;c&amp;&amp;5>b;){if(c.google_osd_static_frame)return c;if(c.aswift_0&amp;&amp;(!a||c.aswift_0.google_osd_static_frame))return c.aswift_0;b++;c=c!=c.parent?c.parent:null}}catch(d){}return null},Pa=function(a,b,c,d){if(10<Na)w.clearInterval(J);else if(++Na,w.postMessage&amp;&amp;(b.b||b.a)){var e=Oa(!0);if(e){var f={};Ka(b,f);f[0]=&quot;goog_request_monitoring&quot;;f[6]=a;f[16]=c;d&amp;&amp;d.length&amp;&amp;(f[17]=d.join(&quot;,&quot;));try{var g=Ma(f);e.postMessage(g,&quot;*&quot;)}catch(k){}}}};E(&quot;area base br col command embed hr img input keygen link meta param source track wbr&quot;.split(&quot; &quot;));E(&quot;action&quot;,&quot;cite&quot;,&quot;data&quot;,&quot;formaction&quot;,&quot;href&quot;,&quot;manifest&quot;,&quot;poster&quot;,&quot;src&quot;);E(&quot;embed&quot;,&quot;iframe&quot;,&quot;link&quot;,&quot;object&quot;,&quot;script&quot;,&quot;style&quot;,&quot;template&quot;);var Qa;if(!(Qa=!Ca&amp;&amp;!G)){var Ra;if(Ra=G)Ra=G&amp;&amp;9<=Ja;Qa=Ra}Qa||Ca&amp;&amp;Ha(&quot;1.9.1&quot;);G&amp;&amp;Ha(&quot;9&quot;);var Sa,K=0,L=&quot;&quot;,M=!1,N=!1,O=!1,Ta=!1,Ua=[],I=null,P=&quot;&quot;,Va=[],Wa=[],Xa=!1,Q=&quot;&quot;,R=&quot;&quot;,Ya=(new Date).getTime(),Za=[&quot;1&quot;,&quot;0&quot;,&quot;3&quot;],S=0,T=!1,U=&quot;&quot;,V=null,W=0,X=0,$a=0,ab=function(a,b){M&amp;&amp;Y(a,b,!0);(O||N&amp;&amp;Ta)&amp;&amp;Y(a,b)},Y=function(a,b,c){if((b=b||P)&amp;&amp;!Xa&amp;&amp;(2==X||c)){b=bb(b,c);if(!c&amp;&amp;T){T=!1;V&amp;&amp;(a.clearInterval(V),V=null);var d=U;try{a.localStorage[d]=b+&quot;&amp;timestamp=&quot;+q()+&quot;&amp;send&quot;}catch(e){}5!=S&amp;&amp;xa(a,b,function(){a.localStorage.removeItem(d)})}else x(a,b);c?M=!1:Xa=!0}},bb=function(a,b){var c;c=b?&quot;osdim&quot;:O?&quot;osd2&quot;:&quot;osdtos&quot;;var d=[&quot;//pagead2.googlesyndication.com/activeview&quot;,&quot;?id=&quot;,c];&quot;osd2&quot;==c&amp;&amp;N&amp;&amp;Ta&amp;&amp;d.push(&quot;&amp;ts=1&quot;);L&amp;&amp;d.push(&quot;&amp;avi=&quot;,L);Sa&amp;&amp;d.push(&quot;&amp;cid=&quot;,Sa);0!=S&amp;&amp;d.push(&quot;&amp;lsid=&quot;,S);T&amp;&amp;d.push(&quot;&amp;cwls=1&quot;);d.push(&quot;&amp;ti=1&quot;);d.push(&quot;&amp;&quot;,a);d.push(&quot;&amp;uc=&quot;+$a);c=d.join(&quot;&quot;);for(d=0;d<Va.length;d++){try{var e=Va[d]()}catch(f){}var g=&quot;max_length&quot;;2<=e.length&amp;&amp;(3==e.length&amp;&amp;(g=e[2]),c=t(c,A(e[0]),A(e[1]),g))}2E3<c.length&amp;&amp;(c=c.substring(0,2E3));return c},Z=function(a,b){if(Q){try{var c=t(Q,&quot;vi&quot;,a);ga()&amp;&amp;x(z.contentWindow,c)}catch(d){}0<=qa(Za,a)&amp;&amp;(Q=&quot;&quot;);var c=b||P,e;e=t(&quot;//pagead2.googlesyndication.com/pagead/gen_204?id=sldb&quot;,&quot;avi&quot;,L);e=t(e,&quot;vi&quot;,a);c&amp;&amp;(e+=&quot;&amp;&quot;+c);try{x(w,e)}catch(f){}}},cb=function(){Z(&quot;-1&quot;)},eb=function(a){if(a&amp;&amp;a.data&amp;&amp;p(a.data)){var b;var c=a.data;if(p(c)){b={};for(var c=c.split(&quot;\n&quot;),d=0;d<c.length;d++){var e=c[d].indexOf(&quot;=&quot;);if(!(0>=e)){var f=Number(c[d].substr(0,e)),e=c[d].substr(e+1);switch(f){case 5:case 8:case 11:case 15:case 16:e=&quot;true&quot;==e;break;case 4:case 7:case 6:case 14:e=Number(e);break;case 3:if(&quot;function&quot;==m(decodeURIComponent))try{e=decodeURIComponent(e)}catch(g){throw Error(&quot;Error: URI malformed: &quot;+e);}break;case 17:e=ra(decodeURIComponent(e).split(&quot;,&quot;),Number)}b[f]=e}}b=b[0]?b:null}else b=null;if(b&amp;&amp;(c=new H(b[4],b[12]),I&amp;&amp;I.match(c))){for(c=0;c<Wa.length;c++)Wa[c](b);c=b[0];if(&quot;goog_acknowledge_monitoring&quot;==c)w.clearInterval(J),W=2;else if(&quot;goog_get_mode&quot;==c){W=1;d={};I&amp;&amp;Ka(I,d);d[0]=&quot;goog_provide_mode&quot;;d[6]=X;try{var k=Ma(d);a.source.postMessage(k,a.origin)}catch(u){}w.clearInterval(J);W=2}else if(&quot;goog_update_data&quot;==c){if(a=w,P=b[3],++$a,T){k=U;d=bb(P);try{a.localStorage[k]=db(d)}catch(v){}}}else&quot;goog_image_request&quot;==c&amp;&amp;(ab(w,b[3]),b[5]||b[11]||Z(&quot;0&quot;,b[3]));if(&quot;goog_update_data&quot;==c||&quot;goog_image_request&quot;==c)(1==X||2==X||M)&amp;&amp;b[5]&amp;&amp;(a=1==b[15]&amp;&amp;&quot;goog_update_data&quot;==c,Ta=!0,Z(&quot;1&quot;),R&amp;&amp;(k=R,ga()&amp;&amp;x(z.contentWindow,k),R=&quot;&quot;),M&amp;&amp;!a&amp;&amp;Y(w,void 0,!0),1==X?Xa=!0:(2==S||4==S||5==S&amp;&amp;!T)&amp;&amp;Y(w)),(1==X||2==X||M)&amp;&amp;b[11]&amp;&amp;(N=!1,Z(&quot;3&quot;),M&amp;&amp;Y(w,void 0,!0),(2==S||4==S||5==S&amp;&amp;!T)&amp;&amp;Y(w))}}},fb=function(){ab(w);Z(&quot;0&quot;);if(2>W&amp;&amp;2==X){var a=w,b=&quot;//pagead2.googlesyndication.com/pagead/gen_204?id=osd2&amp;&quot;,c=[];c.push(&quot;ovr_value=&quot;+K);c.push(&quot;avi=&quot;+L);I&amp;&amp;(c=c.concat(La()));c.push(&quot;tt=&quot;+((new Date).getTime()-Ya));a.document&amp;&amp;a.document.referrer&amp;&amp;c.push(&quot;ref=&quot;+A(a.document.referrer));c.push(&quot;hs=&quot;+W);b+=c.join(&quot;&amp;&quot;);try{x(a,b)}catch(d){}}},db=function(a){var b=a.match(/^(.*&amp;timestamp=)\d+$/);return b?b[1]+q():a+&quot;&amp;timestamp=&quot;+q()},gb=function(){var a={};Ka(I,a);a[0]=&quot;goog_dom_content_loaded&quot;;var b=Ma(a);ua(function(){var a=Oa(!1),d=!a;!a&amp;&amp;w&amp;&amp;(a=w.parent);if(a&amp;&amp;a.postMessage)try{a.postMessage(b,&quot;*&quot;),d&amp;&amp;w.postMessage(b,&quot;*&quot;)}catch(e){}})};r(&quot;osdlfm&quot;,B(&quot;osd_listener::init&quot;,function(a,b,c,d,e,f,g,k,u,v,n){K=a;Q=b;R=d;M=f;S=v||0;Sa=n;N=g&amp;&amp;f;1!=u&amp;&amp;2!=u||Ua.push(sa[&quot;MRC_TEST_&quot;+u]);I=new H(e,ba());D(w,&quot;load&quot;,cb,&quot;osd_listener::load&quot;);D(w,&quot;message&quot;,eb,&quot;osd_listener::message&quot;);L=c||&quot;&quot;;D(w,&quot;unload&quot;,fb,&quot;osd_listener::unload&quot;);var l=w.document;!l.readyState||&quot;complete&quot;!=l.readyState&amp;&amp;&quot;loaded&quot;!=l.readyState?(&quot;msie&quot;in ha?ha.msie:ha.msie=-1!=navigator.userAgent.toLowerCase().indexOf(&quot;msie&quot;))&amp;&amp;!window.opera?D(l,&quot;readystatechange&quot;,function(){&quot;complete&quot;!=l.readyState&amp;&amp;&quot;loaded&quot;!=l.readyState||gb()},&quot;osd_listener::rsc&quot;):D(l,&quot;DOMContentLoaded&quot;,gb,&quot;osd_listener::dcl&quot;):gb();-1==K?X=f?3:1:-2==K?X=3:0<K&amp;&amp;(X=2,O=!0);N&amp;&amp;!O&amp;&amp;(X=2);2==X&amp;&amp;w.location.hostname.match(/doubleclick\.net/)&amp;&amp;(3==S||4==S||5==S)&amp;&amp;va()&amp;&amp;1E3>w.localStorage.length&amp;&amp;(U=&quot;LSPNGS-&quot;+I.toString()+&quot;-&quot;+(&quot;&quot;+Math.random()).split(&quot;.&quot;)[1]+q(),T=!0,V=w.setInterval(pa(&quot;osd_listener::ls_int&quot;,function(){var a=w,b=U,c=a.localStorage[b];if(c)try{a.localStorage[b]=db(c)}catch(d){}}),1E3));I&amp;&amp;(I.b||I.a)&amp;&amp;(W=1,J=w.setInterval(pa(&quot;osd_proto::reqm_int&quot;,aa(Pa,X,I,N,Ua)),500))}));r(&quot;osdlac&quot;,B(&quot;osd_listener::lac_ex&quot;,function(a){Va.push(a)}));r(&quot;osdlamrc&quot;,B(&quot;osd_listener::lamrc_ex&quot;,function(a){Wa.push(a)}));r(&quot;osdsir&quot;,B(&quot;osd_listener::sir_ex&quot;,ab));})();osdlfm(-1,'','BtrSRgYG2VL3WJZaz8AWLxoCoBwDc8_OR4AEAABABOAHIAQHgAgDIA5sE4AQBwhMDEIAB','',3970146942,true,false,'',0,0,'');</script><script>adSlot.finalize('ads');registerAdLocationExtensionRedirectPing(adSlot);</script> <script>(function(){var d=function(a,b,c){return a.call.apply(a.bind,arguments)},e=function(a,b,c){if(!a)throw Error();if(2<arguments.length){var g=Array.prototype.slice.call(arguments,2);return function(){var c=Array.prototype.slice.call(arguments);Array.prototype.unshift.apply(c,g);return a.apply(b,c)}}return function(){return a.apply(b,arguments)}},f=function(a,b,c){f=Function.prototype.bind&amp;&amp;-1!=Function.prototype.bind.toString().indexOf(&quot;native code&quot;)?d:e;return f.apply(null,arguments)},h=Date.now||function(){return+new Date};var k=function(a,b,c){a.addEventListener?a.addEventListener(b,c,!1):a.attachEvent&amp;&amp;a.attachEvent(&quot;on&quot;+b,c)};var l=document,m=window;var q=function(a,b,c,g,w){this.h=!1;this.g=-1;this.j=a;this.k=b;this.l=c;this.i=w;g&amp;&amp;n()&amp;&amp;p(this,2);a=f(this.n,this);k(l,&quot;visibilitychange&quot;,a);k(l,&quot;mozvisibilitychange&quot;,a);k(l,&quot;msvisibilitychange&quot;,a);k(l,&quot;webkitvisibilitychange&quot;,a);a=f(this.m,this);k(m,&quot;click&quot;,a)};q.prototype.n=function(){if(n())this.h&amp;&amp;(this.g=h(),p(this,0));else{if(-1!=this.g){var a=h()-this.g;this.g=-1;p(this,1,a)}this.i&amp;&amp;p(this,3)}};q.prototype.m=function(){this.h=!0;var a=f(this.o,this);m.setTimeout(a,5E3)};q.prototype.o=function(){this.h=!1};var p=function(a,b,c){a=[&quot;//&quot;,a.l?&quot;googleads.g.doubleclick.net&quot;:&quot;pagead2.googlesyndication.com&quot;,&quot;/pagead/gen_204?id=wfocus&quot;,&quot;&amp;gqid=&quot;+a.j,&quot;&amp;qqid=&quot;+a.k].join(&quot;&quot;);0==b&amp;&amp;(a+=&quot;&amp;return=0&quot;);1==b&amp;&amp;(a+=&quot;&amp;return=1&amp;timeDelta=&quot;+c);2==b&amp;&amp;(a+=&quot;&amp;bgload=1&quot;);3==b&amp;&amp;(a+=&quot;&amp;fg=1&quot;);m.google_image_requests||(m.google_image_requests=[]);b=m.document.createElement(&quot;img&quot;);b.src=a;m.google_image_requests.push(b)},n=function(){return&quot;undefined&quot;!==typeof l.hidden?l.hidden:&quot;undefined&quot;!==typeof l.mozHidden?l.mozHidden:&quot;undefined&quot;!==typeof l.msHidden?l.msHidden:&quot;undefined&quot;!==typeof l.webkitHidden?l.webkitHidden:!1};var r=function(a,b,c,g){return a?new q(a.getEscapedGwsQueryId(),a.getEscapedQemQueryId(),b,c,g):null},t=[&quot;wfocusinit&quot;],u=this;t[0]in u||!u.execScript||u.execScript(&quot;var &quot;+t[0]);for(var v;t.length&amp;&amp;(v=t.shift());){var x;if(x=!t.length)x=void 0!==r;x?u[v]=r:u=u[v]?u[v]:u[v]={}};})();wfocusinit(adSlot,false,false,false);</script>  </body></html>{&quot;uid&quot;:1,&quot;hostPeerName&quot;:&quot;https://www.scribd.com&quot;,&quot;initialGeometry&quot;:&quot;{\&quot;windowCoords_t\&quot;:21,\&quot;windowCoords_r\&quot;:1366,\&quot;windowCoords_b\&quot;:726,\&quot;windowCoords_l\&quot;:0,\&quot;frameCoords_t\&quot;:2235,\&quot;frameCoords_r\&quot;:890,\&quot;frameCoords_b\&quot;:2325,\&quot;frameCoords_l\&quot;:162,\&quot;styleZIndex\&quot;:\&quot;auto\&quot;,\&quot;allowedExpansion_t\&quot;:0,\&quot;allowedExpansion_r\&quot;:0,\&quot;allowedExpansion_b\&quot;:0,\&quot;allowedExpansion_l\&quot;:0,\&quot;xInView\&quot;:0,\&quot;yInView\&quot;:0}&quot;,&quot;permissions&quot;:&quot;{\&quot;expandByOverlay\&quot;:true,\&quot;expandByPush\&quot;:false,\&quot;readCookie\&quot;:false,\&quot;writeCookie\&quot;:false}&quot;,&quot;metadata&quot;:&quot;{\&quot;shared\&quot;:{\&quot;sf_ver\&quot;:\&quot;1-0-1\&quot;,\&quot;ck_on\&quot;:1,\&quot;flash_ver\&quot;:\&quot;16.0.0\&quot;}}&quot;}" scrolling="no" marginwidth="0" marginheight="0" width="728" height="90" data-is-safeframe="true" style="border: 0px; vertical-align: bottom;"></iframe></div><iframe id="google_ads_iframe_/1024966/Doc_Between_Leaderboard_BTF_728x90_2_0__hidden__" name="google_ads_iframe_/1024966/Doc_Between_Leaderboard_BTF_728x90_2_0__hidden__" width="0" height="0" scrolling="no" marginwidth="0" marginheight="0" frameborder="0" src="javascript:&quot;<html><body style='background:transparent'></body></html>&quot;" style="border: 0px; vertical-align: bottom; visibility: hidden; display: none;"></iframe></div>
    </div>




  <div class="outer_page only_ie6_border  not_visible" id="outer_page_3" style="width: 1270px; height: 982px;">
      <div class="newpage" id="page3" style="width: 1167px; height: 902px; -webkit-transform: scale(0.7617823479006); -webkit-transform-origin: 0% 0%; display: none;">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/3-45daa1ffed.jpg">
</div>
</div>
</div>



  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  </div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 3};

        pageParams.containerElem = document.getElementById("outer_page_3");
          pageParams.innerPageElem = document.getElementById("page3");
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_3" class="between_page_ads is_filled" style="display: block; height: 90px;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(3);
      </script><div id="between_page_ads_inner_3" style="position: absolute; width: 728px; height: 90px;"><div id="google_ads_iframe_/1024966/Doc_Between_Leaderboard_BTF_728x90_3_0__container__" style="border: 0pt none;"><iframe id="google_ads_iframe_/1024966/Doc_Between_Leaderboard_BTF_728x90_3_0" name="google_ads_iframe_/1024966/Doc_Between_Leaderboard_BTF_728x90_3_0" width="728" height="90" scrolling="no" marginwidth="0" marginheight="0" frameborder="0" src="javascript:&quot;<html><body style='background:transparent'></body></html>&quot;" style="border: 0px; vertical-align: bottom;"></iframe></div><iframe id="google_ads_iframe_/1024966/Doc_Between_Leaderboard_BTF_728x90_3_0__hidden__" name="google_ads_iframe_/1024966/Doc_Between_Leaderboard_BTF_728x90_3_0__hidden__" width="0" height="0" scrolling="no" marginwidth="0" marginheight="0" frameborder="0" src="javascript:&quot;<html><body style='background:transparent'></body></html>&quot;" style="border: 0px; vertical-align: bottom; visibility: hidden; display: none;"></iframe></div>
    </div>




  <div class="outer_page only_ie6_border   not_visible" id="outer_page_4" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="-webkit-transform: scale(0.7617823479006); -webkit-transform-origin: 0% 0%; display: none;"><div class="newpage" id="page4" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/4-fbfe135b80.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 4};

        pageParams.containerElem = document.getElementById("outer_page_4");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/4-fbfe135b80.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_4" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(4);
      </script>
    </div>




  <div class="outer_page only_ie6_border    not_visible" id="outer_page_5" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(0.7617823479006); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page5" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/5-5bba4b96c4.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 5};

        pageParams.containerElem = document.getElementById("outer_page_5");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/5-5bba4b96c4.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_5" class="between_page_ads is_filled" style="display: block; height: 90px;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(5);
      </script><div id="between_page_ads_inner_5" style="position: absolute; width: 728px; height: 90px;"><div id="google_ads_iframe_/1024966/Doc_Between_Leaderboard_BTF_728x90_5_0__container__" style="border: 0pt none;"><iframe id="google_ads_iframe_/1024966/Doc_Between_Leaderboard_BTF_728x90_5_0" name="google_ads_iframe_/1024966/Doc_Between_Leaderboard_BTF_728x90_5_0" width="728" height="90" scrolling="no" marginwidth="0" marginheight="0" frameborder="0" src="javascript:&quot;<html><body style='background:transparent'></body></html>&quot;" style="border: 0px; vertical-align: bottom;"></iframe></div><iframe id="google_ads_iframe_/1024966/Doc_Between_Leaderboard_BTF_728x90_5_0__hidden__" name="google_ads_iframe_/1024966/Doc_Between_Leaderboard_BTF_728x90_5_0__hidden__" width="0" height="0" scrolling="no" marginwidth="0" marginheight="0" frameborder="0" src="javascript:&quot;<html><body style='background:transparent'></body></html>&quot;" style="border: 0px; vertical-align: bottom; visibility: hidden; display: none;"></iframe></div>
    </div>




  <div class="outer_page only_ie6_border    not_visible" id="outer_page_6" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(0.7617823479006); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page6" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/6-ac3d44fceb.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 6};

        pageParams.containerElem = document.getElementById("outer_page_6");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/6-ac3d44fceb.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_6" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(6);
      </script>
    </div>




  <div class="outer_page only_ie6_border    not_visible" id="outer_page_7" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(0.7617823479006); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page7" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/7-54c55286cb.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 7};

        pageParams.containerElem = document.getElementById("outer_page_7");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/7-54c55286cb.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_7" class="between_page_ads is_filled" style="display: block; height: 90px;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(7);
      </script><div id="between_page_ads_inner_7" style="position: absolute; width: 728px; height: 90px;"><div id="google_ads_iframe_/1024966/Doc_Between_Leaderboard_BTF_728x90_7_0__container__" style="border: 0pt none;"><iframe id="google_ads_iframe_/1024966/Doc_Between_Leaderboard_BTF_728x90_7_0" name="google_ads_iframe_/1024966/Doc_Between_Leaderboard_BTF_728x90_7_0" width="728" height="90" scrolling="no" marginwidth="0" marginheight="0" frameborder="0" src="javascript:&quot;<html><body style='background:transparent'></body></html>&quot;" style="border: 0px; vertical-align: bottom;"></iframe></div><iframe id="google_ads_iframe_/1024966/Doc_Between_Leaderboard_BTF_728x90_7_0__hidden__" name="google_ads_iframe_/1024966/Doc_Between_Leaderboard_BTF_728x90_7_0__hidden__" width="0" height="0" scrolling="no" marginwidth="0" marginheight="0" frameborder="0" src="javascript:&quot;<html><body style='background:transparent'></body></html>&quot;" style="border: 0px; vertical-align: bottom; visibility: hidden; display: none;"></iframe></div>
    </div>




  <div class="outer_page only_ie6_border    not_visible" id="outer_page_8" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(0.7617823479006); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page8" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/8-ffdd67af05.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 8};

        pageParams.containerElem = document.getElementById("outer_page_8");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/8-ffdd67af05.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_8" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(8);
      </script>
    </div>




  <div class="outer_page only_ie6_border    not_visible" id="outer_page_9" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(0.7617823479006); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page9" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/9-1e09ddaf81.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 9};

        pageParams.containerElem = document.getElementById("outer_page_9");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/9-1e09ddaf81.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_9" class="between_page_ads is_filled" style="display: block; height: 90px;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(9);
      </script><div id="between_page_ads_inner_9" style="position: absolute; width: 728px; height: 90px;"><div id="google_ads_iframe_/1024966/Doc_Between_Leaderboard_BTF_728x90_9_0__container__" style="border: 0pt none;"><iframe id="google_ads_iframe_/1024966/Doc_Between_Leaderboard_BTF_728x90_9_0" name="google_ads_iframe_/1024966/Doc_Between_Leaderboard_BTF_728x90_9_0" width="728" height="90" scrolling="no" marginwidth="0" marginheight="0" frameborder="0" src="javascript:&quot;<html><body style='background:transparent'></body></html>&quot;" style="border: 0px; vertical-align: bottom;"></iframe></div><iframe id="google_ads_iframe_/1024966/Doc_Between_Leaderboard_BTF_728x90_9_0__hidden__" name="google_ads_iframe_/1024966/Doc_Between_Leaderboard_BTF_728x90_9_0__hidden__" width="0" height="0" scrolling="no" marginwidth="0" marginheight="0" frameborder="0" src="javascript:&quot;<html><body style='background:transparent'></body></html>&quot;" style="border: 0px; vertical-align: bottom; visibility: hidden; display: none;"></iframe></div>
    </div>




  <div class="outer_page only_ie6_border   not_visible" id="outer_page_10" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(0.7617823479006); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page10" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/10-3fda455369.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 10};

        pageParams.containerElem = document.getElementById("outer_page_10");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/10-3fda455369.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_10" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(10);
      </script>
    </div>




  <div class="outer_page only_ie6_border    not_visible" id="outer_page_11" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(0.7617823479006); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page11" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/11-3273dc614e.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 11};

        pageParams.containerElem = document.getElementById("outer_page_11");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/11-3273dc614e.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_11" class="between_page_ads is_filled" style="display: block; height: 90px;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(11);
      </script><div id="between_page_ads_inner_11" style="position: absolute; width: 728px; height: 90px;"><div id="google_ads_iframe_/1024966/Doc_Between_Leaderboard_BTF_728x90_11_0__container__" style="border: 0pt none;"><iframe id="google_ads_iframe_/1024966/Doc_Between_Leaderboard_BTF_728x90_11_0" name="google_ads_iframe_/1024966/Doc_Between_Leaderboard_BTF_728x90_11_0" width="728" height="90" scrolling="no" marginwidth="0" marginheight="0" frameborder="0" src="javascript:&quot;<html><body style='background:transparent'></body></html>&quot;" style="border: 0px; vertical-align: bottom;"></iframe></div><iframe id="google_ads_iframe_/1024966/Doc_Between_Leaderboard_BTF_728x90_11_0__hidden__" name="google_ads_iframe_/1024966/Doc_Between_Leaderboard_BTF_728x90_11_0__hidden__" width="0" height="0" scrolling="no" marginwidth="0" marginheight="0" frameborder="0" src="javascript:&quot;<html><body style='background:transparent'></body></html>&quot;" style="border: 0px; vertical-align: bottom; visibility: hidden; display: none;"></iframe></div>
    </div>




  <div class="outer_page only_ie6_border    not_visible" id="outer_page_12" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(0.7617823479006); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page12" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/12-7ef6c2442e.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 12};

        pageParams.containerElem = document.getElementById("outer_page_12");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/12-7ef6c2442e.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_12" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(12);
      </script>
    </div>




  <div class="outer_page only_ie6_border    not_visible" id="outer_page_13" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(0.7617823479006); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page13" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/13-68d161d449.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 13};

        pageParams.containerElem = document.getElementById("outer_page_13");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/13-68d161d449.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_13" class="between_page_ads is_filled" style="display: block; height: 90px;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(13);
      </script><div id="between_page_ads_inner_13" style="position: absolute; width: 728px; height: 90px;"><div id="google_ads_iframe_/1024966/Doc_Between_Leaderboard_BTF_728x90_13_0__container__" style="border: 0pt none;"><iframe id="google_ads_iframe_/1024966/Doc_Between_Leaderboard_BTF_728x90_13_0" name="google_ads_iframe_/1024966/Doc_Between_Leaderboard_BTF_728x90_13_0" width="728" height="90" scrolling="no" marginwidth="0" marginheight="0" frameborder="0" src="javascript:&quot;<html><body style='background:transparent'></body></html>&quot;" style="border: 0px; vertical-align: bottom;"></iframe></div><iframe id="google_ads_iframe_/1024966/Doc_Between_Leaderboard_BTF_728x90_13_0__hidden__" name="google_ads_iframe_/1024966/Doc_Between_Leaderboard_BTF_728x90_13_0__hidden__" width="0" height="0" scrolling="no" marginwidth="0" marginheight="0" frameborder="0" src="javascript:&quot;<html><body style='background:transparent'></body></html>&quot;" style="border: 0px; vertical-align: bottom; visibility: hidden; display: none;"></iframe></div>
    </div>




  <div class="outer_page only_ie6_border    not_visible" id="outer_page_14" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(0.7617823479006); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page14" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/14-d347cfb065.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 14};

        pageParams.containerElem = document.getElementById("outer_page_14");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/14-d347cfb065.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_14" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(14);
      </script>
    </div>




  <div class="outer_page only_ie6_border     not_visible" id="outer_page_15" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(0.7617823479006); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page15" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/15-ef2cb3b801.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 15};

        pageParams.containerElem = document.getElementById("outer_page_15");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/15-ef2cb3b801.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_15" class="between_page_ads is_filled" style="display: block; height: 90px;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(15);
      </script><div id="between_page_ads_inner_15" style="position: absolute; width: 728px; height: 90px;"><div id="google_ads_iframe_/1024966/Doc_Between_Leaderboard_BTF_728x90_15_0__container__" style="border: 0pt none;"><iframe id="google_ads_iframe_/1024966/Doc_Between_Leaderboard_BTF_728x90_15_0" name="google_ads_iframe_/1024966/Doc_Between_Leaderboard_BTF_728x90_15_0" width="728" height="90" scrolling="no" marginwidth="0" marginheight="0" frameborder="0" src="javascript:&quot;<html><body style='background:transparent'></body></html>&quot;" style="border: 0px; vertical-align: bottom;"></iframe></div><iframe id="google_ads_iframe_/1024966/Doc_Between_Leaderboard_BTF_728x90_15_0__hidden__" name="google_ads_iframe_/1024966/Doc_Between_Leaderboard_BTF_728x90_15_0__hidden__" width="0" height="0" scrolling="no" marginwidth="0" marginheight="0" frameborder="0" src="javascript:&quot;<html><body style='background:transparent'></body></html>&quot;" style="border: 0px; vertical-align: bottom; visibility: hidden; display: none;"></iframe></div>
    </div>




  <div class="outer_page only_ie6_border     not_visible" id="outer_page_16" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(0.7617823479006); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page16" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/16-60ff9521b6.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 16};

        pageParams.containerElem = document.getElementById("outer_page_16");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/16-60ff9521b6.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_16" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(16);
      </script>
    </div>




  <div class="outer_page only_ie6_border     not_visible" id="outer_page_17" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(0.7617823479006); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page17" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/17-3ba0f37928.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 17};

        pageParams.containerElem = document.getElementById("outer_page_17");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/17-3ba0f37928.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_17" class="between_page_ads is_filled" style="display: block; height: 90px;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(17);
      </script><div id="between_page_ads_inner_17" style="position: absolute; width: 728px; height: 90px;"><div id="google_ads_iframe_/1024966/Doc_Between_Leaderboard_BTF_728x90_17_0__container__" style="border: 0pt none;"><iframe id="google_ads_iframe_/1024966/Doc_Between_Leaderboard_BTF_728x90_17_0" name="google_ads_iframe_/1024966/Doc_Between_Leaderboard_BTF_728x90_17_0" width="728" height="90" scrolling="no" marginwidth="0" marginheight="0" frameborder="0" src="javascript:&quot;<html><body style='background:transparent'></body></html>&quot;" style="border: 0px; vertical-align: bottom;"></iframe></div><iframe id="google_ads_iframe_/1024966/Doc_Between_Leaderboard_BTF_728x90_17_0__hidden__" name="google_ads_iframe_/1024966/Doc_Between_Leaderboard_BTF_728x90_17_0__hidden__" width="0" height="0" scrolling="no" marginwidth="0" marginheight="0" frameborder="0" src="javascript:&quot;<html><body style='background:transparent'></body></html>&quot;" style="border: 0px; vertical-align: bottom; visibility: hidden; display: none;"></iframe></div>
    </div>




  <div class="outer_page only_ie6_border     not_visible" id="outer_page_18" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(0.7617823479006); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page18" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/18-8ffadee1b3.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 18};

        pageParams.containerElem = document.getElementById("outer_page_18");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/18-8ffadee1b3.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_18" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(18);
      </script>
    </div>




  <div class="outer_page only_ie6_border      not_visible" id="outer_page_19" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="-webkit-transform: scale(0.7617823479006); -webkit-transform-origin: 0% 0%; display: none;"><div class="newpage" id="page19" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/19-de6148b1fa.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 19};

        pageParams.containerElem = document.getElementById("outer_page_19");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/19-de6148b1fa.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_19" class="between_page_ads is_filled" style="display: block; height: 90px;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(19);
      </script><div id="between_page_ads_inner_19" style="position: absolute; width: 728px; height: 90px;"><div id="google_ads_iframe_/1024966/Doc_Between_Leaderboard_BTF_728x90_19_0__container__" style="border: 0pt none; display: inline-block; width: 728px; height: 90px;"><iframe frameborder="0" src="https://tpc.googlesyndication.com/safeframe/1-0-1/html/container.html#xpc=sf-gdn-exp-2&amp;p=https%3A//www.scribd.com" id="google_ads_iframe_/1024966/Doc_Between_Leaderboard_BTF_728x90_19_0" name="1-0-1;61269;<!doctype html><html><head><style><!--
a:link { color: #000000 }a:visited { color: #000000 }a:hover { color: #000000 }a:active { color: #000000 }  --></style><script><!--
(function(){var d=this,f=function(a){var b=typeof a;if(&quot;object&quot;==b)if(a){if(a instanceof Array)return&quot;array&quot;;if(a instanceof Object)return b;var c=Object.prototype.toString.call(a);if(&quot;[object Window]&quot;==c)return&quot;object&quot;;if(&quot;[object Array]&quot;==c||&quot;number&quot;==typeof a.length&amp;&amp;&quot;undefined&quot;!=typeof a.splice&amp;&amp;&quot;undefined&quot;!=typeof a.propertyIsEnumerable&amp;&amp;!a.propertyIsEnumerable(&quot;splice&quot;))return&quot;array&quot;;if(&quot;[object Function]&quot;==c||&quot;undefined&quot;!=typeof a.call&amp;&amp;&quot;undefined&quot;!=typeof a.propertyIsEnumerable&amp;&amp;!a.propertyIsEnumerable(&quot;call&quot;))return&quot;function&quot;}else return&quot;null&quot;;else if(&quot;function&quot;==b&amp;&amp;&quot;undefined&quot;==typeof a.call)return&quot;object&quot;;return b};var g;e:{var h=d.navigator;if(h){var k=h.userAgent;if(k){g=k;break e}}g=&quot;&quot;};var l=-1!=g.indexOf(&quot;Opera&quot;)||-1!=g.indexOf(&quot;OPR&quot;),n=-1!=g.indexOf(&quot;Trident&quot;)||-1!=g.indexOf(&quot;MSIE&quot;),p=-1!=g.indexOf(&quot;Gecko&quot;)&amp;&amp;-1==g.toLowerCase().indexOf(&quot;webkit&quot;)&amp;&amp;!(-1!=g.indexOf(&quot;Trident&quot;)||-1!=g.indexOf(&quot;MSIE&quot;)),q=-1!=g.toLowerCase().indexOf(&quot;webkit&quot;);(function(){var a=&quot;&quot;,b;if(l&amp;&amp;d.opera)return a=d.opera.version,&quot;function&quot;==f(a)?a():a;p?b=/rv\:([^\);]+)(\)|;)/:n?b=/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/:q&amp;&amp;(b=/WebKit\/(\S+)/);b&amp;&amp;(a=(a=b.exec(g))?a[1]:&quot;&quot;);return n&amp;&amp;(b=(b=d.document)?b.documentMode:void 0,b>parseFloat(a))?String(b):a})();var r={};window.ss=function(a){void 0!==r[a]?r[a]++:r[a]=1;var b=document.getElementById(a),c=r[a];if(window.css)css(a,&quot;nm&quot;,c,void 0,void 0);else if(b){a=b.href;var e=a.indexOf(&quot;&amp;nm=&quot;);if(0>e)c=a+&quot;&amp;nm=&quot;+c;else var e=e+4,m=a.indexOf(&quot;&amp;&quot;,e),c=0<=m?a.substring(0,e)+c+a.substring(m):a.substring(0,e)+c;b.href=2E3<c.length?a:c}};})();function su(id) {var a = document.getElementById(id);var b = (new Date()).getTime();if (a &amp;&amp; a.myt &amp;&amp; b) {var t = b - a.myt;if (window.css) {css(id,'clkt',t);return;}var bi = a.href.indexOf(&quot;&amp;clkt=&quot;);if (bi > 0) {var c = a.href.substring(0, bi+6); var d = a.href.substring(bi+6, a.href.length);var ei = d.indexOf(&quot;&amp;&quot;);var r = '';if (ei >= 0)r = d.substring(ei, d.length);a.href = c + t + r; } else {a.href += &quot;&amp;clkt=&quot; + t;}}}(function(){var d=this,g=function(a){var b=typeof a;if(&quot;object&quot;==b)if(a){if(a instanceof Array)return&quot;array&quot;;if(a instanceof Object)return b;var c=Object.prototype.toString.call(a);if(&quot;[object Window]&quot;==c)return&quot;object&quot;;if(&quot;[object Array]&quot;==c||&quot;number&quot;==typeof a.length&amp;&amp;&quot;undefined&quot;!=typeof a.splice&amp;&amp;&quot;undefined&quot;!=typeof a.propertyIsEnumerable&amp;&amp;!a.propertyIsEnumerable(&quot;splice&quot;))return&quot;array&quot;;if(&quot;[object Function]&quot;==c||&quot;undefined&quot;!=typeof a.call&amp;&amp;&quot;undefined&quot;!=typeof a.propertyIsEnumerable&amp;&amp;!a.propertyIsEnumerable(&quot;call&quot;))return&quot;function&quot;}else return&quot;null&quot;;else if(&quot;function&quot;==b&amp;&amp;&quot;undefined&quot;==typeof a.call)return&quot;object&quot;;return b};var h;e:{var k=d.navigator;if(k){var l=k.userAgent;if(l){h=l;break e}}h=&quot;&quot;};var m=-1!=h.indexOf(&quot;Opera&quot;)||-1!=h.indexOf(&quot;OPR&quot;),n=-1!=h.indexOf(&quot;Trident&quot;)||-1!=h.indexOf(&quot;MSIE&quot;),p=-1!=h.indexOf(&quot;Gecko&quot;)&amp;&amp;-1==h.toLowerCase().indexOf(&quot;webkit&quot;)&amp;&amp;!(-1!=h.indexOf(&quot;Trident&quot;)||-1!=h.indexOf(&quot;MSIE&quot;)),q=-1!=h.toLowerCase().indexOf(&quot;webkit&quot;);(function(){var a=&quot;&quot;,b;if(m&amp;&amp;d.opera)return a=d.opera.version,&quot;function&quot;==g(a)?a():a;p?b=/rv\:([^\);]+)(\)|;)/:n?b=/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/:q&amp;&amp;(b=/WebKit\/(\S+)/);b&amp;&amp;(a=(a=b.exec(h))?a[1]:&quot;&quot;);return n&amp;&amp;(b=(b=d.document)?b.documentMode:void 0,b>parseFloat(a))?String(b):a})();var r=function(a,b,c,e){if(window.css)css(b,c,e,void 0,void 0);else if(a){b=a.href;var f=&quot;&amp;&quot;+c+&quot;=&quot;;c=b.indexOf(f);0>c?e=b+f+e:(c+=f.length,f=b.indexOf(&quot;&amp;&quot;,c),e=0<=f?b.substring(0,c)+e+b.substring(f):b.substring(0,c)+e);a.href=2E3<e.length?b:e}};var t=null,u=function(a){t=a};document.addEventListener&amp;&amp;document.addEventListener(&quot;mousedown&quot;,u,!0);window.xy=function(a,b,c){c=c||b;if((a=a||t)&amp;&amp;b&amp;&amp;c){var e=Math.round(a.clientY-c.offsetTop),f=b.id;r(b,f,&quot;nx&quot;,Math.round(a.clientX-c.offsetLeft));r(b,f,&quot;ny&quot;,e)}};})();(function(){var d=this,f=function(a){var b=typeof a;if(&quot;object&quot;==b)if(a){if(a instanceof Array)return&quot;array&quot;;if(a instanceof Object)return b;var c=Object.prototype.toString.call(a);if(&quot;[object Window]&quot;==c)return&quot;object&quot;;if(&quot;[object Array]&quot;==c||&quot;number&quot;==typeof a.length&amp;&amp;&quot;undefined&quot;!=typeof a.splice&amp;&amp;&quot;undefined&quot;!=typeof a.propertyIsEnumerable&amp;&amp;!a.propertyIsEnumerable(&quot;splice&quot;))return&quot;array&quot;;if(&quot;[object Function]&quot;==c||&quot;undefined&quot;!=typeof a.call&amp;&amp;&quot;undefined&quot;!=typeof a.propertyIsEnumerable&amp;&amp;!a.propertyIsEnumerable(&quot;call&quot;))return&quot;function&quot;}else return&quot;null&quot;;else if(&quot;function&quot;==b&amp;&amp;&quot;undefined&quot;==typeof a.call)return&quot;object&quot;;return b};var g;e:{var h=d.navigator;if(h){var k=h.userAgent;if(k){g=k;break e}}g=&quot;&quot;};var l=-1!=g.indexOf(&quot;Opera&quot;)||-1!=g.indexOf(&quot;OPR&quot;),n=-1!=g.indexOf(&quot;Trident&quot;)||-1!=g.indexOf(&quot;MSIE&quot;),p=-1!=g.indexOf(&quot;Gecko&quot;)&amp;&amp;-1==g.toLowerCase().indexOf(&quot;webkit&quot;)&amp;&amp;!(-1!=g.indexOf(&quot;Trident&quot;)||-1!=g.indexOf(&quot;MSIE&quot;)),q=-1!=g.toLowerCase().indexOf(&quot;webkit&quot;);(function(){var a=&quot;&quot;,b;if(l&amp;&amp;d.opera)return a=d.opera.version,&quot;function&quot;==f(a)?a():a;p?b=/rv\:([^\);]+)(\)|;)/:n?b=/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/:q&amp;&amp;(b=/WebKit\/(\S+)/);b&amp;&amp;(a=(a=b.exec(g))?a[1]:&quot;&quot;);return n&amp;&amp;(b=(b=d.document)?b.documentMode:void 0,b>parseFloat(a))?String(b):a})();var r=[0,2,1],t=null;document.addEventListener&amp;&amp;document.addEventListener(&quot;mousedown&quot;,function(a){t=a},!0);window.mb=function(a){if(a){var b=window.event||t;if(b){var c;(c=b.which?1<<r[b.which-1]:b.button)&amp;&amp;b.shiftKey&amp;&amp;(c|=8);c&amp;&amp;b.altKey&amp;&amp;(c|=16);c&amp;&amp;b.ctrlKey&amp;&amp;(c|=32);if(c)if(window.css)css(a.id,&quot;mb&quot;,c,void 0,void 0);else if(a){var b=a.href,e=b.indexOf(&quot;&amp;mb=&quot;);if(0>e)c=b+&quot;&amp;mb=&quot;+c;else{var e=e+4,m=b.indexOf(&quot;&amp;&quot;,e);c=0<=m?b.substring(0,e)+c+b.substring(m):b.substring(0,e)+c}a.href=2E3<c.length?b:c}}}};})();(function(){var c=function(a,e,h){var b=document;b.addEventListener?b.addEventListener(a,e,h||!1):b.attachEvent&amp;&amp;b.attachEvent(&quot;on&quot;+a,e)};var d,f=!1,g=!1;c(&quot;mousedown&quot;,function(){f=!0});c(&quot;keydown&quot;,function(){g=!0});document.addEventListener&amp;&amp;c(&quot;click&quot;,function(a){d=a},!0);window.accbk=function(){var a=d?d:window.event;return a?f||g?!1:(a.preventDefault?a.preventDefault():a.returnValue=!1,!0):!1};})();function st(id) {var a = document.getElementById(id);if (a) {a.myt = (new Date()).getTime();xy(window.event, a, document.body);mb(a);}}function ha(a,x){  if (accbk()) return;su(a);}function ca(a) {su(a);top.location.href=document.getElementById(a).href;}function ia(a,e,x) {if (accbk()) return;su(a);}function ga(o,e,x) {if (document.getElementById) {var a=o.id.substring(1),p=&quot;&quot;,r=&quot;&quot;,g=e.target,t,f,h;if (g) {t=g.id;f=g.parentNode;if (f) {p=f.id;h=f.parentNode;if (h)r=h.id;}} else {h=e.srcElement;f=h.parentNode;if (f)p=f.id;t=h.id;}if (t==a||p==a||r==a)return true;ia(a,e,x);top.location.href=document.getElementById(a).href;}}
//-->
</script></head><body leftMargin=&quot;0&quot; topMargin=&quot;0&quot; marginwidth=&quot;0&quot; marginheight=&quot;0&quot; style=&quot;background:transparent&quot; ><div id=&quot;google_image_div&quot; style=&quot;height: 90px; width: 728px; overflow:hidden; position:absolute&quot;><a id=&quot;aw0&quot; target=&quot;_top&quot; href=&quot;http://www.googleadservices.com/pagead/aclk?sa=L&amp;ai=CWrJ5hYG2VK7-MJa18gXbwYKQApnz6oMGgdm6lvIBh-CivcABEAEg7PzvGmDhtLqFkBqgAcerytoDyAEC4AIAqAMByAOZBKoErgFP0Ba9cJ2PZ-Ur_-thimaodKTT23UMSIiXxUN_QcPyxlCJvo7uEuiiQWalKde4HZBGOAD-76HZ4ivrWoI4awzNTGdzdmJBBF-SCh6zmPwHfnHFHeHBOFDZG1KUHTq9rp8dYslDdlpWexi8lKLpzUBVC_v74P8XuMgSWXHPZHF6Z26IQbfXcPFcj9BPOftbJulzqspLvSDZTD-eoM6wb1wwxDW3E5YGjjKRQuIOxS7gBAGIBgGgBgKAB6HUtSU&amp;num=1&amp;cid=5GjkhX6xw_0lv3sFRb0vpW3D&amp;sig=AOD64_2nzicybPil1bM57jmyRlb_o9vMDQ&amp;client=ca-pub-8799115960791774&amp;adurl=http://www1.smart.com.ph/Prepaid/add-ons/ringback%3Futm_source%3Dgoogle%26utm_medium%3Ddisplay%26utm_campaign%3DPrepaidMyRingback%26utm_content%3Dgeneric&quot;><img src=&quot;https://tpc.googlesyndication.com/simgad/15226728339627555949&quot; border=&quot;0&quot; width=&quot;728&quot; class=&quot;img_ad&quot; onload=&quot;&quot; /></a><style>div,ul,li{margin:0;padding:0;}#abgc{height:15px;position:absolute;right:0px;text-rendering:geometricPrecision;top:0;width:19px;z-index:9010;}#abgb{height:100%;}#abgc img{display:block;}#abgc svg{display:block;}#abgs{display:none;height:100%;}#abgl{text-decoration:none;}</style><div id=abgc><div id=abgb></div><div id=abgs><a id=abgl href=&quot;https://www.google.com/url?ct=abg&amp;amp;q=https://www.google.com/adsense/support/bin/request.py%3Fcontact%3Dabg_afc%26url%3Dhttps://www.scribd.com/doc/90484468/Rizal-by-Austin-Coates%26gl%3DPH%26hl%3Den%26client%3Dca-pub-8799115960791774%26ai0%3DCWrJ5hYG2VK7-MJa18gXbwYKQApnz6oMGgdm6lvIBh-CivcABEAEg7PzvGmDhtLqFkBqgAcerytoDyAEC4AIAqAMByAOZBKoErgFP0Ba9cJ2PZ-Ur_-thimaodKTT23UMSIiXxUN_QcPyxlCJvo7uEuiiQWalKde4HZBGOAD-76HZ4ivrWoI4awzNTGdzdmJBBF-SCh6zmPwHfnHFHeHBOFDZG1KUHTq9rp8dYslDdlpWexi8lKLpzUBVC_v74P8XuMgSWXHPZHF6Z26IQbfXcPFcj9BPOftbJulzqspLvSDZTD-eoM6wb1wwxDW3E5YGjjKRQuIOxS7gBAGIBgGgBgKAB6HUtSU&amp;amp;usg=AFQjCNHlkibEhvuazHkkPhrC2jec__SH5Q&quot; target=_blank></a></div></div><script>var abgp={el:document.getElementById('abgc'),ael:document.getElementById('abgs'),iel:document.getElementById('abgb'),hw:19,sw:77,hh:15,sh:15,himg:'https://tpc.googlesyndication.com'+'/pagead/images/ad_choices_i.png',simg:'https://tpc.googlesyndication.com/pagead/images/ad_choices_en.png',alt:'AdChoices',t:'AdChoices',tw:53,t2:'',t2w:0,tbo:0,att:'adchoices',ff:'img',halign:'right',fe:false,fnb:false,iba:false,uic:false,icd:undefined};</script><script src=&quot;https://tpc.googlesyndication.com/pagead/js/r20150108/r20110914/abg.js&quot;></script></div><script>(function(){var h,k=this,aa=function(a){var b=typeof a;if(&quot;object&quot;==b)if(a){if(a instanceof Array)return&quot;array&quot;;if(a instanceof Object)return b;var c=Object.prototype.toString.call(a);if(&quot;[object Window]&quot;==c)return&quot;object&quot;;if(&quot;[object Array]&quot;==c||&quot;number&quot;==typeof a.length&amp;&amp;&quot;undefined&quot;!=typeof a.splice&amp;&amp;&quot;undefined&quot;!=typeof a.propertyIsEnumerable&amp;&amp;!a.propertyIsEnumerable(&quot;splice&quot;))return&quot;array&quot;;if(&quot;[object Function]&quot;==c||&quot;undefined&quot;!=typeof a.call&amp;&amp;&quot;undefined&quot;!=typeof a.propertyIsEnumerable&amp;&amp;!a.propertyIsEnumerable(&quot;call&quot;))return&quot;function&quot;}else return&quot;null&quot;;else if(&quot;function&quot;==b&amp;&amp;&quot;undefined&quot;==typeof a.call)return&quot;object&quot;;return b},m=function(a){return&quot;string&quot;==typeof a},p=function(a){return&quot;function&quot;==aa(a)},ba=function(a,b,c){return a.call.apply(a.bind,arguments)},da=function(a,b,c){if(!a)throw Error();if(2<arguments.length){var d=Array.prototype.slice.call(arguments,2);return function(){var c=Array.prototype.slice.call(arguments);Array.prototype.unshift.apply(c,d);return a.apply(b,c)}}return function(){return a.apply(b,arguments)}},q=function(a,b,c){q=Function.prototype.bind&amp;&amp;-1!=Function.prototype.bind.toString().indexOf(&quot;native code&quot;)?ba:da;return q.apply(null,arguments)},ea=function(a,b){var c=Array.prototype.slice.call(arguments,1);return function(){var b=c.slice();b.push.apply(b,arguments);return a.apply(this,b)}},r=function(a,b){var c=a.split(&quot;.&quot;),d=k;c[0]in d||!d.execScript||d.execScript(&quot;var &quot;+c[0]);for(var e;c.length&amp;&amp;(e=c.shift());)c.length||void 0===b?d=d[e]?d[e]:d[e]={}:d[e]=b},u=function(a,b){function c(){}c.prototype=b.prototype;a.$a=b.prototype;a.prototype=new c;a.sb=function(a,c,f){for(var g=Array(arguments.length-2),l=2;l<arguments.length;l++)g[l-2]=arguments[l];return b.prototype[c].apply(a,g)}};var fa=String.prototype.trim?function(a){return a.trim()}:function(a){return a.replace(/^[\s\xa0]+|[\s\xa0]+$/g,&quot;&quot;)},v=function(a,b){return-1!=a.indexOf(b)},ja=function(a,b){return a<b?-1:a>b?1:0};var ka=function(a){this.g=a||[]},la=function(a){this.g=a||[]},ma=function(a){this.g=a||[]},w=function(a){a=a.g[3];return null!=a?a:!1};ka.prototype.getEscapedQemQueryId=function(){var a=this.g[6];return null!=a?a:&quot;&quot;};ka.prototype.getEscapedGwsQueryId=function(){var a=this.g[7];return null!=a?a:&quot;&quot;};var na=new la,x=function(a){return(a=a.g[5])?new la(a):na},oa=function(a){a=a.g[4];return null!=a?a:&quot;&quot;};var y=Array.prototype,pa=y.indexOf?function(a,b,c){return y.indexOf.call(a,b,c)}:function(a,b,c){c=null==c?0:0>c?Math.max(0,a.length+c):c;if(m(a))return m(b)&amp;&amp;1==b.length?a.indexOf(b,c):-1;for(;c<a.length;c++)if(c in a&amp;&amp;a[c]===b)return c;return-1},qa=y.forEach?function(a,b,c){y.forEach.call(a,b,c)}:function(a,b,c){for(var d=a.length,e=m(a)?a.split(&quot;&quot;):a,f=0;f<d;f++)f in e&amp;&amp;b.call(c,e[f],f,a)},ra=function(a){return y.concat.apply(y,arguments)},sa=function(a){var b=a.length;if(0<b){for(var c=Array(b),d=0;d<b;d++)c[d]=a[d];return c}return[]};var ta=function(a){ta[&quot; &quot;](a);return a};ta[&quot; &quot;]=function(){};var ua=function(a,b){for(var c in a)b.call(void 0,a[c],c,a)},va=&quot;constructor hasOwnProperty isPrototypeOf propertyIsEnumerable toLocaleString toString valueOf&quot;.split(&quot; &quot;),wa=function(a,b){for(var c,d,e=1;e<arguments.length;e++){d=arguments[e];for(c in d)a[c]=d[c];for(var f=0;f<va.length;f++)c=va[f],Object.prototype.hasOwnProperty.call(d,c)&amp;&amp;(a[c]=d[c])}},xa=function(a){var b=arguments.length;if(1==b&amp;&amp;&quot;array&quot;==aa(arguments[0]))return xa.apply(null,arguments[0]);for(var c={},d=0;d<b;d++)c[arguments[d]]=!0;return c};var z;i:{var ya=k.navigator;if(ya){var za=ya.userAgent;if(za){z=za;break i}}z=&quot;&quot;};var Aa=v(z,&quot;Opera&quot;)||v(z,&quot;OPR&quot;),A=v(z,&quot;Trident&quot;)||v(z,&quot;MSIE&quot;),B=v(z,&quot;Gecko&quot;)&amp;&amp;!v(z.toLowerCase(),&quot;webkit&quot;)&amp;&amp;!(v(z,&quot;Trident&quot;)||v(z,&quot;MSIE&quot;)),C=v(z.toLowerCase(),&quot;webkit&quot;),Ba=v(z,&quot;Android&quot;),Ca=function(){var a=k.document;return a?a.documentMode:void 0},Da=function(){var a=&quot;&quot;,b;if(Aa&amp;&amp;k.opera)return a=k.opera.version,p(a)?a():a;B?b=/rv\:([^\);]+)(\)|;)/:A?b=/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/:C&amp;&amp;(b=/WebKit\/(\S+)/);b&amp;&amp;(a=(a=b.exec(z))?a[1]:&quot;&quot;);return A&amp;&amp;(b=Ca(),b>parseFloat(a))?String(b):a}(),Ea={},D=function(a){var b;if(!(b=Ea[a])){b=0;for(var c=fa(String(Da)).split(&quot;.&quot;),d=fa(String(a)).split(&quot;.&quot;),e=Math.max(c.length,d.length),f=0;0==b&amp;&amp;f<e;f++){var g=c[f]||&quot;&quot;,l=d[f]||&quot;&quot;,n=RegExp(&quot;(\\d*)(\\D*)&quot;,&quot;g&quot;),t=RegExp(&quot;(\\d*)(\\D*)&quot;,&quot;g&quot;);do{var X=n.exec(g)||[&quot;&quot;,&quot;&quot;,&quot;&quot;],Y=t.exec(l)||[&quot;&quot;,&quot;&quot;,&quot;&quot;];if(0==X[0].length&amp;&amp;0==Y[0].length)break;b=ja(0==X[1].length?0:parseInt(X[1],10),0==Y[1].length?0:parseInt(Y[1],10))||ja(0==X[2].length,0==Y[2].length)||ja(X[2],Y[2])}while(0==b)}b=Ea[a]=0<=b}return b},Fa=k.document,Ga=Fa&amp;&amp;A?Ca()||(&quot;CSS1Compat&quot;==Fa.compatMode?parseInt(Da,10):5):void 0;var Ha=!A||A&amp;&amp;9<=Ga,Ia=A&amp;&amp;!D(&quot;9&quot;);!C||D(&quot;528&quot;);B&amp;&amp;D(&quot;1.9b&quot;)||A&amp;&amp;D(&quot;8&quot;)||Aa&amp;&amp;D(&quot;9.5&quot;)||C&amp;&amp;D(&quot;528&quot;);B&amp;&amp;!D(&quot;8&quot;)||A&amp;&amp;D(&quot;9&quot;);var Ja=function(){this.Qa=this.Qa;this.cb=this.cb};Ja.prototype.Qa=!1;var E=function(a,b){this.type=a;this.currentTarget=this.target=b;this.defaultPrevented=this.Q=!1;this.Ga=!0};E.prototype.preventDefault=function(){this.defaultPrevented=!0;this.Ga=!1};var F=function(a,b){E.call(this,a?a.type:&quot;&quot;);this.relatedTarget=this.currentTarget=this.target=null;this.charCode=this.keyCode=this.button=this.screenY=this.screenX=this.clientY=this.clientX=this.offsetY=this.offsetX=0;this.metaKey=this.shiftKey=this.altKey=this.ctrlKey=!1;this.G=this.state=null;if(a){this.G=a;var c=this.type=a.type;this.target=a.target||a.srcElement;this.currentTarget=b;var d=a.relatedTarget;if(d){if(B){var e;i:{try{ta(d.nodeName);e=!0;break i}catch(f){}e=!1}e||(d=null)}}else&quot;mouseover&quot;==c?d=a.fromElement:&quot;mouseout&quot;==c&amp;&amp;(d=a.toElement);this.relatedTarget=d;Object.defineProperties?Object.defineProperties(this,{offsetX:{configurable:!0,enumerable:!0,get:this.Na,set:this.Ya},offsetY:{configurable:!0,enumerable:!0,get:this.Oa,set:this.Za}}):(this.offsetX=this.Na(),this.offsetY=this.Oa());this.clientX=void 0!==a.clientX?a.clientX:a.pageX;this.clientY=void 0!==a.clientY?a.clientY:a.pageY;this.screenX=a.screenX||0;this.screenY=a.screenY||0;this.button=a.button;this.keyCode=a.keyCode||0;this.charCode=a.charCode||(&quot;keypress&quot;==c?a.keyCode:0);this.ctrlKey=a.ctrlKey;this.altKey=a.altKey;this.shiftKey=a.shiftKey;this.metaKey=a.metaKey;this.state=a.state;a.defaultPrevented&amp;&amp;this.preventDefault()}};u(F,E);h=F.prototype;h.preventDefault=function(){F.$a.preventDefault.call(this);var a=this.G;if(a.preventDefault)a.preventDefault();else if(a.returnValue=!1,Ia)try{if(a.ctrlKey||112<=a.keyCode&amp;&amp;123>=a.keyCode)a.keyCode=-1}catch(b){}};h.Na=function(){return C||void 0!==this.G.offsetX?this.G.offsetX:this.G.layerX};h.Ya=function(a){Object.defineProperties(this,{offsetX:{writable:!0,enumerable:!0,configurable:!0,value:a}})};h.Oa=function(){return C||void 0!==this.G.offsetY?this.G.offsetY:this.G.layerY};h.Za=function(a){Object.defineProperties(this,{offsetY:{writable:!0,enumerable:!0,configurable:!0,value:a}})};var G=&quot;closure_listenable_&quot;+(1E6*Math.random()|0),Ka=0;var La=function(a,b,c,d,e){this.K=a;this.aa=null;this.src=b;this.type=c;this.X=!!d;this.Z=e;this.key=++Ka;this.M=this.Y=!1},Ma=function(a){a.M=!0;a.K=null;a.aa=null;a.src=null;a.Z=null};var H=function(a){this.src=a;this.o={};this.ea=0};H.prototype.add=function(a,b,c,d,e){var f=a.toString();a=this.o[f];a||(a=this.o[f]=[],this.ea++);var g=Na(a,b,d,e);-1<g?(b=a[g],c||(b.Y=!1)):(b=new La(b,this.src,f,!!d,e),b.Y=c,a.push(b));return b};H.prototype.remove=function(a,b,c,d){a=a.toString();if(!(a in this.o))return!1;var e=this.o[a];b=Na(e,b,c,d);return-1<b?(Ma(e[b]),y.splice.call(e,b,1),0==e.length&amp;&amp;(delete this.o[a],this.ea--),!0):!1};var Oa=function(a,b){var c=b.type;if(c in a.o){var d=a.o[c],e=pa(d,b),f;(f=0<=e)&amp;&amp;y.splice.call(d,e,1);f&amp;&amp;(Ma(b),0==a.o[c].length&amp;&amp;(delete a.o[c],a.ea--))}};H.prototype.wa=function(a,b,c,d){a=this.o[a.toString()];var e=-1;a&amp;&amp;(e=Na(a,b,c,d));return-1<e?a[e]:null};var Na=function(a,b,c,d){for(var e=0;e<a.length;++e){var f=a[e];if(!f.M&amp;&amp;f.K==b&amp;&amp;f.X==!!c&amp;&amp;f.Z==d)return e}return-1};var Pa=&quot;closure_lm_&quot;+(1E6*Math.random()|0),Qa={},Ra=0,Sa=function(a,b,c,d,e){if(&quot;array&quot;==aa(b))for(var f=0;f<b.length;f++)Sa(a,b[f],c,d,e);else if(c=Ta(c),a&amp;&amp;a[G])a.listen(b,c,d,e);else{if(!b)throw Error(&quot;Invalid event type&quot;);var f=!!d,g=Ua(a);g||(a[Pa]=g=new H(a));c=g.add(b,c,!1,d,e);c.aa||(d=Va(),c.aa=d,d.src=a,d.K=c,a.addEventListener?a.addEventListener(b.toString(),d,f):a.attachEvent(Wa(b.toString()),d),Ra++)}},Va=function(){var a=Xa,b=Ha?function(c){return a.call(b.src,b.K,c)}:function(c){c=a.call(b.src,b.K,c);if(!c)return c};return b},Ya=function(a,b,c,d,e){if(&quot;array&quot;==aa(b))for(var f=0;f<b.length;f++)Ya(a,b[f],c,d,e);else c=Ta(c),a&amp;&amp;a[G]?a.unlisten(b,c,d,e):a&amp;&amp;(a=Ua(a))&amp;&amp;(b=a.wa(b,c,!!d,e))&amp;&amp;Za(b)},Za=function(a){if(&quot;number&quot;!=typeof a&amp;&amp;a&amp;&amp;!a.M){var b=a.src;if(b&amp;&amp;b[G])Oa(b.P,a);else{var c=a.type,d=a.aa;b.removeEventListener?b.removeEventListener(c,d,a.X):b.detachEvent&amp;&amp;b.detachEvent(Wa(c),d);Ra--;(c=Ua(b))?(Oa(c,a),0==c.ea&amp;&amp;(c.src=null,b[Pa]=null)):Ma(a)}}},Wa=function(a){return a in Qa?Qa[a]:Qa[a]=&quot;on&quot;+a},ab=function(a,b,c,d){var e=!0;if(a=Ua(a))if(b=a.o[b.toString()])for(b=b.concat(),a=0;a<b.length;a++){var f=b[a];f&amp;&amp;f.X==c&amp;&amp;!f.M&amp;&amp;(f=$a(f,d),e=e&amp;&amp;!1!==f)}return e},$a=function(a,b){var c=a.K,d=a.Z||a.src;a.Y&amp;&amp;Za(a);return c.call(d,b)},Xa=function(a,b){if(a.M)return!0;if(!Ha){var c;if(!(c=b))i:{c=[&quot;window&quot;,&quot;event&quot;];for(var d=k,e;e=c.shift();)if(null!=d[e])d=d[e];else{c=null;break i}c=d}e=c;c=new F(e,this);d=!0;if(!(0>e.keyCode||void 0!=e.returnValue)){i:{var f=!1;if(0==e.keyCode)try{e.keyCode=-1;break i}catch(g){f=!0}if(f||void 0==e.returnValue)e.returnValue=!0}e=[];for(f=c.currentTarget;f;f=f.parentNode)e.push(f);for(var f=a.type,l=e.length-1;!c.Q&amp;&amp;0<=l;l--){c.currentTarget=e[l];var n=ab(e[l],f,!0,c),d=d&amp;&amp;n}for(l=0;!c.Q&amp;&amp;l<e.length;l++)c.currentTarget=e[l],n=ab(e[l],f,!1,c),d=d&amp;&amp;n}return d}return $a(a,new F(b,this))},Ua=function(a){a=a[Pa];return a instanceof H?a:null},bb=&quot;__closure_events_fn_&quot;+(1E9*Math.random()>>>0),Ta=function(a){if(p(a))return a;a[bb]||(a[bb]=function(b){return a.handleEvent(b)});return a[bb]};var I=function(){Ja.call(this);this.P=new H(this);this.Ua=this;this.Pa=null};u(I,Ja);I.prototype[G]=!0;h=I.prototype;h.addEventListener=function(a,b,c,d){Sa(this,a,b,c,d)};h.removeEventListener=function(a,b,c,d){Ya(this,a,b,c,d)};h.dispatchEvent=function(a){var b,c=this.Pa;if(c)for(b=[];c;c=c.Pa)b.push(c);var c=this.Ua,d=a.type||a;if(m(a))a=new E(a,c);else if(a instanceof E)a.target=a.target||c;else{var e=a;a=new E(d,c);wa(a,e)}var e=!0,f;if(b)for(var g=b.length-1;!a.Q&amp;&amp;0<=g;g--)f=a.currentTarget=b[g],e=J(f,d,!0,a)&amp;&amp;e;a.Q||(f=a.currentTarget=c,e=J(f,d,!0,a)&amp;&amp;e,a.Q||(e=J(f,d,!1,a)&amp;&amp;e));if(b)for(g=0;!a.Q&amp;&amp;g<b.length;g++)f=a.currentTarget=b[g],e=J(f,d,!1,a)&amp;&amp;e;return e};h.listen=function(a,b,c,d){return this.P.add(String(a),b,!1,c,d)};h.unlisten=function(a,b,c,d){return this.P.remove(String(a),b,c,d)};var J=function(a,b,c,d){b=a.P.o[String(b)];if(!b)return!0;b=b.concat();for(var e=!0,f=0;f<b.length;++f){var g=b[f];if(g&amp;&amp;!g.M&amp;&amp;g.X==c){var l=g.K,n=g.Z||g.src;g.Y&amp;&amp;Oa(a.P,g);e=!1!==l.call(n,d)&amp;&amp;e}}return e&amp;&amp;0!=d.Ga};I.prototype.wa=function(a,b,c,d){return this.P.wa(String(a),b,c,d)};var cb=function(a,b,c,d){a.addEventListener?a.addEventListener(b,c,d||!1):a.attachEvent&amp;&amp;a.attachEvent(&quot;on&quot;+b,c)},db=function(a,b,c,d){a.removeEventListener?a.removeEventListener(b,c,d||!1):a.detachEvent&amp;&amp;a.detachEvent(&quot;on&quot;+b,c)};var eb=function(a,b){var c=window;c.google_image_requests||(c.google_image_requests=[]);var d=c.document.createElement(&quot;img&quot;);if(b){var e=function(a){b(a);db(d,&quot;load&quot;,e);db(d,&quot;error&quot;,e)};cb(d,&quot;load&quot;,e);cb(d,&quot;error&quot;,e)}d.src=a;c.google_image_requests.push(d)};var fb=window;var gb=function(a,b,c,d,e,f){var g;if(document.createEvent)g=document.createEvent(&quot;MouseEvents&quot;),g.initMouseEvent(b,!0,!0,null,0,0,0,0,0,d,!1,e,f,c,null);else if(document.createEventObject)g=document.createEventObject(),g.va=&quot;on&quot;+b,g.button=c,g.ctrlKey=d,g.shiftKey=e,g.metaKey=f;else return!1;document.createEvent?a.dispatchEvent(g):a.fireEvent(g.va,g);return!0},ib=function(a){a.preventDefault?a.preventDefault():a.returnValue=!1};var jb=function(a){k.setTimeout(function(){throw a;},0)},kb,lb=function(){var a=k.MessageChannel;&quot;undefined&quot;===typeof a&amp;&amp;&quot;undefined&quot;!==typeof window&amp;&amp;window.postMessage&amp;&amp;window.addEventListener&amp;&amp;(a=function(){var a=document.createElement(&quot;iframe&quot;);a.style.display=&quot;none&quot;;a.src=&quot;&quot;;document.documentElement.appendChild(a);var b=a.contentWindow,a=b.document;a.open();a.write(&quot;&quot;);a.close();var c=&quot;callImmediate&quot;+Math.random(),d=&quot;file:&quot;==b.location.protocol?&quot;*&quot;:b.location.protocol+&quot;//&quot;+b.location.host,a=q(function(a){if((&quot;*&quot;==d||a.origin==d)&amp;&amp;a.data==c)this.port1.onmessage()},this);b.addEventListener(&quot;message&quot;,a,!1);this.port1={};this.port2={postMessage:function(){b.postMessage(c,d)}}});if(&quot;undefined&quot;!==typeof a&amp;&amp;!v(z,&quot;Trident&quot;)&amp;&amp;!v(z,&quot;MSIE&quot;)){var b=new a,c={},d=c;b.port1.onmessage=function(){if(void 0!==c.next){c=c.next;var a=c.Sa;c.Sa=null;a()}};return function(a){d.next={Sa:a};d=d.next;b.port2.postMessage(0)}}return&quot;undefined&quot;!==typeof document&amp;&amp;&quot;onreadystatechange&quot;in document.createElement(&quot;script&quot;)?function(a){var b=document.createElement(&quot;script&quot;);b.onreadystatechange=function(){b.onreadystatechange=null;b.parentNode.removeChild(b);b=null;a();a=null};document.documentElement.appendChild(b)}:function(a){k.setTimeout(a,0)}};var sb=function(a,b){nb||ob();pb||(nb(),pb=!0);qb.push(new rb(a,b))},nb,ob=function(){if(k.Promise&amp;&amp;k.Promise.resolve){var a=k.Promise.resolve();nb=function(){a.then(tb)}}else nb=function(){var a=tb;!p(k.setImmediate)||k.Window&amp;&amp;k.Window.prototype.setImmediate==k.setImmediate?(kb||(kb=lb()),kb(a)):k.setImmediate(a)}},pb=!1,qb=[],tb=function(){for(;qb.length;){var a=qb;qb=[];for(var b=0;b<a.length;b++){var c=a[b];try{c.qb.call(c.scope)}catch(d){jb(d)}}}pb=!1},rb=function(a,b){this.qb=a;this.scope=b};var K=function(a,b){this.C=0;this.Fa=void 0;this.D=this.Ha=null;this.ba=this.sa=!1;try{var c=this;a.call(b,function(a){ub(c,2,a)},function(a){ub(c,3,a)})}catch(d){ub(this,3,d)}},vb=function(a){return new K(function(b,c){a.length||b(void 0);for(var d=0,e;e=a[d];d++)e.then(b,c)})},wb=function(a){return new K(function(b,c){var d=a.length,e=[];if(d)for(var f=function(a,c){d--;e[a]=c;0==d&amp;&amp;b(e)},g=function(a){c(a)},l=0,n;n=a[l];l++)n.then(ea(f,l),g);else b(e)})};K.prototype.then=function(a,b,c){return xb(this,p(a)?a:null,p(b)?b:null,c)};K.prototype.then=K.prototype.then;K.prototype.$goog_Thenable=!0;var zb=function(a,b){a.D&amp;&amp;a.D.length||2!=a.C&amp;&amp;3!=a.C||yb(a);a.D||(a.D=[]);a.D.push(b)},xb=function(a,b,c,d){var e={da:null,Ia:null,Ja:null};e.da=new K(function(a,g){e.Ia=b?function(c){try{var e=b.call(d,c);a(e)}catch(t){g(t)}}:a;e.Ja=c?function(b){try{var e=c.call(d,b);a(e)}catch(t){g(t)}}:g});e.da.Ha=a;zb(a,e);return e.da};K.prototype.La=function(a){this.C=0;ub(this,2,a)};K.prototype.Ma=function(a){this.C=0;ub(this,3,a)};var ub=function(a,b,c){if(0==a.C){if(a==c)b=3,c=new TypeError(&quot;Promise cannot resolve to itself&quot;);else{var d;if(c)try{d=!!c.$goog_Thenable}catch(e){d=!1}else d=!1;if(d){a.C=1;c.then(a.La,a.Ma,a);return}d=typeof c;if(&quot;object&quot;==d&amp;&amp;null!=c||&quot;function&quot;==d)try{var f=c.then;if(p(f)){Ab(a,c,f);return}}catch(g){b=3,c=g}}a.Fa=c;a.C=b;yb(a);3!=b||Bb(a,c)}},Ab=function(a,b,c){a.C=1;var d=!1,e=function(b){d||(d=!0,a.La(b))},f=function(b){d||(d=!0,a.Ma(b))};try{c.call(b,e,f)}catch(g){f(g)}},yb=function(a){a.sa||(a.sa=!0,sb(a.bb,a))};K.prototype.bb=function(){for(;this.D&amp;&amp;this.D.length;){var a=this.D;this.D=[];for(var b=0;b<a.length;b++){var c=a[b],d=this.Fa;if(2==this.C)c.Ia(d);else{if(c.da)for(var e=void 0,e=this;e&amp;&amp;e.ba;e=e.Ha)e.ba=!1;c.Ja(d)}}}this.sa=!1};var Bb=function(a,b){a.ba=!0;sb(function(){a.ba&amp;&amp;Cb.call(null,b)})},Cb=jb;xa(&quot;area base br col command embed hr img input keygen link meta param source track wbr&quot;.split(&quot; &quot;));xa(&quot;action&quot;,&quot;cite&quot;,&quot;data&quot;,&quot;formaction&quot;,&quot;href&quot;,&quot;manifest&quot;,&quot;poster&quot;,&quot;src&quot;);xa(&quot;embed&quot;,&quot;iframe&quot;,&quot;link&quot;,&quot;object&quot;,&quot;script&quot;,&quot;style&quot;,&quot;template&quot;);!B&amp;&amp;!A||A&amp;&amp;A&amp;&amp;9<=Ga||B&amp;&amp;D(&quot;1.9.1&quot;);A&amp;&amp;D(&quot;9&quot;);var Db=function(a,b,c){var d=document;c=c||d;var e=a&amp;&amp;&quot;*&quot;!=a?a.toUpperCase():&quot;&quot;;if(c.querySelectorAll&amp;&amp;c.querySelector&amp;&amp;(e||b))return c.querySelectorAll(e+(b?&quot;.&quot;+b:&quot;&quot;));if(b&amp;&amp;c.getElementsByClassName){a=c.getElementsByClassName(b);if(e){c={};for(var f=d=0,g;g=a[f];f++)e==g.nodeName&amp;&amp;(c[d++]=g);c.length=d;return c}return a}a=c.getElementsByTagName(e||&quot;*&quot;);if(b){c={};for(f=d=0;g=a[f];f++){var e=g.className,l;if(l=&quot;function&quot;==typeof e.split)l=0<=pa(e.split(/\s+/),b);l&amp;&amp;(c[d++]=g)}c.length=d;return c}return a};var Eb=function(a,b,c){var d=&quot;mouseenter_custom&quot;==b,e=L(b);return function(f){f||(f=window.event);if(f.type==e){if(&quot;mouseenter_custom&quot;==b||&quot;mouseleave_custom&quot;==b){var g;if(g=d?f.relatedTarget||f.fromElement:f.relatedTarget||f.toElement)for(var l=0;l<a.length;l++){var n;n=a[l];var t=g;if(n.contains&amp;&amp;1==t.nodeType)n=n==t||n.contains(t);else if(&quot;undefined&quot;!=typeof n.compareDocumentPosition)n=n==t||Boolean(n.compareDocumentPosition(t)&amp;16);else{for(;t&amp;&amp;n!=t;)t=t.parentNode;n=t==n}if(n)return}}c(f)}}},L=function(a){return&quot;mouseenter_custom&quot;==a?&quot;mouseover&quot;:&quot;mouseleave_custom&quot;==a?&quot;mouseout&quot;:a};var Fb=function(a,b,c,d,e){if(e)c=a+(&quot;&amp;&quot;+b+&quot;=&quot;+c);else{var f=&quot;&amp;&quot;+b+&quot;=&quot;,g=a.indexOf(f);0>g?c=a+f+c:(g+=f.length,f=a.indexOf(&quot;&amp;&quot;,g),c=0<=f?a.substring(0,g)+c+a.substring(f):a.substring(0,g)+c)}return 2E3<c.length?void 0!==d?Fb(a,b,d,void 0,e):a:c};var Gb=&quot;StopIteration&quot;in k?k.StopIteration:Error(&quot;StopIteration&quot;),Hb=function(){};Hb.prototype.next=function(){throw Gb;};Hb.prototype.ob=function(){return this};var M=function(a,b){this.t={};this.l=[];this.$=this.k=0;var c=arguments.length;if(1<c){if(c%2)throw Error(&quot;Uneven number of arguments&quot;);for(var d=0;d<c;d+=2)this.set(arguments[d],arguments[d+1])}else if(a){var e;if(a instanceof M)e=a.S(),d=a.L();else{var c=[],f=0;for(e in a)c[f++]=e;e=c;c=[];f=0;for(d in a)c[f++]=a[d];d=c}for(c=0;c<e.length;c++)this.set(e[c],d[c])}};M.prototype.L=function(){Ib(this);for(var a=[],b=0;b<this.l.length;b++)a.push(this.t[this.l[b]]);return a};M.prototype.S=function(){Ib(this);return this.l.concat()};M.prototype.T=function(a){return N(this.t,a)};M.prototype.remove=function(a){return N(this.t,a)?(delete this.t[a],this.k--,this.$++,this.l.length>2*this.k&amp;&amp;Ib(this),!0):!1};var Ib=function(a){if(a.k!=a.l.length){for(var b=0,c=0;b<a.l.length;){var d=a.l[b];N(a.t,d)&amp;&amp;(a.l[c++]=d);b++}a.l.length=c}if(a.k!=a.l.length){for(var e={},c=b=0;b<a.l.length;)d=a.l[b],N(e,d)||(a.l[c++]=d,e[d]=1),b++;a.l.length=c}};h=M.prototype;h.get=function(a,b){return N(this.t,a)?this.t[a]:b};h.set=function(a,b){N(this.t,a)||(this.k++,this.l.push(a),this.$++);this.t[a]=b};h.forEach=function(a,b){for(var c=this.S(),d=0;d<c.length;d++){var e=c[d],f=this.get(e);a.call(b,f,e,this)}};h.clone=function(){return new M(this)};h.ob=function(a){Ib(this);var b=0,c=this.l,d=this.t,e=this.$,f=this,g=new Hb;g.next=function(){for(;;){if(e!=f.$)throw Error(&quot;The map has changed since the iterator was created&quot;);if(b>=c.length)throw Gb;var g=c[b++];return a?g:d[g]}};return g};var N=function(a,b){return Object.prototype.hasOwnProperty.call(a,b)};var Jb=/^(?:([^:/?#.]+):)?(?:\/\/(?:([^/?#]*)@)?([^/#?]*?)(?::([0-9]+))?(?=[/#?]|$))?([^?#]+)?(?:\?([^#]*))?(?:#(.*))?$/,Lb=function(a){if(Kb){Kb=!1;var b=k.location;if(b){var c=b.href;if(c&amp;&amp;(c=(c=Lb(c)[3]||null)?decodeURI(c):c)&amp;&amp;c!=b.hostname)throw Kb=!0,Error();}}return a.match(Jb)},Kb=C;var Mb=function(a,b){var c;if(a instanceof Mb)this.m=void 0!==b?b:a.m,Nb(this,a.F),c=a.J,O(this),this.J=c,Ob(this,a.H),Pb(this,a.N),c=a.s,O(this),this.s=c,Qb(this,a.w.clone()),c=a.I,O(this),this.I=c;else if(a&amp;&amp;(c=Lb(String(a)))){this.m=!!b;Nb(this,c[1]||&quot;&quot;,!0);var d=c[2]||&quot;&quot;;O(this);this.J=P(d);Ob(this,c[3]||&quot;&quot;,!0);Pb(this,c[4]);d=c[5]||&quot;&quot;;O(this);this.s=P(d,!0);Qb(this,c[6]||&quot;&quot;,!0);c=c[7]||&quot;&quot;;O(this);this.I=P(c)}else this.m=!!b,this.w=new Q(null,0,this.m)};h=Mb.prototype;h.F=&quot;&quot;;h.J=&quot;&quot;;h.H=&quot;&quot;;h.N=null;h.s=&quot;&quot;;h.I=&quot;&quot;;h.rb=!1;h.m=!1;h.toString=function(){var a=[],b=this.F;b&amp;&amp;a.push(Rb(b,Sb,!0),&quot;:&quot;);if(b=this.H){a.push(&quot;//&quot;);var c=this.J;c&amp;&amp;a.push(Rb(c,Sb,!0),&quot;@&quot;);a.push(encodeURIComponent(String(b)).replace(/%25([0-9a-fA-F]{2})/g,&quot;%$1&quot;));b=this.N;null!=b&amp;&amp;a.push(&quot;:&quot;,String(b))}if(b=this.s)this.H&amp;&amp;&quot;/&quot;!=b.charAt(0)&amp;&amp;a.push(&quot;/&quot;),a.push(Rb(b,&quot;/&quot;==b.charAt(0)?Tb:Ub,!0));(b=this.w.toString())&amp;&amp;a.push(&quot;?&quot;,b);(b=this.I)&amp;&amp;a.push(&quot;#&quot;,Rb(b,Vb));return a.join(&quot;&quot;)};h.resolve=function(a){var b=this.clone(),c=!!a.F;c?Nb(b,a.F):c=!!a.J;if(c){var d=a.J;O(b);b.J=d}else c=!!a.H;c?Ob(b,a.H):c=null!=a.N;d=a.s;if(c)Pb(b,a.N);else if(c=!!a.s){if(&quot;/&quot;!=d.charAt(0))if(this.H&amp;&amp;!this.s)d=&quot;/&quot;+d;else{var e=b.s.lastIndexOf(&quot;/&quot;);-1!=e&amp;&amp;(d=b.s.substr(0,e+1)+d)}e=d;if(&quot;..&quot;==e||&quot;.&quot;==e)d=&quot;&quot;;else if(v(e,&quot;./&quot;)||v(e,&quot;/.&quot;)){for(var d=0==e.lastIndexOf(&quot;/&quot;,0),e=e.split(&quot;/&quot;),f=[],g=0;g<e.length;){var l=e[g++];&quot;.&quot;==l?d&amp;&amp;g==e.length&amp;&amp;f.push(&quot;&quot;):&quot;..&quot;==l?((1<f.length||1==f.length&amp;&amp;&quot;&quot;!=f[0])&amp;&amp;f.pop(),d&amp;&amp;g==e.length&amp;&amp;f.push(&quot;&quot;)):(f.push(l),d=!0)}d=f.join(&quot;/&quot;)}else d=e}c?(O(b),b.s=d):c=&quot;&quot;!==a.w.toString();c?Qb(b,P(a.w.toString())):c=!!a.I;c&amp;&amp;(a=a.I,O(b),b.I=a);return b};h.clone=function(){return new Mb(this)};var Nb=function(a,b,c){O(a);a.F=c?P(b,!0):b;a.F&amp;&amp;(a.F=a.F.replace(/:$/,&quot;&quot;))},Ob=function(a,b,c){O(a);a.H=c?P(b,!0):b},Pb=function(a,b){O(a);if(b){b=Number(b);if(isNaN(b)||0>b)throw Error(&quot;Bad port number &quot;+b);a.N=b}else a.N=null},Qb=function(a,b,c){O(a);b instanceof Q?(a.w=b,a.w.ua(a.m)):(c||(b=Rb(b,Wb)),a.w=new Q(b,0,a.m))},O=function(a){if(a.rb)throw Error(&quot;Tried to modify a read-only Uri&quot;);};Mb.prototype.ua=function(a){this.m=a;this.w&amp;&amp;this.w.ua(a);return this};var P=function(a,b){return a?b?decodeURI(a):decodeURIComponent(a):&quot;&quot;},Rb=function(a,b,c){return m(a)?(a=encodeURI(a).replace(b,Xb),c&amp;&amp;(a=a.replace(/%25([0-9a-fA-F]{2})/g,&quot;%$1&quot;)),a):null},Xb=function(a){a=a.charCodeAt(0);return&quot;%&quot;+(a>>4&amp;15).toString(16)+(a&amp;15).toString(16)},Sb=/[#\/\?@]/g,Ub=/[\#\?:]/g,Tb=/[\#\?]/g,Wb=/[\#\?@]/g,Vb=/#/g,Q=function(a,b,c){this.n=a||null;this.m=!!c},R=function(a){if(!a.j&amp;&amp;(a.j=new M,a.k=0,a.n)){var b=q(a.add,a);a=a.n.split(&quot;&amp;&quot;);for(var c=0;c<a.length;c++){var d=a[c].indexOf(&quot;=&quot;),e=null,f=null;0<=d?(e=a[c].substring(0,d),f=a[c].substring(d+1)):e=a[c];b(decodeURIComponent(e.replace(/\+/g,&quot; &quot;)),f?decodeURIComponent(f.replace(/\+/g,&quot; &quot;)):&quot;&quot;)}}};h=Q.prototype;h.j=null;h.k=null;h.add=function(a,b){R(this);this.n=null;a=S(this,a);var c=this.j.get(a);c||this.j.set(a,c=[]);c.push(b);this.k++;return this};h.remove=function(a){R(this);a=S(this,a);return this.j.T(a)?(this.n=null,this.k-=this.j.get(a).length,this.j.remove(a)):!1};h.T=function(a){R(this);a=S(this,a);return this.j.T(a)};h.S=function(){R(this);for(var a=this.j.L(),b=this.j.S(),c=[],d=0;d<b.length;d++)for(var e=a[d],f=0;f<e.length;f++)c.push(b[d]);return c};h.L=function(a){R(this);var b=[];if(m(a))this.T(a)&amp;&amp;(b=ra(b,this.j.get(S(this,a))));else{a=this.j.L();for(var c=0;c<a.length;c++)b=ra(b,a[c])}return b};h.set=function(a,b){R(this);this.n=null;a=S(this,a);this.T(a)&amp;&amp;(this.k-=this.j.get(a).length);this.j.set(a,[b]);this.k++;return this};h.get=function(a,b){var c=a?this.L(a):[];return 0<c.length?String(c[0]):b};h.toString=function(){if(this.n)return this.n;if(!this.j)return&quot;&quot;;for(var a=[],b=this.j.S(),c=0;c<b.length;c++)for(var d=b[c],e=encodeURIComponent(String(d)),d=this.L(d),f=0;f<d.length;f++){var g=e;&quot;&quot;!==d[f]&amp;&amp;(g+=&quot;=&quot;+encodeURIComponent(String(d[f])));a.push(g)}return this.n=a.join(&quot;&amp;&quot;)};h.clone=function(){var a=new Q;a.n=this.n;this.j&amp;&amp;(a.j=this.j.clone(),a.k=this.k);return a};var S=function(a,b){var c=String(b);a.m&amp;&amp;(c=c.toLowerCase());return c};Q.prototype.ua=function(a){a&amp;&amp;!this.m&amp;&amp;(R(this),this.n=null,this.j.forEach(function(a,c){var d=c.toLowerCase();c!=d&amp;&amp;(this.remove(c),this.remove(d),0<a.length&amp;&amp;(this.n=null,this.j.set(S(this,d),sa(a)),this.k+=a.length))},this));this.m=a};var Yb;Yb=!1;var T=z;T&amp;&amp;(-1!=T.indexOf(&quot;Firefox&quot;)||-1!=T.indexOf(&quot;Camino&quot;)||-1!=T.indexOf(&quot;iPad&quot;)||-1!=T.indexOf(&quot;iPhone&quot;)||-1!=T.indexOf(&quot;iPod&quot;)||-1!=T.indexOf(&quot;Chrome&quot;)||-1!=T.indexOf(&quot;Android&quot;)&amp;&amp;(Yb=!0));var Zb=Yb;var U={tb:0,la:1,URL:2,ja:3,fa:4,Ba:5,Aa:7,za:8,ya:9,ka:6,ib:10,kb:11,jb:12,gb:13,xa:14,Ra:15,lb:16,nb:17,eb:18,fb:19,ub:1E3};var $b=function(a,b,c,d){b=c(d,b);if(!(b instanceof Array))return a;qa(b,function(b){if(2!==b.length&amp;&amp;3!==b.length)return a;a=Fb(a,b[0],b[1],b[2],!0)});return a},ac=function(a,b,c){if(window.ona){ib(a);a=b.href;i:{if(window.ona){if(c.match(/itunes[.]apple[.]com/)){if(window.onc)window.onc(a),window.ona(c);else window.ona(a);c=!0;break i}c=a;if(c.match(/market[.]android[.]com|play[.]google[.]com/)&amp;&amp;c.match(/[\?&amp;]sa=L/)&amp;&amp;!c.match(/googleadservices[.]com/)){var d=window.location.host;if(d){b=1;for(var e=d.split(&quot;:&quot;),d=[];0<b&amp;&amp;e.length;)d.push(e.shift()),b--;e.length&amp;&amp;d.push(e.join(&quot;:&quot;));b=d[0];d=d[1];c=new Mb(c);Ob(c,b);Pb(c,d);c=c.toString()}c=c.replace(&quot;?&quot;,&quot;?&quot;+encodeURIComponent(&quot;rct&quot;)+&quot;=&quot;+encodeURIComponent(&quot;j&quot;)+&quot;&amp;&quot;);b=new XMLHttpRequest;b.open(&quot;GET&quot;,c,!1);b.send();b.responseText&amp;&amp;(b=b.responseText.match(/URL=\'([^\']*)\'/),1<b.length&amp;&amp;(c=b[1].replace(/&amp;amp;/g,&quot;&amp;&quot;)));c=Zb||Ba?c.replace(/https?:\/\/(market.android.com|play.google.com\/store\/apps)\//,&quot;market://&quot;):c}else c=null;if(c){window.ona(c);c=!0;break i}}c=!1}if(!c)window.ona(a)}};var V=function(a){this.ma=a;this.pa=[];this.W=[];this.na={};this.i={};this.Ca=1;this.O=&quot;data-original-click-url&quot;;this.qa=&quot;data-landing-url&quot;;this.A={};this.ra=!1;this.V=[]};V.prototype.registerBeaconUrlBuilder=function(a){this.W.push(a)};var bc=function(a,b,c){var d=b=b.getAttribute(a.O);if(d)for(var e=0;e<a.pa.length;e++)d=$b(d,b,a.pa[e],c);return d},cc=function(a,b,c,d){if(0!=a.W.length&amp;&amp;(d.preventDefault?!d.defaultPrevented:!1!==d.returnValue)){ib(d);for(var e=[],f=0;f<a.W.length;f++){var g=a.W[f](c);if(g){var l=new K(function(a){eb(g,a)});e.push(l)}}c=wb(e);e=new K(function(a){window.setTimeout(a,2E3)});vb([c,e]).then(q(V.prototype.ab,a,b,d))}};V.prototype.ab=function(a,b){this.ra=!0;var c=!1;b.target&amp;&amp;(c=gb(b.target,&quot;click&quot;,b.button,b.ctrlKey,b.shiftKey,b.metaKey));a.href&amp;&amp;!c&amp;&amp;(fb.top.location=a.href)};V.prototype.Ta=function(a,b,c,d){if(this.ra)this.ra=!1;else{d||(d=window.event);ua(this.i[c][b],function(a){a(d)});var e=bc(this,a,d.type);e&amp;&amp;(this.A[b]?a.ping=e:a.href=e);&quot;click&quot;==c&amp;&amp;cc(this,a,b,d);dc(this);&quot;click&quot;!=c||(d.preventDefault?d.defaultPrevented:!1===d.returnValue)||ac(d,a,oa(this.ma))}};var ec=function(a,b,c,d){a.i[d]||(a.i[d]={});a.i[d][c]||(a.i[d][c]={});a=q(a.Ta,a,b,c,d);cb(b,d,a,void 0)};h=V.prototype;h.U=function(a,b){for(var c=0;c<a.length;c++){var d=a[c];d.setAttribute(this.O,d.href);ec(this,d,b,&quot;mousedown&quot;);ec(this,d,b,&quot;click&quot;)}this.na[b]=!0};h.usePingClickTracking=function(a,b){this.A[b]=!0;for(var c=0;c<a.length;c++){var d=a[c];d.ping&amp;&amp;(d.setAttribute(this.O,d.ping),d.setAttribute(this.qa,d.href))}};h.disablePingClickTracking=function(a,b){if(!(b in this.A)){this.A[b]=!1;for(var c=0;c<a.length;c++){var d=a[c];d.ping&amp;&amp;(d.setAttribute(this.O,d.ping),d.href=d.ping,d.removeAttribute(&quot;ping&quot;))}}};h.suspendPingClickTracking=function(a,b){if(this.A[b]){this.A[b]=!1;for(var c=0;c<a.length;c++){var d=a[c];d.getAttribute(this.qa)&amp;&amp;(d.href=d.getAttribute(this.O),d.removeAttribute(&quot;ping&quot;))}}};h.restorePingClickTracking=function(a,b){if(b in this.A&amp;&amp;!this.A[b]){this.A[b]=!0;for(var c=0;c<a.length;c++){var d=a[c],e=d.getAttribute(this.qa);e&amp;&amp;(d.ping=d.getAttribute(this.O),d.href=e)}}};h.queueOnObjectAfterClickModifiers=function(a,b,c,d){this.V.push({Va:a,va:b,Xa:c,Wa:d})};var dc=function(a){for(var b=0;b<a.V.length;b++){var c=a.V[b],d=c.Va,e=c.va,f=c.Xa;c.Wa&amp;&amp;(f.preventDefault?f.defaultPrevented:!1===f.returnValue)||d.fireOnObject(e,f)}a.V=[]};var fc=&quot;undefined&quot;!=typeof DOMTokenList,gc=function(a,b){if(fc){var c=a.classList;0==c.contains(b)&amp;&amp;c.toggle(b)}else if(c=a.className){for(var c=c.split(/\s+/),d=!1,e=0;e<c.length&amp;&amp;!d;++e)d=c[e]==b;d||(c.push(b),a.className=c.join(&quot; &quot;))}else a.className=b},hc=function(a,b){if(fc){var c=a.classList;1==c.contains(b)&amp;&amp;c.toggle(b)}else if((c=a.className)&amp;&amp;!(0>c.indexOf(b))){for(var c=c.split(/\s+/),d=0;d<c.length;++d)c[d]==b&amp;&amp;c.splice(d--,1);a.className=c.join(&quot; &quot;)}};var W=function(a,b,c){this.ta=new I;this.h=a;this.h[0]=[b];this.Ea=[];this.R=b.style.display;this.p=new V(c);this.ma=c};h=W.prototype;h.navigationAdPieces=function(){return this.Ea};h.Ka=function(){return!0};h.hide=function(){for(var a=this.h[0],b=0;b<a.length;b++)a[b].style.display=&quot;none&quot;};h.reset=function(){for(var a=this.h[0],b=0;b<a.length;b++)a[b].style.display=this.R};h.has=function(a){return(a=this.h[a])&amp;&amp;0<a.length};h.listen=function(a,b,c){var d=this.h[a];if(d){var e=this.p,f=L(b),g=(&quot;click&quot;==b||&quot;mousedown&quot;==b)&amp;&amp;e.na[a],l=Eb(d,b,ea(c,a,this));e.i[f]||(e.i[f]={});e.i[f][a]||(e.i[f][a]={});var n=e.Ca;e.i[f][a][n]=l;e.Ca=n+1;if(!g)for(e=0;e<d.length;e++)cb(d[e],f,l,void 0);c.B||(c.B={});c.B[b]||(c.B[b]={});c.B[b][a]=n}};h.unlisten=function(a,b,c){var d;if(c.B&amp;&amp;c.B[b]&amp;&amp;c.B[b][a]){var e=c.B[b][a];delete c.B[b][a];d=e}else d=-1;if(c=this.h[a]){var f=this.p,e=L(b);b=(&quot;click&quot;==b||&quot;mousedown&quot;==b)&amp;&amp;f.na[a];if(f.i[e]&amp;&amp;f.i[e][a]){var g=f.i[e][a][d];delete f.i[e][a][d];a=g}else a=null;if(a&amp;&amp;!b)for(b=0;b<c.length;b++)db(c[b],e,a,void 0)}};h.dispatchMouseEvent=function(a,b,c,d,e,f){if(a=this.h[a])for(var g=0;g<a.length;g++){var l=b,l=L(l);gb(a[g],l,c,d,e,f)}};h.registerClickUrlModifier=function(a){this.p.pa.push(a)};h.registerBeaconUrlBuilder=function(a){this.p.registerBeaconUrlBuilder(a)};h.modifyCssClass=function(a,b,c){if(b&amp;&amp;(a=this.h[a]))for(var d=0;d<a.length;d++)(c?hc:gc)(a[d],b)};h.getAttribute=function(a,b){var c=this.h[a];if(c&amp;&amp;b)for(var d=0;d<c.length;d++){var e=c[d].getAttribute(b);if(e)return e}return null};h.setAttribute=function(a,b,c){(a=this.h[a])&amp;&amp;0<a.length&amp;&amp;b&amp;&amp;a[0].setAttribute(b,c)};h.removeAttribute=function(a,b){var c=this.h[a];c&amp;&amp;0<c.length&amp;&amp;b&amp;&amp;c[0].removeAttribute(b)};h.addScroller=function(a,b){var c=this.h[a];if(window.CreateScrollerForElement)for(var d=0;d<c.length;d++){var e=c[d];if(e)for(var d=b,f=e||document,e=f.querySelectorAll&amp;&amp;f.querySelector?f.querySelectorAll(&quot;.&quot;+d):Db(&quot;*&quot;,d,e),d=0;d<e.length;d++)window.CreateScrollerForElement(e[d],!1,!0,!0)}};h.getBoundingClientRect=function(a){return(a=this.h[a])?a[0].getBoundingClientRect():null};h.forEachAdPiece=function(a){var b=this.h;ua(U,function(c){b[c]&amp;&amp;0<b[c].length&amp;&amp;a(c)})};h.U=function(a){this.h[a]&amp;&amp;this.Ka(a)&amp;&amp;(this.Ea.push(a),this.p.U(this.h[a],a))};h.usePingClickTracking=function(a){this.h[a]&amp;&amp;this.p.usePingClickTracking(this.h[a],a)};h.disablePingClickTracking=function(a){this.h[a]&amp;&amp;this.p.disablePingClickTracking(this.h[a],a)};h.suspendPingClickTracking=function(a){this.h[a]&amp;&amp;this.p.suspendPingClickTracking(this.h[a],a)};h.restorePingClickTracking=function(a){this.h[a]&amp;&amp;this.p.restorePingClickTracking(this.h[a],a)};h.hasHref=function(a){a=this.h[a];if(!a)return!1;for(var b=0;b<a.length;b++)if(!a[b].href)return!1;return!0};h.creativeConversionUrl=function(){var a=this.ma.g[5];return null!=a?a:&quot;&quot;};h.listenOnObject=function(a,b){Sa(this.ta,a,b)};h.unlistenOnObject=function(a,b){Ya(this.ta,a,b)};h.fireOnObject=function(a,b){var c=this.ta;c&amp;&amp;c[G]?J(c,a,!1,b):ab(c,a,!1,b)};h.queueOnObjectAfterClickModifiers=function(a,b,c){this.p.queueOnObjectAfterClickModifiers(this,a,b,c)};W.prototype.modifyCssClass=W.prototype.modifyCssClass;W.prototype.has=W.prototype.has;W.prototype.listen=W.prototype.listen;W.prototype.unlisten=W.prototype.unlisten;W.prototype.dispatchMouseEvent=W.prototype.dispatchMouseEvent;W.prototype.registerClickUrlModifier=W.prototype.registerClickUrlModifier;W.prototype.usePingClickTracking=W.prototype.usePingClickTracking;W.prototype.disablePingClickTracking=W.prototype.disablePingClickTracking;W.prototype.suspendPingClickTracking=W.prototype.suspendPingClickTracking;W.prototype.restorePingClickTracking=W.prototype.restorePingClickTracking;W.prototype.registerBeaconUrlBuilder=W.prototype.registerBeaconUrlBuilder;W.prototype.hide=W.prototype.hide;W.prototype.reset=W.prototype.reset;W.prototype.forEachAdPiece=W.prototype.forEachAdPiece;W.prototype.getAttribute=W.prototype.getAttribute;W.prototype.setAttribute=W.prototype.setAttribute;W.prototype.removeAttribute=W.prototype.removeAttribute;W.prototype.getBoundingClientRect=W.prototype.getBoundingClientRect;W.prototype.addScroller=W.prototype.addScroller;W.prototype.hasHref=W.prototype.hasHref;W.prototype.creativeConversionUrl=W.prototype.creativeConversionUrl;W.prototype.listenOnObject=W.prototype.listenOnObject;W.prototype.unlistenOnObject=W.prototype.unlistenOnObject;W.prototype.fireOnObject=W.prototype.fireOnObject;W.prototype.navigationAdPieces=W.prototype.navigationAdPieces;W.prototype.queueOnObjectAfterClickModifiers=W.prototype.queueOnObjectAfterClickModifiers;var jc=function(a,b,c){W.call(this,a,b,c);for(a=0;a<ic.length;a++)this.U(ic[a]);this.listen(4,&quot;mouseover&quot;,q(this.modifyCssClass,this,0,&quot;onhoverbg&quot;,!1));this.listen(4,&quot;mouseout&quot;,q(this.modifyCssClass,this,0,&quot;onhoverbg&quot;,!0))};u(jc,W);var ic=[U.la,U.URL,U.fa,U.Ba,U.Aa,U.za,U.ja,U.ya,U.ka,U.xa,U.Ra],kc={la:&quot;rhtitle&quot;,ja:&quot;rhbody&quot;,URL:&quot;rhurl&quot;,fa:&quot;rhbutton&quot;,za:&quot;rhfavicon&quot;,xa:&quot;rhaddress&quot;,ka:&quot;rhimage&quot;,lb:&quot;rhimagegallery&quot;,ib:&quot;rhimage-container&quot;,kb:&quot;rhexpand-button&quot;,jb:&quot;rhimage-collapsed&quot;,ya:&quot;rhbackground&quot;,gb:&quot;rh-icore-empty&quot;,Ba:&quot;rhsitelink&quot;,Aa:&quot;rhradlink&quot;,nb:&quot;rh-multiframe&quot;,eb:&quot;rh-box-breadcrumbs&quot;};jc.prototype.Ka=function(a){return this.hasHref(a)||4==a||6==a};r(&quot;buildRhTextAd&quot;,function(a){a=new ma(a);var b=a.g[1],c;var d={};if(b=document.getElementById(&quot;taw&quot;+(null!=b?b:0))){d[0]=[b];for(c in kc){var e=U[c],f=d,g=Db(null,kc[c],b);f[e]=[];for(var l=0;l<g.length;l++)f[e].push(g[l])}c=new jc(d,b,a)}else c=null;return c});var Z=function(a,b,c){I.call(this);this.u=a;this.R=&quot;none&quot;;this.u&amp;&amp;(this.R=this.u.style.display);this.v=b;this.g=c;this.i={};this.oa=[];this.Da=!1;this.q=[]};u(Z,I);h=Z.prototype;h.forEachAd=function(a){qa(this.v,a)};h.addAd=function(a){this.v.push(a)};h.pb=function(a){if(a=document.getElementById(a))this.u=a,this.R=this.u.style.display;if(0==this.v.length)window.css=null;else{window.SlideConstructor&amp;&amp;0<this.v.length&amp;&amp;new window.SlideConstructor(this.v[0],this,w(this.g));window.GridConstructor&amp;&amp;0<this.v.length&amp;&amp;new window.GridConstructor(this,w(this.g));window.ImageExpandConstructor&amp;&amp;1==this.v.length&amp;&amp;new window.ImageExpandConstructor(this,w(this.g));window.OneClickConstructor&amp;&amp;0<this.v.length&amp;&amp;new window.OneClickConstructor(this,0);if(window.OnePointFiveClickConstructor&amp;&amp;0<this.v.length){a=x(this.g).g[0];var b=x(this.g).g[1],c=x(this.g).g[2],d=x(this.g).g[4],e=x(this.g).g[3];new window.OnePointFiveClickConstructor(this,null!=a?a:!1,null!=b?b:!1,null!=c?c:!1,null!=e?e:0,null!=d?d:!1)}window.MultiframeConstructor&amp;&amp;new window.MultiframeConstructor(this,w(this.g));if(a=window.ona)a=this.g.g[4],a=!(null!=a&amp;&amp;a);a&amp;&amp;(window.ona=null);for(a=0;a<this.oa.length;++a)this.oa[a]();this.Da=!0}};h.listenOnContainer=function(a,b){var c=Eb([this.u],a,ea(b,this));cb(this.u,L(a),c,void 0);this.i[a]||(this.i[a]={});this.i[a][b]=c};h.unlistenOnContainer=function(a,b){var c;this.i[a]&amp;&amp;this.i[a][b]?(c=this.i[a][b],delete this.i[a][b]):c=null;c&amp;&amp;db(this.u,L(a),c,void 0)};h.listenOnObject=function(a,b){Sa(this,a,b)};h.unlistenOnObject=function(a,b){Ya(this,a,b)};h.fireOnObject=function(a,b){b.vb=this;this&amp;&amp;this[G]?J(this,a,!1,b):ab(this,a,!1,b)};h.registerFinalizeCallback=function(a){this.Da?a():this.oa.push(a)};h.registerWidget=function(a,b){0<=pa(this.q,a)||(this.q[b]=a,a.reset(this))};var lc=function(a){a.u.style.display=&quot;none&quot;;for(var b=0;b<a.q.length;b++)a.q[b]&amp;&amp;a.q[b].hide(a)};Z.prototype.resetAll=function(){this.u.style.display=this.R;for(var a=0;a<this.q.length;a++)this.q[a]&amp;&amp;this.q[a].reset(this)};Z.prototype.showOnly=function(a){var b=this;lc(this);mc(this,a,function(a){a.show(b)})};var mc=function(a,b,c){a.q[b]&amp;&amp;c(a.q[b])};Z.prototype.isMobile=function(){return w(this.g)};Z.prototype.getEscapedQemQueryId=function(){return this.g.getEscapedQemQueryId()};Z.prototype.getEscapedGwsQueryId=function(){return this.g.getEscapedGwsQueryId()};Z.prototype.forEachAd=Z.prototype.forEachAd;Z.prototype.addAd=Z.prototype.addAd;Z.prototype.finalize=Z.prototype.pb;Z.prototype.registerFinalizeCallback=Z.prototype.registerFinalizeCallback;Z.prototype.listenOnContainer=Z.prototype.listenOnContainer;Z.prototype.unlistenOnContainer=Z.prototype.unlistenOnContainer;Z.prototype.registerWidget=Z.prototype.registerWidget;Z.prototype.resetAll=Z.prototype.resetAll;Z.prototype.showOnly=Z.prototype.showOnly;Z.prototype.isMobile=Z.prototype.isMobile;Z.prototype.getEscapedQemQueryId=Z.prototype.getEscapedQemQueryId;Z.prototype.getEscapedGwsQueryId=Z.prototype.getEscapedGwsQueryId;Z.prototype.listenOnObject=Z.prototype.listenOnObject;Z.prototype.unlistenOnObject=Z.prototype.unlistenOnObject;Z.prototype.fireOnObject=Z.prototype.fireOnObject;r(&quot;buildAdSlot&quot;,function(a){a=new Z(null,[],new ka(a));r(&quot;adSlot&quot;,a);return a});var nc=function(a,b,c){var d=[];d[0]=[b];d[15]=[a];W.call(this,d,b,c);this.U(15)};u(nc,W);r(&quot;buildImageAd&quot;,function(a){a=new ma(a);var b=document,c=b.getElementById(&quot;google_image_div&quot;),b=b.getElementById(&quot;aw0&quot;);return c&amp;&amp;b?new nc(b,c,a):null});var pc=function(a,b,c){W.call(this,a,b,c);for(a=0;a<oc.length;a++)this.U(oc[a])};u(pc,W);var oc=[U.la,U.URL,U.fa,U.Ba,U.Aa,U.za,U.ja,U.ya,U.ka,U.xa,U.Ra],qc={la:&quot;headline&quot;,ja:&quot;description&quot;,fa:&quot;button&quot;,fb:&quot;logo&quot;,ka:&quot;product&quot;};r(&quot;buildTemplateAd&quot;,function(a){var b;a=new ma(a);var c={},d=document.getElementById(&quot;adContent&quot;);if(d){c[0]=[d];for(b in qc){var e=U[b],f=c,g=Db(null,qc[b],d);f[e]=[];for(var l=0;l<g.length;l++)f[e].push(g[l])}b=new pc(c,d,a)}else b=null;return b});})();</script><script>buildAdSlot([null,728,90,0,0]);var ad = buildImageAd([1,0,728,90,null,&quot;https://googleads.g.doubleclick.net/pagead/conversion/?ai=CWrJ5hYG2VK7-MJa18gXbwYKQApnz6oMGgdm6lvIBh-CivcABEAEg7PzvGmDhtLqFkBqgAcerytoDyAEC4AIAqAMByAOZBKoErgFP0Ba9cJ2PZ-Ur_-thimaodKTT23UMSIiXxUN_QcPyxlCJvo7uEuiiQWalKde4HZBGOAD-76HZ4ivrWoI4awzNTGdzdmJBBF-SCh6zmPwHfnHFHeHBOFDZG1KUHTq9rp8dYslDdlpWexi8lKLpzUBVC_v74P8XuMgSWXHPZHF6Z26IQbfXcPFcj9BPOftbJulzqspLvSDZTD-eoM6wb1wwxDW3E5YGjjKRQuIOxS7gBAGIBgGgBgKAB6HUtSU\u0026sigh=zzEAlHdV3G8&quot;]);adSlot.addAd(ad);adSlot.finalize('google_image_div');</script><script></script><script>(function(){var c=this,e=function(a,b){var f=a.split(&quot;.&quot;),d=c;f[0]in d||!d.execScript||d.execScript(&quot;var &quot;+f[0]);for(var g;f.length&amp;&amp;(g=f.shift());)f.length||void 0===b?d=d[g]?d[g]:d[g]={}:d[g]=b},h=function(a,b){var f=Array.prototype.slice.call(arguments,1);return function(){var b=f.slice();b.push.apply(b,arguments);return a.apply(this,b)}};var k=function(){this.g=[];this.h={}};k.prototype.report=function(){for(var a=[],b=0;b<this.g.length;++b)a.push(l(this.g[b]));return a};var l=function(a){var b=[a.key,a.value];void 0!==a.i&amp;&amp;b.push(a.i);return b},m={};var n=function(a,b,f,d,g){&quot;true&quot;===d.getAttribute(f,&quot;data-is-action-button-expanded&quot;)&amp;&amp;(b=12);ia(a,g,b)},p=function(a){return function(){a()}},q=function(a){return a.report()};e(&quot;registerAd&quot;,function(a,b){void 0!==m[b]||(m[b]=new k);a.registerClickUrlModifier(h(q,m[b]));a.listen(0,&quot;mouseover&quot;,p(h(ss,b)));a.listen(0,&quot;focus&quot;,p(h(ss,b)));a.listen(1,&quot;click&quot;,p(h(ha,b)));a.listen(1,&quot;focus&quot;,p(h(ss,b)));a.listen(1,&quot;mousedown&quot;,p(h(st,b)));a.listen(1,&quot;mouseover&quot;,p(h(ss,b)));a.listen(2,&quot;click&quot;,h(n,b,null));a.listen(2,&quot;mousedown&quot;,p(h(st,b)));a.listen(4,&quot;click&quot;,h(n,b,8));a.listen(4,&quot;mousedown&quot;,p(h(st,b)));a.listen(8,&quot;click&quot;,h(n,b,11));a.listen(8,&quot;mousedown&quot;,p(h(st,b)));a.listen(6,&quot;click&quot;,h(n,b,9));a.listen(6,&quot;mousedown&quot;,p(h(st,b)));a.listen(9,&quot;click&quot;,h(n,b,2));a.listen(9,&quot;mousedown&quot;,p(h(st,b)));a.listen(15,&quot;click&quot;,p(h(ha,b)));a.listen(15,&quot;mousedown&quot;,p(h(st,b)));a.listen(5,&quot;click&quot;,h(n,b,6));a.listen(5,&quot;mousedown&quot;,p(h(st,b)));return a});e(&quot;css&quot;,function(a,b,f,d,g){a=m[a];void 0!==a&amp;&amp;(void 0===a.h[b]||d?(d=a.g.length,a.h[b]=d,a.g[d]={key:b,value:f,i:g}):(b=a.g[a.h[b]],b.value=f,b.i=g))});})();registerAd(ad, 'aw0');</script><iframe scrolling=&quot;no&quot; frameborder=0 height=0 width=0 src=&quot;https://cm.g.doubleclick.net/push?client=ca-pub-8799115960791774&quot; style=&quot;position:absolute&quot;></iframe><script type=&quot;text/javascript&quot;>(function(){var h=this,m=function(a){var b=typeof a;if(&quot;object&quot;==b)if(a){if(a instanceof Array)return&quot;array&quot;;if(a instanceof Object)return b;var c=Object.prototype.toString.call(a);if(&quot;[object Window]&quot;==c)return&quot;object&quot;;if(&quot;[object Array]&quot;==c||&quot;number&quot;==typeof a.length&amp;&amp;&quot;undefined&quot;!=typeof a.splice&amp;&amp;&quot;undefined&quot;!=typeof a.propertyIsEnumerable&amp;&amp;!a.propertyIsEnumerable(&quot;splice&quot;))return&quot;array&quot;;if(&quot;[object Function]&quot;==c||&quot;undefined&quot;!=typeof a.call&amp;&amp;&quot;undefined&quot;!=typeof a.propertyIsEnumerable&amp;&amp;!a.propertyIsEnumerable(&quot;call&quot;))return&quot;function&quot;}else return&quot;null&quot;;else if(&quot;function&quot;==b&amp;&amp;&quot;undefined&quot;==typeof a.call)return&quot;object&quot;;return b},p=function(a){return&quot;string&quot;==typeof a},aa=function(a,b){var c=Array.prototype.slice.call(arguments,1);return function(){var b=c.slice();b.push.apply(b,arguments);return a.apply(this,b)}},q=Date.now||function(){return+new Date},r=function(a,b){var c=a.split(&quot;.&quot;),d=h;c[0]in d||!d.execScript||d.execScript(&quot;var &quot;+c[0]);for(var e;c.length&amp;&amp;(e=c.shift());)c.length||void 0===b?d=d[e]?d[e]:d[e]={}:d[e]=b};var t=function(a,b,c,d,e){if(e)c=a+(&quot;&amp;&quot;+b+&quot;=&quot;+c);else{var f=&quot;&amp;&quot;+b+&quot;=&quot;,g=a.indexOf(f);0>g?c=a+f+c:(g+=f.length,f=a.indexOf(&quot;&amp;&quot;,g),c=0<=f?a.substring(0,g)+c+a.substring(f):a.substring(0,g)+c)}return 2E3<c.length?void 0!==d?t(a,b,d,void 0,e):a:c};var ba=function(){var a=/[&amp;\?]exk=([^&amp; ]+)/.exec(w.location.href);return a&amp;&amp;2==a.length?a[1]:null};var ca=function(a){var b=a.toString();a.name&amp;&amp;-1==b.indexOf(a.name)&amp;&amp;(b+=&quot;: &quot;+a.name);a.message&amp;&amp;-1==b.indexOf(a.message)&amp;&amp;(b+=&quot;: &quot;+a.message);if(a.stack){a=a.stack;var c=b;try{-1==a.indexOf(c)&amp;&amp;(a=c+&quot;\n&quot;+a);for(var d;a!=d;)d=a,a=a.replace(/((https?:\/..*\/)[^\/:]*:\d+(?:.|\n)*)\2/,&quot;$1&quot;);b=a.replace(/\n */g,&quot;\n&quot;)}catch(e){b=c}}return b},x=function(a,b){a.google_image_requests||(a.google_image_requests=[]);var c=a.document.createElement(&quot;img&quot;);c.src=b;a.google_image_requests.push(c)};var y=document,w=window;var da=String.prototype.trim?function(a){return a.trim()}:function(a){return a.replace(/^[\s\xa0]+|[\s\xa0]+$/g,&quot;&quot;)},ea=function(a,b){return a<b?-1:a>b?1:0};var z=null,fa=function(a,b){for(var c in a)Object.prototype.hasOwnProperty.call(a,c)&amp;&amp;b.call(null,a[c],c,a)};function A(a){return&quot;function&quot;==typeof encodeURIComponent?encodeURIComponent(a):escape(a)}var ga=function(){if(!y.body)return!1;if(!z){var a=y.createElement(&quot;iframe&quot;);a.style.display=&quot;none&quot;;a.id=&quot;anonIframe&quot;;z=a;y.body.appendChild(a)}return!0},ha={};var ia=!0,ja={},ma=function(a,b,c,d){var e=ka,f,g=ia;try{f=b()}catch(k){try{var u=ca(k);b=&quot;&quot;;k.fileName&amp;&amp;(b=k.fileName);var v=-1;k.lineNumber&amp;&amp;(v=k.lineNumber);g=e(a,u,b,v,c)}catch(n){try{var l=ca(n);a=&quot;&quot;;n.fileName&amp;&amp;(a=n.fileName);c=-1;n.lineNumber&amp;&amp;(c=n.lineNumber);ka(&quot;pAR&quot;,l,a,c,void 0,void 0)}catch(wa){la({context:&quot;mRE&quot;,msg:wa.toString()+&quot;\n&quot;+(wa.stack||&quot;&quot;)},void 0)}}if(!g)throw k;}finally{if(d)try{d()}catch(hb){}}return f},ka=function(a,b,c,d,e,f){var g={};if(e)try{e(g)}catch(k){}g.context=a;g.msg=b.substring(0,512);c&amp;&amp;(g.file=c);0<d&amp;&amp;(g.line=d.toString());g.url=y.URL.substring(0,512);g.ref=y.referrer.substring(0,512);na(g);la(g,f);return ia},la=function(a,b){try{if(Math.random()<(b||.01)){var c=&quot;/pagead/gen_204?id=jserror&quot;+oa(a),d=&quot;http&quot;+(&quot;http:&quot;==w.location.protocol?&quot;&quot;:&quot;s&quot;)+&quot;://pagead2.googlesyndication.com&quot;+c,d=d.substring(0,2E3);x(w,d)}}catch(e){}},na=function(a){var b=a||{};fa(ja,function(a,d){b[d]=w[a]})},B=function(a,b,c,d,e){return function(){var f=arguments;return ma(a,function(){return b.apply(c,f)},d,e)}},pa=function(a,b){return B(a,b,void 0,void 0,void 0)},oa=function(a){var b=&quot;&quot;;fa(a,function(a,d){if(0===a||a)b+=&quot;&amp;&quot;+d+&quot;=&quot;+A(a)});return b};var C=Array.prototype,qa=C.indexOf?function(a,b,c){return C.indexOf.call(a,b,c)}:function(a,b,c){c=null==c?0:0>c?Math.max(0,a.length+c):c;if(p(a))return p(b)&amp;&amp;1==b.length?a.indexOf(b,c):-1;for(;c<a.length;c++)if(c in a&amp;&amp;a[c]===b)return c;return-1},ra=C.map?function(a,b,c){return C.map.call(a,b,c)}:function(a,b,c){for(var d=a.length,e=Array(d),f=p(a)?a.split(&quot;&quot;):a,g=0;g<d;g++)g in f&amp;&amp;(e[g]=b.call(c,f[g],g,a));return e};var sa={c:947190538,d:947190541};if(y&amp;&amp;y.URL)var ta=y.URL,ia=!(ta&amp;&amp;(0<ta.indexOf(&quot;?google_debug&quot;)||0<ta.indexOf(&quot;&amp;google_debug&quot;)));var D=function(a,b,c,d){c=B(d||&quot;osd_or_lidar::&quot;+b,c,void 0,void 0,void 0);a.addEventListener?a.addEventListener(b,c,!1):a.attachEvent&amp;&amp;a.attachEvent(&quot;on&quot;+b,c)},ua=function(a){var b=0,c=function(){a();b++;10>b&amp;&amp;w.setTimeout(pa(&quot;osd_listener::ldcl_int&quot;,c),100)};c()};var va=function(){try{w.localStorage.setItem(&quot;__sak&quot;,&quot;1&quot;);var a=w.localStorage.__sak;w.localStorage.removeItem(&quot;__sak&quot;);return&quot;1&quot;==a}catch(b){return!1}},xa=function(a,b,c){a.google_image_requests||(a.google_image_requests=[]);var d=a.document.createElement(&quot;img&quot;);D(d,&quot;load&quot;,c,&quot;osd::ls_img::load&quot;);d.src=b;a.google_image_requests.push(d)};var ya=function(a,b){for(var c in a)b.call(void 0,a[c],c,a)},E=function(a){var b=arguments.length;if(1==b&amp;&amp;&quot;array&quot;==m(arguments[0]))return E.apply(null,arguments[0]);for(var c={},d=0;d<b;d++)c[arguments[d]]=!0;return c};var F;r:{var za=h.navigator;if(za){var Aa=za.userAgent;if(Aa){F=Aa;break r}}F=&quot;&quot;};var Ba=-1!=F.indexOf(&quot;Opera&quot;)||-1!=F.indexOf(&quot;OPR&quot;),G=-1!=F.indexOf(&quot;Trident&quot;)||-1!=F.indexOf(&quot;MSIE&quot;),Ca=-1!=F.indexOf(&quot;Gecko&quot;)&amp;&amp;-1==F.toLowerCase().indexOf(&quot;webkit&quot;)&amp;&amp;!(-1!=F.indexOf(&quot;Trident&quot;)||-1!=F.indexOf(&quot;MSIE&quot;)),Da=-1!=F.toLowerCase().indexOf(&quot;webkit&quot;),Ea=function(){var a=h.document;return a?a.documentMode:void 0},Fa=function(){var a=&quot;&quot;,b;if(Ba&amp;&amp;h.opera)return a=h.opera.version,&quot;function&quot;==m(a)?a():a;Ca?b=/rv\:([^\);]+)(\)|;)/:G?b=/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/:Da&amp;&amp;(b=/WebKit\/(\S+)/);b&amp;&amp;(a=(a=b.exec(F))?a[1]:&quot;&quot;);return G&amp;&amp;(b=Ea(),b>parseFloat(a))?String(b):a}(),Ga={},Ha=function(a){if(!Ga[a]){for(var b=0,c=da(String(Fa)).split(&quot;.&quot;),d=da(String(a)).split(&quot;.&quot;),e=Math.max(c.length,d.length),f=0;0==b&amp;&amp;f<e;f++){var g=c[f]||&quot;&quot;,k=d[f]||&quot;&quot;,u=RegExp(&quot;(\\d*)(\\D*)&quot;,&quot;g&quot;),v=RegExp(&quot;(\\d*)(\\D*)&quot;,&quot;g&quot;);do{var n=u.exec(g)||[&quot;&quot;,&quot;&quot;,&quot;&quot;],l=v.exec(k)||[&quot;&quot;,&quot;&quot;,&quot;&quot;];if(0==n[0].length&amp;&amp;0==l[0].length)break;b=ea(0==n[1].length?0:parseInt(n[1],10),0==l[1].length?0:parseInt(l[1],10))||ea(0==n[2].length,0==l[2].length)||ea(n[2],l[2])}while(0==b)}Ga[a]=0<=b}},Ia=h.document,Ja=Ia&amp;&amp;G?Ea()||(&quot;CSS1Compat&quot;==Ia.compatMode?parseInt(Fa,10):5):void 0;var H=function(a,b){this.b=a||0;this.a=b||&quot;&quot;},Ka=function(a,b){a.b&amp;&amp;(b[4]=a.b);a.a&amp;&amp;(b[12]=a.a)};H.prototype.match=function(a){return(this.b||this.a)&amp;&amp;(a.b||a.a)?this.a||a.a?this.a==a.a:this.b||a.b?this.b==a.b:!1:!1};H.prototype.toString=function(){var a=&quot;&quot;+this.b;this.a&amp;&amp;(a+=&quot;-&quot;+this.a);return a};var La=function(){var a=I,b=[];a.b&amp;&amp;b.push(&quot;adk=&quot;+a.b);a.a&amp;&amp;b.push(&quot;exk=&quot;+a.a);return b},Ma=function(a){var b=[];ya(a,function(a,d){var e=A(d),f=a;p(f)&amp;&amp;(f=A(f));b.push(e+&quot;=&quot;+f)});return b.join(&quot;\n&quot;)},J=0,Na=0,Oa=function(a){var b=0,c=w;if(c&amp;&amp;c.Goog_AdSense_getAdAdapterInstance)return c;try{for(;c&amp;&amp;5>b;){if(c.google_osd_static_frame)return c;if(c.aswift_0&amp;&amp;(!a||c.aswift_0.google_osd_static_frame))return c.aswift_0;b++;c=c!=c.parent?c.parent:null}}catch(d){}return null},Pa=function(a,b,c,d){if(10<Na)w.clearInterval(J);else if(++Na,w.postMessage&amp;&amp;(b.b||b.a)){var e=Oa(!0);if(e){var f={};Ka(b,f);f[0]=&quot;goog_request_monitoring&quot;;f[6]=a;f[16]=c;d&amp;&amp;d.length&amp;&amp;(f[17]=d.join(&quot;,&quot;));try{var g=Ma(f);e.postMessage(g,&quot;*&quot;)}catch(k){}}}};E(&quot;area base br col command embed hr img input keygen link meta param source track wbr&quot;.split(&quot; &quot;));E(&quot;action&quot;,&quot;cite&quot;,&quot;data&quot;,&quot;formaction&quot;,&quot;href&quot;,&quot;manifest&quot;,&quot;poster&quot;,&quot;src&quot;);E(&quot;embed&quot;,&quot;iframe&quot;,&quot;link&quot;,&quot;object&quot;,&quot;script&quot;,&quot;style&quot;,&quot;template&quot;);var Qa;if(!(Qa=!Ca&amp;&amp;!G)){var Ra;if(Ra=G)Ra=G&amp;&amp;9<=Ja;Qa=Ra}Qa||Ca&amp;&amp;Ha(&quot;1.9.1&quot;);G&amp;&amp;Ha(&quot;9&quot;);var Sa,K=0,L=&quot;&quot;,M=!1,N=!1,O=!1,Ta=!1,Ua=[],I=null,P=&quot;&quot;,Va=[],Wa=[],Xa=!1,Q=&quot;&quot;,R=&quot;&quot;,Ya=(new Date).getTime(),Za=[&quot;1&quot;,&quot;0&quot;,&quot;3&quot;],S=0,T=!1,U=&quot;&quot;,V=null,W=0,X=0,$a=0,ab=function(a,b){M&amp;&amp;Y(a,b,!0);(O||N&amp;&amp;Ta)&amp;&amp;Y(a,b)},Y=function(a,b,c){if((b=b||P)&amp;&amp;!Xa&amp;&amp;(2==X||c)){b=bb(b,c);if(!c&amp;&amp;T){T=!1;V&amp;&amp;(a.clearInterval(V),V=null);var d=U;try{a.localStorage[d]=b+&quot;&amp;timestamp=&quot;+q()+&quot;&amp;send&quot;}catch(e){}5!=S&amp;&amp;xa(a,b,function(){a.localStorage.removeItem(d)})}else x(a,b);c?M=!1:Xa=!0}},bb=function(a,b){var c;c=b?&quot;osdim&quot;:O?&quot;osd2&quot;:&quot;osdtos&quot;;var d=[&quot;//pagead2.googlesyndication.com/activeview&quot;,&quot;?id=&quot;,c];&quot;osd2&quot;==c&amp;&amp;N&amp;&amp;Ta&amp;&amp;d.push(&quot;&amp;ts=1&quot;);L&amp;&amp;d.push(&quot;&amp;avi=&quot;,L);Sa&amp;&amp;d.push(&quot;&amp;cid=&quot;,Sa);0!=S&amp;&amp;d.push(&quot;&amp;lsid=&quot;,S);T&amp;&amp;d.push(&quot;&amp;cwls=1&quot;);d.push(&quot;&amp;ti=1&quot;);d.push(&quot;&amp;&quot;,a);d.push(&quot;&amp;uc=&quot;+$a);c=d.join(&quot;&quot;);for(d=0;d<Va.length;d++){try{var e=Va[d]()}catch(f){}var g=&quot;max_length&quot;;2<=e.length&amp;&amp;(3==e.length&amp;&amp;(g=e[2]),c=t(c,A(e[0]),A(e[1]),g))}2E3<c.length&amp;&amp;(c=c.substring(0,2E3));return c},Z=function(a,b){if(Q){try{var c=t(Q,&quot;vi&quot;,a);ga()&amp;&amp;x(z.contentWindow,c)}catch(d){}0<=qa(Za,a)&amp;&amp;(Q=&quot;&quot;);var c=b||P,e;e=t(&quot;//pagead2.googlesyndication.com/pagead/gen_204?id=sldb&quot;,&quot;avi&quot;,L);e=t(e,&quot;vi&quot;,a);c&amp;&amp;(e+=&quot;&amp;&quot;+c);try{x(w,e)}catch(f){}}},cb=function(){Z(&quot;-1&quot;)},eb=function(a){if(a&amp;&amp;a.data&amp;&amp;p(a.data)){var b;var c=a.data;if(p(c)){b={};for(var c=c.split(&quot;\n&quot;),d=0;d<c.length;d++){var e=c[d].indexOf(&quot;=&quot;);if(!(0>=e)){var f=Number(c[d].substr(0,e)),e=c[d].substr(e+1);switch(f){case 5:case 8:case 11:case 15:case 16:e=&quot;true&quot;==e;break;case 4:case 7:case 6:case 14:e=Number(e);break;case 3:if(&quot;function&quot;==m(decodeURIComponent))try{e=decodeURIComponent(e)}catch(g){throw Error(&quot;Error: URI malformed: &quot;+e);}break;case 17:e=ra(decodeURIComponent(e).split(&quot;,&quot;),Number)}b[f]=e}}b=b[0]?b:null}else b=null;if(b&amp;&amp;(c=new H(b[4],b[12]),I&amp;&amp;I.match(c))){for(c=0;c<Wa.length;c++)Wa[c](b);c=b[0];if(&quot;goog_acknowledge_monitoring&quot;==c)w.clearInterval(J),W=2;else if(&quot;goog_get_mode&quot;==c){W=1;d={};I&amp;&amp;Ka(I,d);d[0]=&quot;goog_provide_mode&quot;;d[6]=X;try{var k=Ma(d);a.source.postMessage(k,a.origin)}catch(u){}w.clearInterval(J);W=2}else if(&quot;goog_update_data&quot;==c){if(a=w,P=b[3],++$a,T){k=U;d=bb(P);try{a.localStorage[k]=db(d)}catch(v){}}}else&quot;goog_image_request&quot;==c&amp;&amp;(ab(w,b[3]),b[5]||b[11]||Z(&quot;0&quot;,b[3]));if(&quot;goog_update_data&quot;==c||&quot;goog_image_request&quot;==c)(1==X||2==X||M)&amp;&amp;b[5]&amp;&amp;(a=1==b[15]&amp;&amp;&quot;goog_update_data&quot;==c,Ta=!0,Z(&quot;1&quot;),R&amp;&amp;(k=R,ga()&amp;&amp;x(z.contentWindow,k),R=&quot;&quot;),M&amp;&amp;!a&amp;&amp;Y(w,void 0,!0),1==X?Xa=!0:(2==S||4==S||5==S&amp;&amp;!T)&amp;&amp;Y(w)),(1==X||2==X||M)&amp;&amp;b[11]&amp;&amp;(N=!1,Z(&quot;3&quot;),M&amp;&amp;Y(w,void 0,!0),(2==S||4==S||5==S&amp;&amp;!T)&amp;&amp;Y(w))}}},fb=function(){ab(w);Z(&quot;0&quot;);if(2>W&amp;&amp;2==X){var a=w,b=&quot;//pagead2.googlesyndication.com/pagead/gen_204?id=osd2&amp;&quot;,c=[];c.push(&quot;ovr_value=&quot;+K);c.push(&quot;avi=&quot;+L);I&amp;&amp;(c=c.concat(La()));c.push(&quot;tt=&quot;+((new Date).getTime()-Ya));a.document&amp;&amp;a.document.referrer&amp;&amp;c.push(&quot;ref=&quot;+A(a.document.referrer));c.push(&quot;hs=&quot;+W);b+=c.join(&quot;&amp;&quot;);try{x(a,b)}catch(d){}}},db=function(a){var b=a.match(/^(.*&amp;timestamp=)\d+$/);return b?b[1]+q():a+&quot;&amp;timestamp=&quot;+q()},gb=function(){var a={};Ka(I,a);a[0]=&quot;goog_dom_content_loaded&quot;;var b=Ma(a);ua(function(){var a=Oa(!1),d=!a;!a&amp;&amp;w&amp;&amp;(a=w.parent);if(a&amp;&amp;a.postMessage)try{a.postMessage(b,&quot;*&quot;),d&amp;&amp;w.postMessage(b,&quot;*&quot;)}catch(e){}})};r(&quot;osdlfm&quot;,B(&quot;osd_listener::init&quot;,function(a,b,c,d,e,f,g,k,u,v,n){K=a;Q=b;R=d;M=f;S=v||0;Sa=n;N=g&amp;&amp;f;1!=u&amp;&amp;2!=u||Ua.push(sa[&quot;MRC_TEST_&quot;+u]);I=new H(e,ba());D(w,&quot;load&quot;,cb,&quot;osd_listener::load&quot;);D(w,&quot;message&quot;,eb,&quot;osd_listener::message&quot;);L=c||&quot;&quot;;D(w,&quot;unload&quot;,fb,&quot;osd_listener::unload&quot;);var l=w.document;!l.readyState||&quot;complete&quot;!=l.readyState&amp;&amp;&quot;loaded&quot;!=l.readyState?(&quot;msie&quot;in ha?ha.msie:ha.msie=-1!=navigator.userAgent.toLowerCase().indexOf(&quot;msie&quot;))&amp;&amp;!window.opera?D(l,&quot;readystatechange&quot;,function(){&quot;complete&quot;!=l.readyState&amp;&amp;&quot;loaded&quot;!=l.readyState||gb()},&quot;osd_listener::rsc&quot;):D(l,&quot;DOMContentLoaded&quot;,gb,&quot;osd_listener::dcl&quot;):gb();-1==K?X=f?3:1:-2==K?X=3:0<K&amp;&amp;(X=2,O=!0);N&amp;&amp;!O&amp;&amp;(X=2);2==X&amp;&amp;w.location.hostname.match(/doubleclick\.net/)&amp;&amp;(3==S||4==S||5==S)&amp;&amp;va()&amp;&amp;1E3>w.localStorage.length&amp;&amp;(U=&quot;LSPNGS-&quot;+I.toString()+&quot;-&quot;+(&quot;&quot;+Math.random()).split(&quot;.&quot;)[1]+q(),T=!0,V=w.setInterval(pa(&quot;osd_listener::ls_int&quot;,function(){var a=w,b=U,c=a.localStorage[b];if(c)try{a.localStorage[b]=db(c)}catch(d){}}),1E3));I&amp;&amp;(I.b||I.a)&amp;&amp;(W=1,J=w.setInterval(pa(&quot;osd_proto::reqm_int&quot;,aa(Pa,X,I,N,Ua)),500))}));r(&quot;osdlac&quot;,B(&quot;osd_listener::lac_ex&quot;,function(a){Va.push(a)}));r(&quot;osdlamrc&quot;,B(&quot;osd_listener::lamrc_ex&quot;,function(a){Wa.push(a)}));r(&quot;osdsir&quot;,B(&quot;osd_listener::sir_ex&quot;,ab));})();osdlfm(-1,'','B3KLlhYG2VK7-MJa18gXbwYKQAgCB2bqW8gEAABABOAHIAQLgAgDIA5kE4AQBoAYCwhMDEIAB','',1827521381,true,false,'',0,0,'');</script></body></html>{&quot;uid&quot;:2,&quot;hostPeerName&quot;:&quot;https://www.scribd.com&quot;,&quot;initialGeometry&quot;:&quot;{\&quot;windowCoords_t\&quot;:21,\&quot;windowCoords_r\&quot;:1366,\&quot;windowCoords_b\&quot;:726,\&quot;windowCoords_l\&quot;:0,\&quot;frameCoords_t\&quot;:16801,\&quot;frameCoords_r\&quot;:890,\&quot;frameCoords_b\&quot;:16891,\&quot;frameCoords_l\&quot;:162,\&quot;styleZIndex\&quot;:\&quot;auto\&quot;,\&quot;allowedExpansion_t\&quot;:0,\&quot;allowedExpansion_r\&quot;:0,\&quot;allowedExpansion_b\&quot;:0,\&quot;allowedExpansion_l\&quot;:0,\&quot;xInView\&quot;:0,\&quot;yInView\&quot;:0}&quot;,&quot;permissions&quot;:&quot;{\&quot;expandByOverlay\&quot;:true,\&quot;expandByPush\&quot;:false,\&quot;readCookie\&quot;:false,\&quot;writeCookie\&quot;:false}&quot;,&quot;metadata&quot;:&quot;{\&quot;shared\&quot;:{\&quot;sf_ver\&quot;:\&quot;1-0-1\&quot;,\&quot;ck_on\&quot;:1,\&quot;flash_ver\&quot;:\&quot;16.0.0\&quot;}}&quot;}" scrolling="no" marginwidth="0" marginheight="0" width="728" height="90" data-is-safeframe="true" style="border: 0px; vertical-align: bottom;"></iframe></div><iframe id="google_ads_iframe_/1024966/Doc_Between_Leaderboard_BTF_728x90_19_0__hidden__" name="google_ads_iframe_/1024966/Doc_Between_Leaderboard_BTF_728x90_19_0__hidden__" width="0" height="0" scrolling="no" marginwidth="0" marginheight="0" frameborder="0" src="javascript:&quot;<html><body style='background:transparent'></body></html>&quot;" style="border: 0px; vertical-align: bottom; visibility: hidden; display: none;"></iframe></div>
    </div>




  <div class="outer_page only_ie6_border        not_visible" id="outer_page_20" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="-webkit-transform: scale(0.7617823479006); -webkit-transform-origin: 0% 0%; display: none;"><div class="newpage" id="page20" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/20-4e896fa7b7.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 20};

        pageParams.containerElem = document.getElementById("outer_page_20");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/20-4e896fa7b7.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_20" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(20);
      </script>
    </div>




  <div class="outer_page only_ie6_border         not_visible" id="outer_page_21" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="-webkit-transform: scale(0.7617823479006); -webkit-transform-origin: 0% 0%; display: none;"><div class="newpage" id="page21" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/21-d7f9ec2fc7.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 21};

        pageParams.containerElem = document.getElementById("outer_page_21");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/21-d7f9ec2fc7.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_21" class="between_page_ads is_filled" style="display: block; height: 90px;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(21);
      </script><div id="between_page_ads_inner_21" style="position: absolute; width: 728px; height: 90px;"><div id="google_ads_iframe_/1024966/Doc_Between_Leaderboard_BTF_728x90_21_0__container__" style="border: 0pt none;"><iframe id="google_ads_iframe_/1024966/Doc_Between_Leaderboard_BTF_728x90_21_0" name="google_ads_iframe_/1024966/Doc_Between_Leaderboard_BTF_728x90_21_0" width="728" height="90" scrolling="no" marginwidth="0" marginheight="0" frameborder="0" src="javascript:&quot;<html><body style='background:transparent'></body></html>&quot;" style="border: 0px; vertical-align: bottom;"></iframe></div><iframe id="google_ads_iframe_/1024966/Doc_Between_Leaderboard_BTF_728x90_21_0__hidden__" name="google_ads_iframe_/1024966/Doc_Between_Leaderboard_BTF_728x90_21_0__hidden__" width="0" height="0" scrolling="no" marginwidth="0" marginheight="0" frameborder="0" src="javascript:&quot;<html><body style='background:transparent'></body></html>&quot;" style="border: 0px; vertical-align: bottom; visibility: hidden; display: none;"></iframe></div>
    </div>




  <div class="outer_page only_ie6_border        not_visible" id="outer_page_22" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="-webkit-transform: scale(0.7617823479006); -webkit-transform-origin: 0% 0%; display: none;"><div class="newpage" id="page22" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/22-a6a9b01449.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 22};

        pageParams.containerElem = document.getElementById("outer_page_22");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/22-a6a9b01449.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_22" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(22);
      </script>
    </div>




  <div class="outer_page only_ie6_border       not_visible" id="outer_page_23" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="-webkit-transform: scale(0.7617823479006); -webkit-transform-origin: 0% 0%; display: none;"><div class="newpage" id="page23" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/23-4c58766fa3.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 23};

        pageParams.containerElem = document.getElementById("outer_page_23");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/23-4c58766fa3.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_23" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(23);
      </script>
    </div>




  <div class="outer_page only_ie6_border       not_visible" id="outer_page_24" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(0.7617823479006); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page24" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/24-3068317511.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 24};

        pageParams.containerElem = document.getElementById("outer_page_24");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/24-3068317511.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_24" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(24);
      </script>
    </div>




  <div class="outer_page only_ie6_border     not_visible" id="outer_page_25" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="-webkit-transform: scale(0.7617823479006); -webkit-transform-origin: 0% 0%; display: none;"><div class="newpage" id="page25" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/25-eee4416536.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 25};

        pageParams.containerElem = document.getElementById("outer_page_25");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/25-eee4416536.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_25" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(25);
      </script>
    </div>




  <div class="outer_page only_ie6_border     not_visible" id="outer_page_26" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(0.7617823479006); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page26" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/26-c4662a9c28.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 26};

        pageParams.containerElem = document.getElementById("outer_page_26");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/26-c4662a9c28.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_26" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(26);
      </script>
    </div>




  <div class="outer_page only_ie6_border      not_visible" id="outer_page_27" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(0.7617823479006); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page27" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/27-6e02e7a7b6.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 27};

        pageParams.containerElem = document.getElementById("outer_page_27");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/27-6e02e7a7b6.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_27" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(27);
      </script>
    </div>




  <div class="outer_page only_ie6_border      not_visible" id="outer_page_28" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page28" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/28-a301f8d7ef.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 28};

        pageParams.containerElem = document.getElementById("outer_page_28");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/28-a301f8d7ef.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_28" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(28);
      </script>
    </div>




  <div class="outer_page only_ie6_border      not_visible" id="outer_page_29" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page29" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/29-2605c624d0.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 29};

        pageParams.containerElem = document.getElementById("outer_page_29");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/29-2605c624d0.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_29" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(29);
      </script>
    </div>




  <div class="outer_page only_ie6_border      not_visible" id="outer_page_30" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page30" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/30-3f1458f758.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 30};

        pageParams.containerElem = document.getElementById("outer_page_30");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/30-3f1458f758.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_30" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(30);
      </script>
    </div>




  <div class="outer_page only_ie6_border     not_visible" id="outer_page_31" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page31" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/31-8c967641df.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 31};

        pageParams.containerElem = document.getElementById("outer_page_31");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/31-8c967641df.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_31" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(31);
      </script>
    </div>




  <div class="outer_page only_ie6_border    not_visible" id="outer_page_32" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="-webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%; display: none;"><div class="newpage" id="page32" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/32-3b2327a517.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 32};

        pageParams.containerElem = document.getElementById("outer_page_32");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/32-3b2327a517.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_32" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(32);
      </script>
    </div>




  <div class="outer_page only_ie6_border      not_visible" id="outer_page_33" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page33" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/33-6b046bbb52.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 33};

        pageParams.containerElem = document.getElementById("outer_page_33");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/33-6b046bbb52.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_33" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(33);
      </script>
    </div>




  <div class="outer_page only_ie6_border     not_visible" id="outer_page_34" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page34" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/34-bacc706b09.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 34};

        pageParams.containerElem = document.getElementById("outer_page_34");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/34-bacc706b09.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_34" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(34);
      </script>
    </div>




  <div class="outer_page only_ie6_border     not_visible" id="outer_page_35" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page35" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/35-6aeb2ea2f5.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 35};

        pageParams.containerElem = document.getElementById("outer_page_35");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/35-6aeb2ea2f5.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_35" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(35);
      </script>
    </div>




  <div class="outer_page only_ie6_border      not_visible" id="outer_page_36" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page36" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/36-f60b13d722.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 36};

        pageParams.containerElem = document.getElementById("outer_page_36");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/36-f60b13d722.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_36" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(36);
      </script>
    </div>




  <div class="outer_page only_ie6_border   not_visible" id="outer_page_37" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page37" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/37-d53bdac0e6.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 37};

        pageParams.containerElem = document.getElementById("outer_page_37");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/37-d53bdac0e6.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_37" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(37);
      </script>
    </div>




  <div class="outer_page only_ie6_border   not_visible" id="outer_page_38" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page38" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/38-ebb004de9a.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 38};

        pageParams.containerElem = document.getElementById("outer_page_38");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/38-ebb004de9a.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_38" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(38);
      </script>
    </div>




  <div class="outer_page only_ie6_border   not_visible" id="outer_page_39" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page39" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/39-2ed3c92f88.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 39};

        pageParams.containerElem = document.getElementById("outer_page_39");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/39-2ed3c92f88.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_39" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(39);
      </script>
    </div>




  <div class="outer_page only_ie6_border   not_visible" id="outer_page_40" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page40" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/40-b21f3e9182.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 40};

        pageParams.containerElem = document.getElementById("outer_page_40");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/40-b21f3e9182.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_40" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(40);
      </script>
    </div>




  <div class="outer_page only_ie6_border    not_visible" id="outer_page_41" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page41" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1004px; height: 798px; clip: rect(1px 1003px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/41-16a3520482.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 41};

        pageParams.containerElem = document.getElementById("outer_page_41");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/41-16a3520482.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_41" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(41);
      </script>
    </div>




  <div class="outer_page only_ie6_border   not_visible" id="outer_page_42" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page42" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/42-f3ff93041f.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 42};

        pageParams.containerElem = document.getElementById("outer_page_42");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/42-f3ff93041f.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_42" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(42);
      </script>
    </div>




  <div class="outer_page only_ie6_border   not_visible" id="outer_page_43" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page43" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/43-76068ae1aa.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 43};

        pageParams.containerElem = document.getElementById("outer_page_43");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/43-76068ae1aa.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_43" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(43);
      </script>
    </div>




  <div class="outer_page only_ie6_border   not_visible" id="outer_page_44" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page44" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/44-76ba85ba36.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 44};

        pageParams.containerElem = document.getElementById("outer_page_44");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/44-76ba85ba36.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_44" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(44);
      </script>
    </div>




  <div class="outer_page only_ie6_border   not_visible" id="outer_page_45" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page45" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/45-309c8c4ef6.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 45};

        pageParams.containerElem = document.getElementById("outer_page_45");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/45-309c8c4ef6.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_45" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(45);
      </script>
    </div>




  <div class="outer_page only_ie6_border  not_visible" id="outer_page_46" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none;"><div class="newpage" id="page46" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/46-8ea754574f.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 46};

        pageParams.containerElem = document.getElementById("outer_page_46");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/46-8ea754574f.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_46" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(46);
      </script>
    </div>




  <div class="outer_page only_ie6_border  not_visible" id="outer_page_47" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none;"><div class="newpage" id="page47" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/47-617cb3e7c6.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 47};

        pageParams.containerElem = document.getElementById("outer_page_47");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/47-617cb3e7c6.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_47" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(47);
      </script>
    </div>




  <div class="outer_page only_ie6_border  not_visible" id="outer_page_48" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none;"><div class="newpage" id="page48" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/48-b621f5ac78.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 48};

        pageParams.containerElem = document.getElementById("outer_page_48");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/48-b621f5ac78.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_48" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(48);
      </script>
    </div>




  <div class="outer_page only_ie6_border  not_visible" id="outer_page_49" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none;"><div class="newpage" id="page49" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/49-dc96932ca0.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 49};

        pageParams.containerElem = document.getElementById("outer_page_49");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/49-dc96932ca0.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_49" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(49);
      </script>
    </div>




  <div class="outer_page only_ie6_border   not_visible" id="outer_page_50" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page50" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/50-b81ff840f1.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 50};

        pageParams.containerElem = document.getElementById("outer_page_50");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/50-b81ff840f1.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_50" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(50);
      </script>
    </div>




  <div class="outer_page only_ie6_border   not_visible" id="outer_page_51" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page51" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/51-94301e68b6.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 51};

        pageParams.containerElem = document.getElementById("outer_page_51");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/51-94301e68b6.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_51" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(51);
      </script>
    </div>




  <div class="outer_page only_ie6_border   not_visible" id="outer_page_52" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page52" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/52-2bf4c2cb38.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 52};

        pageParams.containerElem = document.getElementById("outer_page_52");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/52-2bf4c2cb38.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_52" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(52);
      </script>
    </div>




  <div class="outer_page only_ie6_border   not_visible" id="outer_page_53" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page53" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/53-08684aadca.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 53};

        pageParams.containerElem = document.getElementById("outer_page_53");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/53-08684aadca.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_53" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(53);
      </script>
    </div>




  <div class="outer_page only_ie6_border   not_visible" id="outer_page_54" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page54" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/54-5d2faa4e8c.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 54};

        pageParams.containerElem = document.getElementById("outer_page_54");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/54-5d2faa4e8c.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_54" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(54);
      </script>
    </div>




  <div class="outer_page only_ie6_border  not_visible" id="outer_page_55" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none;"><div class="newpage" id="page55" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/55-b8036c8499.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 55};

        pageParams.containerElem = document.getElementById("outer_page_55");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/55-b8036c8499.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_55" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(55);
      </script>
    </div>




  <div class="outer_page only_ie6_border  not_visible" id="outer_page_56" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none;"><div class="newpage" id="page56" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/56-abbce7d051.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 56};

        pageParams.containerElem = document.getElementById("outer_page_56");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/56-abbce7d051.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_56" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(56);
      </script>
    </div>




  <div class="outer_page only_ie6_border  not_visible" id="outer_page_57" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none;"><div class="newpage" id="page57" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/57-9bae891833.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 57};

        pageParams.containerElem = document.getElementById("outer_page_57");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/57-9bae891833.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_57" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(57);
      </script>
    </div>




  <div class="outer_page only_ie6_border  not_visible" id="outer_page_58" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none;"><div class="newpage" id="page58" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/58-4f68d7583e.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 58};

        pageParams.containerElem = document.getElementById("outer_page_58");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/58-4f68d7583e.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_58" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(58);
      </script>
    </div>




  <div class="outer_page only_ie6_border  not_visible" id="outer_page_59" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none;"><div class="newpage" id="page59" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/59-3c23f45b1b.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 59};

        pageParams.containerElem = document.getElementById("outer_page_59");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/59-3c23f45b1b.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_59" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(59);
      </script>
    </div>




  <div class="outer_page only_ie6_border  not_visible" id="outer_page_60" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none;"><div class="newpage" id="page60" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/60-752f4e210b.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 60};

        pageParams.containerElem = document.getElementById("outer_page_60");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/60-752f4e210b.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_60" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(60);
      </script>
    </div>




  <div class="outer_page only_ie6_border  not_visible" id="outer_page_61" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none;"><div class="newpage" id="page61" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/61-94b0104183.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 61};

        pageParams.containerElem = document.getElementById("outer_page_61");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/61-94b0104183.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_61" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(61);
      </script>
    </div>




  <div class="outer_page only_ie6_border  not_visible" id="outer_page_62" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none;"><div class="newpage" id="page62" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/62-23e38c7a4a.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 62};

        pageParams.containerElem = document.getElementById("outer_page_62");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/62-23e38c7a4a.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_62" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(62);
      </script>
    </div>




  <div class="outer_page only_ie6_border  not_visible" id="outer_page_63" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none;"><div class="newpage" id="page63" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/63-fe4cbf5958.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 63};

        pageParams.containerElem = document.getElementById("outer_page_63");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/63-fe4cbf5958.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_63" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(63);
      </script>
    </div>




  <div class="outer_page only_ie6_border  not_visible" id="outer_page_64" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none;"><div class="newpage" id="page64" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/64-8a412df80f.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 64};

        pageParams.containerElem = document.getElementById("outer_page_64");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/64-8a412df80f.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_64" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(64);
      </script>
    </div>




  <div class="outer_page only_ie6_border  not_visible" id="outer_page_65" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none;"><div class="newpage" id="page65" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/65-f4e1289ab0.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 65};

        pageParams.containerElem = document.getElementById("outer_page_65");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/65-f4e1289ab0.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_65" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(65);
      </script>
    </div>




  <div class="outer_page only_ie6_border  not_visible" id="outer_page_66" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none;"><div class="newpage" id="page66" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/66-ef40c567a5.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 66};

        pageParams.containerElem = document.getElementById("outer_page_66");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/66-ef40c567a5.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_66" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(66);
      </script>
    </div>




  <div class="outer_page only_ie6_border  not_visible" id="outer_page_67" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none;"><div class="newpage" id="page67" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/67-ead0271069.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 67};

        pageParams.containerElem = document.getElementById("outer_page_67");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/67-ead0271069.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_67" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(67);
      </script>
    </div>




  <div class="outer_page only_ie6_border   not_visible" id="outer_page_68" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page68" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/68-d8ffaae0f9.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 68};

        pageParams.containerElem = document.getElementById("outer_page_68");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/68-d8ffaae0f9.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_68" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(68);
      </script>
    </div>




  <div class="outer_page only_ie6_border   not_visible" id="outer_page_69" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page69" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/69-50846476ae.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 69};

        pageParams.containerElem = document.getElementById("outer_page_69");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/69-50846476ae.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_69" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(69);
      </script>
    </div>




  <div class="outer_page only_ie6_border  not_visible" id="outer_page_70" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none;"><div class="newpage" id="page70" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/70-90b25339a3.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 70};

        pageParams.containerElem = document.getElementById("outer_page_70");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/70-90b25339a3.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_70" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(70);
      </script>
    </div>




  <div class="outer_page only_ie6_border  not_visible" id="outer_page_71" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none;"><div class="newpage" id="page71" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/71-13f5061037.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 71};

        pageParams.containerElem = document.getElementById("outer_page_71");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/71-13f5061037.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_71" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(71);
      </script>
    </div>




  <div class="outer_page only_ie6_border  not_visible" id="outer_page_72" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none;"><div class="newpage" id="page72" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/72-aff200dc46.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 72};

        pageParams.containerElem = document.getElementById("outer_page_72");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/72-aff200dc46.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_72" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(72);
      </script>
    </div>




  <div class="outer_page only_ie6_border  not_visible" id="outer_page_73" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none;"><div class="newpage" id="page73" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/73-3f306354a9.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 73};

        pageParams.containerElem = document.getElementById("outer_page_73");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/73-3f306354a9.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_73" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(73);
      </script>
    </div>




  <div class="outer_page only_ie6_border  not_visible" id="outer_page_74" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none;"><div class="newpage" id="page74" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/74-660d1b5f5b.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 74};

        pageParams.containerElem = document.getElementById("outer_page_74");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/74-660d1b5f5b.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_74" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(74);
      </script>
    </div>




  <div class="outer_page only_ie6_border  not_visible" id="outer_page_75" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none;"><div class="newpage" id="page75" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/75-1b0010cf4d.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 75};

        pageParams.containerElem = document.getElementById("outer_page_75");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/75-1b0010cf4d.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_75" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(75);
      </script>
    </div>




  <div class="outer_page only_ie6_border  not_visible" id="outer_page_76" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none;"><div class="newpage" id="page76" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/76-e01aef4606.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 76};

        pageParams.containerElem = document.getElementById("outer_page_76");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/76-e01aef4606.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_76" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(76);
      </script>
    </div>




  <div class="outer_page only_ie6_border   not_visible" id="outer_page_77" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page77" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/77-33283fa6f5.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 77};

        pageParams.containerElem = document.getElementById("outer_page_77");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/77-33283fa6f5.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_77" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(77);
      </script>
    </div>




  <div class="outer_page only_ie6_border   not_visible" id="outer_page_78" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page78" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/78-fe95eee347.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 78};

        pageParams.containerElem = document.getElementById("outer_page_78");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/78-fe95eee347.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_78" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(78);
      </script>
    </div>




  <div class="outer_page only_ie6_border   not_visible" id="outer_page_79" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page79" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/79-ad6ef2284f.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 79};

        pageParams.containerElem = document.getElementById("outer_page_79");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/79-ad6ef2284f.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_79" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(79);
      </script>
    </div>




  <div class="outer_page only_ie6_border   not_visible" id="outer_page_80" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page80" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/80-744aec7216.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 80};

        pageParams.containerElem = document.getElementById("outer_page_80");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/80-744aec7216.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_80" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(80);
      </script>
    </div>




  <div class="outer_page only_ie6_border   not_visible" id="outer_page_81" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page81" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/81-6387a28e2b.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 81};

        pageParams.containerElem = document.getElementById("outer_page_81");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/81-6387a28e2b.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_81" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(81);
      </script>
    </div>




  <div class="outer_page only_ie6_border   not_visible" id="outer_page_82" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page82" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/82-4f13f6a1bb.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 82};

        pageParams.containerElem = document.getElementById("outer_page_82");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/82-4f13f6a1bb.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_82" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(82);
      </script>
    </div>




  <div class="outer_page only_ie6_border  not_visible" id="outer_page_83" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none;"><div class="newpage" id="page83" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/83-4b8274bda9.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 83};

        pageParams.containerElem = document.getElementById("outer_page_83");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/83-4b8274bda9.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_83" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(83);
      </script>
    </div>




  <div class="outer_page only_ie6_border  not_visible" id="outer_page_84" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none;"><div class="newpage" id="page84" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/84-34b855a77d.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 84};

        pageParams.containerElem = document.getElementById("outer_page_84");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/84-34b855a77d.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_84" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(84);
      </script>
    </div>




  <div class="outer_page only_ie6_border  not_visible" id="outer_page_85" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none;"><div class="newpage" id="page85" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/85-50532f08eb.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 85};

        pageParams.containerElem = document.getElementById("outer_page_85");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/85-50532f08eb.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_85" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(85);
      </script>
    </div>




  <div class="outer_page only_ie6_border  not_visible" id="outer_page_86" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none;"><div class="newpage" id="page86" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/86-70cd899f93.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 86};

        pageParams.containerElem = document.getElementById("outer_page_86");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/86-70cd899f93.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_86" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(86);
      </script>
    </div>




  <div class="outer_page only_ie6_border  not_visible" id="outer_page_87" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none;"><div class="newpage" id="page87" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/87-e22a6e307e.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 87};

        pageParams.containerElem = document.getElementById("outer_page_87");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/87-e22a6e307e.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_87" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(87);
      </script>
    </div>




  <div class="outer_page only_ie6_border  not_visible" id="outer_page_88" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none;"><div class="newpage" id="page88" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/88-0c85c24e74.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 88};

        pageParams.containerElem = document.getElementById("outer_page_88");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/88-0c85c24e74.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_88" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(88);
      </script>
    </div>




  <div class="outer_page only_ie6_border  not_visible" id="outer_page_89" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none;"><div class="newpage" id="page89" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/89-b6770275d9.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 89};

        pageParams.containerElem = document.getElementById("outer_page_89");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/89-b6770275d9.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_89" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(89);
      </script>
    </div>




  <div class="outer_page only_ie6_border  not_visible" id="outer_page_90" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none;"><div class="newpage" id="page90" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/90-3e6b9bf534.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 90};

        pageParams.containerElem = document.getElementById("outer_page_90");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/90-3e6b9bf534.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_90" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(90);
      </script>
    </div>




  <div class="outer_page only_ie6_border  not_visible" id="outer_page_91" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none;"><div class="newpage" id="page91" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/91-952a454e43.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 91};

        pageParams.containerElem = document.getElementById("outer_page_91");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/91-952a454e43.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_91" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(91);
      </script>
    </div>




  <div class="outer_page only_ie6_border  not_visible" id="outer_page_92" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none;"><div class="newpage" id="page92" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/92-5675838b73.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 92};

        pageParams.containerElem = document.getElementById("outer_page_92");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/92-5675838b73.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_92" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(92);
      </script>
    </div>




  <div class="outer_page only_ie6_border  not_visible" id="outer_page_93" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none;"><div class="newpage" id="page93" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/93-70b0c3b78f.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 93};

        pageParams.containerElem = document.getElementById("outer_page_93");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/93-70b0c3b78f.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_93" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(93);
      </script>
    </div>




  <div class="outer_page only_ie6_border  not_visible" id="outer_page_94" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none;"><div class="newpage" id="page94" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/94-0c3ab514e2.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 94};

        pageParams.containerElem = document.getElementById("outer_page_94");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/94-0c3ab514e2.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_94" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(94);
      </script>
    </div>




  <div class="outer_page only_ie6_border  not_visible" id="outer_page_95" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none;"><div class="newpage" id="page95" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/95-13e61ccdf8.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 95};

        pageParams.containerElem = document.getElementById("outer_page_95");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/95-13e61ccdf8.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_95" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(95);
      </script>
    </div>




  <div class="outer_page only_ie6_border  not_visible" id="outer_page_96" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none;"><div class="newpage" id="page96" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/96-01be20f9d3.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 96};

        pageParams.containerElem = document.getElementById("outer_page_96");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/96-01be20f9d3.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_96" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(96);
      </script>
    </div>




  <div class="outer_page only_ie6_border  not_visible" id="outer_page_97" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none;"><div class="newpage" id="page97" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/97-8ccdb740e3.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 97};

        pageParams.containerElem = document.getElementById("outer_page_97");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/97-8ccdb740e3.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_97" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(97);
      </script>
    </div>




  <div class="outer_page only_ie6_border  not_visible" id="outer_page_98" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none;"><div class="newpage" id="page98" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/98-d8eb4df223.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 98};

        pageParams.containerElem = document.getElementById("outer_page_98");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/98-d8eb4df223.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_98" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(98);
      </script>
    </div>




  <div class="outer_page only_ie6_border  not_visible" id="outer_page_99" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none;"><div class="newpage" id="page99" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/99-9bf4dfe804.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 99};

        pageParams.containerElem = document.getElementById("outer_page_99");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/99-9bf4dfe804.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_99" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(99);
      </script>
    </div>




  <div class="outer_page only_ie6_border  not_visible" id="outer_page_100" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none;"><div class="newpage" id="page100" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/100-19267e7b76.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 100};

        pageParams.containerElem = document.getElementById("outer_page_100");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/100-19267e7b76.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_100" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(100);
      </script>
    </div>




  <div class="outer_page only_ie6_border   not_visible" id="outer_page_101" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page101" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/101-9359a34177.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 101};

        pageParams.containerElem = document.getElementById("outer_page_101");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/101-9359a34177.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_101" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(101);
      </script>
    </div>




  <div class="outer_page only_ie6_border   not_visible" id="outer_page_102" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page102" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/102-1bba568d23.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 102};

        pageParams.containerElem = document.getElementById("outer_page_102");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/102-1bba568d23.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_102" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(102);
      </script>
    </div>




  <div class="outer_page only_ie6_border   not_visible" id="outer_page_103" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page103" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/103-6d9af4bb21.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 103};

        pageParams.containerElem = document.getElementById("outer_page_103");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/103-6d9af4bb21.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_103" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(103);
      </script>
    </div>




  <div class="outer_page only_ie6_border  not_visible" id="outer_page_104" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none;"><div class="newpage" id="page104" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/104-c6075de283.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 104};

        pageParams.containerElem = document.getElementById("outer_page_104");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/104-c6075de283.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_104" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(104);
      </script>
    </div>




  <div class="outer_page only_ie6_border  not_visible" id="outer_page_105" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none;"><div class="newpage" id="page105" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/105-612e099ff6.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 105};

        pageParams.containerElem = document.getElementById("outer_page_105");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/105-612e099ff6.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_105" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(105);
      </script>
    </div>




  <div class="outer_page only_ie6_border  not_visible" id="outer_page_106" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none;"><div class="newpage" id="page106" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/106-2c3dae31d7.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 106};

        pageParams.containerElem = document.getElementById("outer_page_106");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/106-2c3dae31d7.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_106" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(106);
      </script>
    </div>




  <div class="outer_page only_ie6_border  not_visible" id="outer_page_107" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none;"><div class="newpage" id="page107" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/107-7d0cf2bf76.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 107};

        pageParams.containerElem = document.getElementById("outer_page_107");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/107-7d0cf2bf76.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_107" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(107);
      </script>
    </div>




  <div class="outer_page only_ie6_border  not_visible" id="outer_page_108" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none;"><div class="newpage" id="page108" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/108-1344d60b5a.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 108};

        pageParams.containerElem = document.getElementById("outer_page_108");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/108-1344d60b5a.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_108" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(108);
      </script>
    </div>




  <div class="outer_page only_ie6_border   not_visible" id="outer_page_109" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page109" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/109-7374aef45a.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 109};

        pageParams.containerElem = document.getElementById("outer_page_109");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/109-7374aef45a.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_109" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(109);
      </script>
    </div>




  <div class="outer_page only_ie6_border   not_visible" id="outer_page_110" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page110" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/110-f11ebfde20.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 110};

        pageParams.containerElem = document.getElementById("outer_page_110");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/110-f11ebfde20.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_110" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(110);
      </script>
    </div>




  <div class="outer_page only_ie6_border   not_visible" id="outer_page_111" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page111" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/111-0dcf89e6ee.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 111};

        pageParams.containerElem = document.getElementById("outer_page_111");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/111-0dcf89e6ee.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_111" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(111);
      </script>
    </div>




  <div class="outer_page only_ie6_border   not_visible" id="outer_page_112" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page112" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/112-80e3bae495.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 112};

        pageParams.containerElem = document.getElementById("outer_page_112");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/112-80e3bae495.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_112" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(112);
      </script>
    </div>




  <div class="outer_page only_ie6_border   not_visible" id="outer_page_113" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page113" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/113-3e68e8af19.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 113};

        pageParams.containerElem = document.getElementById("outer_page_113");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/113-3e68e8af19.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_113" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(113);
      </script>
    </div>




  <div class="outer_page only_ie6_border    not_visible" id="outer_page_114" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page114" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/114-e618ccd2bb.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 114};

        pageParams.containerElem = document.getElementById("outer_page_114");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/114-e618ccd2bb.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_114" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(114);
      </script>
    </div>




  <div class="outer_page only_ie6_border    not_visible" id="outer_page_115" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page115" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/115-f062668982.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 115};

        pageParams.containerElem = document.getElementById("outer_page_115");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/115-f062668982.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_115" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(115);
      </script>
    </div>




  <div class="outer_page only_ie6_border     not_visible" id="outer_page_116" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page116" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/116-09a2840335.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 116};

        pageParams.containerElem = document.getElementById("outer_page_116");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/116-09a2840335.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_116" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(116);
      </script>
    </div>




  <div class="outer_page only_ie6_border    not_visible" id="outer_page_117" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page117" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/117-073a5cc6af.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 117};

        pageParams.containerElem = document.getElementById("outer_page_117");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/117-073a5cc6af.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_117" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(117);
      </script>
    </div>




  <div class="outer_page only_ie6_border    not_visible" id="outer_page_118" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page118" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/118-821d1a7c61.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 118};

        pageParams.containerElem = document.getElementById("outer_page_118");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/118-821d1a7c61.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_118" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(118);
      </script>
    </div>




  <div class="outer_page only_ie6_border    not_visible" id="outer_page_119" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page119" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/119-35f334bece.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 119};

        pageParams.containerElem = document.getElementById("outer_page_119");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/119-35f334bece.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_119" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(119);
      </script>
    </div>




  <div class="outer_page only_ie6_border     not_visible" id="outer_page_120" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page120" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/120-89d83a999e.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 120};

        pageParams.containerElem = document.getElementById("outer_page_120");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/120-89d83a999e.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_120" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(120);
      </script>
    </div>




  <div class="outer_page only_ie6_border      not_visible" id="outer_page_121" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page121" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/121-90e11d18e7.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 121};

        pageParams.containerElem = document.getElementById("outer_page_121");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/121-90e11d18e7.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_121" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(121);
      </script>
    </div>




  <div class="outer_page only_ie6_border      " id="outer_page_122" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: block; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page122" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/122-0f5b62064d.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 122};

        pageParams.containerElem = document.getElementById("outer_page_122");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/122-0f5b62064d.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_122" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(122);
      </script>
    </div>




  <div class="outer_page only_ie6_border      " id="outer_page_123" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: block; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page123" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/123-6237218b2b.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 123};

        pageParams.containerElem = document.getElementById("outer_page_123");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/123-6237218b2b.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_123" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(123);
      </script>
    </div>




  <div class="outer_page only_ie6_border      " id="outer_page_124" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: block; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page124" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/124-bf47f13255.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 124};

        pageParams.containerElem = document.getElementById("outer_page_124");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/124-bf47f13255.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_124" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(124);
      </script>
    </div>




  <div class="outer_page only_ie6_border     " id="outer_page_125" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: block; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page125" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/125-346443d53b.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 125};

        pageParams.containerElem = document.getElementById("outer_page_125");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/125-346443d53b.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_125" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(125);
      </script>
    </div>




  <div class="outer_page only_ie6_border     " id="outer_page_126" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: block; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page126" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/126-eb492a1577.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 126};

        pageParams.containerElem = document.getElementById("outer_page_126");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/126-eb492a1577.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_126" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(126);
      </script>
    </div>




  <div class="outer_page only_ie6_border       not_visible" id="outer_page_127" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page127" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/127-68d1d1cb16.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 127};

        pageParams.containerElem = document.getElementById("outer_page_127");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/127-68d1d1cb16.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_127" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(127);
      </script>
    </div>




  <div class="outer_page only_ie6_border      not_visible" id="outer_page_128" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page128" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/128-8bf1506b61.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 128};

        pageParams.containerElem = document.getElementById("outer_page_128");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/128-8bf1506b61.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_128" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(128);
      </script>
    </div>




  <div class="outer_page only_ie6_border      not_visible" id="outer_page_129" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page129" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/129-7248544736.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 129};

        pageParams.containerElem = document.getElementById("outer_page_129");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/129-7248544736.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_129" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(129);
      </script>
    </div>




  <div class="outer_page only_ie6_border   not_visible" id="outer_page_130" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page130" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/130-1a2d997470.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 130};

        pageParams.containerElem = document.getElementById("outer_page_130");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/130-1a2d997470.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_130" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(130);
      </script>
    </div>




  <div class="outer_page only_ie6_border  not_visible" id="outer_page_131" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none;"><div class="newpage" id="page131" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/131-72cc7d34d9.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 131};

        pageParams.containerElem = document.getElementById("outer_page_131");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/131-72cc7d34d9.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_131" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(131);
      </script>
    </div>




  <div class="outer_page only_ie6_border  not_visible" id="outer_page_132" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none;"><div class="newpage" id="page132" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/132-e75058b4f3.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 132};

        pageParams.containerElem = document.getElementById("outer_page_132");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/132-e75058b4f3.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_132" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(132);
      </script>
    </div>




  <div class="outer_page only_ie6_border  not_visible" id="outer_page_133" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none;"><div class="newpage" id="page133" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/133-f7295af3a5.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 133};

        pageParams.containerElem = document.getElementById("outer_page_133");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/133-f7295af3a5.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_133" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(133);
      </script>
    </div>




  <div class="outer_page only_ie6_border   not_visible" id="outer_page_134" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="-webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%; display: none;"><div class="newpage" id="page134" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/134-724706bdad.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 134};

        pageParams.containerElem = document.getElementById("outer_page_134");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/134-724706bdad.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_134" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(134);
      </script>
    </div>




  <div class="outer_page only_ie6_border  not_visible" id="outer_page_135" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none;"><div class="newpage" id="page135" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/135-b5e1582e30.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 135};

        pageParams.containerElem = document.getElementById("outer_page_135");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/135-b5e1582e30.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_135" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(135);
      </script>
    </div>




  <div class="outer_page only_ie6_border   not_visible" id="outer_page_136" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="-webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%; display: none;"><div class="newpage" id="page136" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/136-d2fd2f02bc.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 136};

        pageParams.containerElem = document.getElementById("outer_page_136");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/136-d2fd2f02bc.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_136" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(136);
      </script>
    </div>




  <div class="outer_page only_ie6_border  not_visible" id="outer_page_137" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none;"><div class="newpage" id="page137" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/137-57669d913d.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 137};

        pageParams.containerElem = document.getElementById("outer_page_137");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/137-57669d913d.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_137" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(137);
      </script>
    </div>




  <div class="outer_page only_ie6_border     not_visible" id="outer_page_138" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page138" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/138-aa02c1e27f.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 138};

        pageParams.containerElem = document.getElementById("outer_page_138");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/138-aa02c1e27f.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_138" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(138);
      </script>
    </div>




  <div class="outer_page only_ie6_border     not_visible" id="outer_page_139" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page139" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/139-4ee1225c4c.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 139};

        pageParams.containerElem = document.getElementById("outer_page_139");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/139-4ee1225c4c.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_139" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(139);
      </script>
    </div>




  <div class="outer_page only_ie6_border     not_visible" id="outer_page_140" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page140" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/140-1a49af815d.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 140};

        pageParams.containerElem = document.getElementById("outer_page_140");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/140-1a49af815d.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_140" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(140);
      </script>
    </div>




  <div class="outer_page only_ie6_border      not_visible" id="outer_page_141" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page141" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/141-537db07bf4.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 141};

        pageParams.containerElem = document.getElementById("outer_page_141");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/141-537db07bf4.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_141" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(141);
      </script>
    </div>




  <div class="outer_page only_ie6_border      not_visible" id="outer_page_142" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page142" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/142-a45a87fdf3.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 142};

        pageParams.containerElem = document.getElementById("outer_page_142");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/142-a45a87fdf3.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_142" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(142);
      </script>
    </div>




  <div class="outer_page only_ie6_border      not_visible" id="outer_page_143" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page143" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/143-77d006d7a7.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 143};

        pageParams.containerElem = document.getElementById("outer_page_143");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/143-77d006d7a7.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_143" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(143);
      </script>
    </div>




  <div class="outer_page only_ie6_border     not_visible" id="outer_page_144" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page144" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/144-0bbb1ee950.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 144};

        pageParams.containerElem = document.getElementById("outer_page_144");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/144-0bbb1ee950.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_144" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(144);
      </script>
    </div>




  <div class="outer_page only_ie6_border     not_visible" id="outer_page_145" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page145" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/145-06c4ab7136.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 145};

        pageParams.containerElem = document.getElementById("outer_page_145");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/145-06c4ab7136.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_145" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(145);
      </script>
    </div>




  <div class="outer_page only_ie6_border    not_visible" id="outer_page_146" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page146" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/146-8a6e362d62.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 146};

        pageParams.containerElem = document.getElementById("outer_page_146");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/146-8a6e362d62.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_146" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(146);
      </script>
    </div>




  <div class="outer_page only_ie6_border    not_visible" id="outer_page_147" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page147" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/147-9b21768c38.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 147};

        pageParams.containerElem = document.getElementById("outer_page_147");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/147-9b21768c38.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_147" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(147);
      </script>
    </div>




  <div class="outer_page only_ie6_border    not_visible" id="outer_page_148" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page148" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/148-1179348074.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 148};

        pageParams.containerElem = document.getElementById("outer_page_148");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/148-1179348074.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_148" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(148);
      </script>
    </div>




  <div class="outer_page only_ie6_border    not_visible" id="outer_page_149" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page149" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/149-ffa12c9181.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 149};

        pageParams.containerElem = document.getElementById("outer_page_149");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/149-ffa12c9181.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_149" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(149);
      </script>
    </div>




  <div class="outer_page only_ie6_border    not_visible" id="outer_page_150" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page150" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/150-0bdcc38088.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 150};

        pageParams.containerElem = document.getElementById("outer_page_150");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/150-0bdcc38088.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_150" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(150);
      </script>
    </div>




  <div class="outer_page only_ie6_border  not_visible" id="outer_page_151" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none;"><div class="newpage" id="page151" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/151-c965835f25.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 151};

        pageParams.containerElem = document.getElementById("outer_page_151");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/151-c965835f25.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_151" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(151);
      </script>
    </div>




  <div class="outer_page only_ie6_border   not_visible" id="outer_page_152" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page152" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/152-8c034f894e.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 152};

        pageParams.containerElem = document.getElementById("outer_page_152");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/152-8c034f894e.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_152" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(152);
      </script>
    </div>




  <div class="outer_page only_ie6_border   not_visible" id="outer_page_153" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page153" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/153-dd41d0c7c6.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 153};

        pageParams.containerElem = document.getElementById("outer_page_153");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/153-dd41d0c7c6.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_153" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(153);
      </script>
    </div>




  <div class="outer_page only_ie6_border   not_visible" id="outer_page_154" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page154" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/154-c8935a8ab3.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 154};

        pageParams.containerElem = document.getElementById("outer_page_154");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/154-c8935a8ab3.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_154" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(154);
      </script>
    </div>




  <div class="outer_page only_ie6_border   not_visible" id="outer_page_155" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page155" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/155-9d3425bc85.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 155};

        pageParams.containerElem = document.getElementById("outer_page_155");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/155-9d3425bc85.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_155" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(155);
      </script>
    </div>




  <div class="outer_page only_ie6_border   not_visible" id="outer_page_156" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page156" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/156-cd50bd7349.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 156};

        pageParams.containerElem = document.getElementById("outer_page_156");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/156-cd50bd7349.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_156" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(156);
      </script>
    </div>




  <div class="outer_page only_ie6_border    not_visible" id="outer_page_157" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page157" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/157-40842d43ad.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 157};

        pageParams.containerElem = document.getElementById("outer_page_157");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/157-40842d43ad.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_157" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(157);
      </script>
    </div>




  <div class="outer_page only_ie6_border   not_visible" id="outer_page_158" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page158" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/158-bb79580fbc.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 158};

        pageParams.containerElem = document.getElementById("outer_page_158");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/158-bb79580fbc.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_158" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(158);
      </script>
    </div>




  <div class="outer_page only_ie6_border   not_visible" id="outer_page_159" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page159" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/159-63ebc15779.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 159};

        pageParams.containerElem = document.getElementById("outer_page_159");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/159-63ebc15779.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_159" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(159);
      </script>
    </div>




  <div class="outer_page only_ie6_border   not_visible" id="outer_page_160" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page160" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/160-a2a696e8d0.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 160};

        pageParams.containerElem = document.getElementById("outer_page_160");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/160-a2a696e8d0.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_160" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(160);
      </script>
    </div>




  <div class="outer_page only_ie6_border    not_visible" id="outer_page_161" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page161" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/161-98895fbee4.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 161};

        pageParams.containerElem = document.getElementById("outer_page_161");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/161-98895fbee4.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_161" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(161);
      </script>
    </div>




  <div class="outer_page only_ie6_border    not_visible" id="outer_page_162" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page162" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/162-1914bbab32.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 162};

        pageParams.containerElem = document.getElementById("outer_page_162");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/162-1914bbab32.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_162" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(162);
      </script>
    </div>




  <div class="outer_page only_ie6_border    not_visible" id="outer_page_163" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page163" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/163-f43c6d537b.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 163};

        pageParams.containerElem = document.getElementById("outer_page_163");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/163-f43c6d537b.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_163" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(163);
      </script>
    </div>




  <div class="outer_page only_ie6_border    not_visible" id="outer_page_164" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page164" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/164-a8700e9fec.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 164};

        pageParams.containerElem = document.getElementById("outer_page_164");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/164-a8700e9fec.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_164" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(164);
      </script>
    </div>




  <div class="outer_page only_ie6_border    not_visible" id="outer_page_165" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page165" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/165-dbaa963622.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 165};

        pageParams.containerElem = document.getElementById("outer_page_165");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/165-dbaa963622.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_165" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(165);
      </script>
    </div>




  <div class="outer_page only_ie6_border  not_visible" id="outer_page_166" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none;"><div class="newpage" id="page166" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/166-d6d033eab1.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 166};

        pageParams.containerElem = document.getElementById("outer_page_166");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/166-d6d033eab1.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_166" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(166);
      </script>
    </div>




  <div class="outer_page only_ie6_border  not_visible" id="outer_page_167" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none;"><div class="newpage" id="page167" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/167-8d69e44316.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 167};

        pageParams.containerElem = document.getElementById("outer_page_167");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/167-8d69e44316.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_167" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(167);
      </script>
    </div>




  <div class="outer_page only_ie6_border   not_visible" id="outer_page_168" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page168" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/168-f9b5421b00.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 168};

        pageParams.containerElem = document.getElementById("outer_page_168");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/168-f9b5421b00.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_168" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(168);
      </script>
    </div>




  <div class="outer_page only_ie6_border    not_visible" id="outer_page_169" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page169" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/169-524931af1f.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 169};

        pageParams.containerElem = document.getElementById("outer_page_169");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/169-524931af1f.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_169" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(169);
      </script>
    </div>




  <div class="outer_page only_ie6_border    not_visible" id="outer_page_170" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page170" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/170-797af4a40e.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 170};

        pageParams.containerElem = document.getElementById("outer_page_170");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/170-797af4a40e.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_170" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(170);
      </script>
    </div>




  <div class="outer_page only_ie6_border    not_visible" id="outer_page_171" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page171" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/171-b23e37a554.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 171};

        pageParams.containerElem = document.getElementById("outer_page_171");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/171-b23e37a554.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_171" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(171);
      </script>
    </div>




  <div class="outer_page only_ie6_border    not_visible" id="outer_page_172" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page172" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/172-2ab4b2341c.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 172};

        pageParams.containerElem = document.getElementById("outer_page_172");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/172-2ab4b2341c.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_172" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(172);
      </script>
    </div>




  <div class="outer_page only_ie6_border     not_visible" id="outer_page_173" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page173" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/173-d466582ca2.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 173};

        pageParams.containerElem = document.getElementById("outer_page_173");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/173-d466582ca2.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_173" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(173);
      </script>
    </div>




  <div class="outer_page only_ie6_border      not_visible" id="outer_page_174" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page174" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/174-545c78355c.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 174};

        pageParams.containerElem = document.getElementById("outer_page_174");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/174-545c78355c.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_174" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(174);
      </script>
    </div>




  <div class="outer_page only_ie6_border      not_visible" id="outer_page_175" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page175" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/175-26a8366366.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 175};

        pageParams.containerElem = document.getElementById("outer_page_175");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/175-26a8366366.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_175" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(175);
      </script>
    </div>




  <div class="outer_page only_ie6_border  not_visible" id="outer_page_176" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="-webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%; display: none;"><div class="newpage" id="page176" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/176-fef99e9ba2.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 176};

        pageParams.containerElem = document.getElementById("outer_page_176");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/176-fef99e9ba2.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_176" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(176);
      </script>
    </div>




  <div class="outer_page only_ie6_border      not_visible" id="outer_page_177" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page177" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/177-2e56a8c41e.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 177};

        pageParams.containerElem = document.getElementById("outer_page_177");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/177-2e56a8c41e.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_177" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(177);
      </script>
    </div>




  <div class="outer_page only_ie6_border     not_visible" id="outer_page_178" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page178" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/178-08738c28b8.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 178};

        pageParams.containerElem = document.getElementById("outer_page_178");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/178-08738c28b8.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_178" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(178);
      </script>
    </div>




  <div class="outer_page only_ie6_border     not_visible" id="outer_page_179" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page179" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/179-9786e20971.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 179};

        pageParams.containerElem = document.getElementById("outer_page_179");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/179-9786e20971.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_179" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(179);
      </script>
    </div>




  <div class="outer_page only_ie6_border     not_visible" id="outer_page_180" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page180" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/180-084094d62e.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 180};

        pageParams.containerElem = document.getElementById("outer_page_180");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/180-084094d62e.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_180" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(180);
      </script>
    </div>




  <div class="outer_page only_ie6_border     not_visible" id="outer_page_181" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page181" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/181-ecd43f0e0a.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 181};

        pageParams.containerElem = document.getElementById("outer_page_181");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/181-ecd43f0e0a.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_181" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(181);
      </script>
    </div>




  <div class="outer_page only_ie6_border      not_visible" id="outer_page_182" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page182" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/182-0ed1a79aff.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 182};

        pageParams.containerElem = document.getElementById("outer_page_182");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/182-0ed1a79aff.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_182" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(182);
      </script>
    </div>




  <div class="outer_page only_ie6_border       not_visible" id="outer_page_183" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page183" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/183-31dfc83f52.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 183};

        pageParams.containerElem = document.getElementById("outer_page_183");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/183-31dfc83f52.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_183" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(183);
      </script>
    </div>




  <div class="outer_page only_ie6_border       not_visible" id="outer_page_184" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page184" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/184-c8991f2988.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 184};

        pageParams.containerElem = document.getElementById("outer_page_184");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/184-c8991f2988.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_184" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(184);
      </script>
    </div>




  <div class="outer_page only_ie6_border       not_visible" id="outer_page_185" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page185" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/185-666b1ee316.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 185};

        pageParams.containerElem = document.getElementById("outer_page_185");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/185-666b1ee316.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_185" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(185);
      </script>
    </div>




  <div class="outer_page only_ie6_border        not_visible" id="outer_page_186" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page186" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/186-b00ce6722b.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 186};

        pageParams.containerElem = document.getElementById("outer_page_186");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/186-b00ce6722b.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_186" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(186);
      </script>
    </div>




  <div class="outer_page only_ie6_border        not_visible" id="outer_page_187" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page187" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/187-b3d5a56482.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 187};

        pageParams.containerElem = document.getElementById("outer_page_187");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/187-b3d5a56482.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_187" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(187);
      </script>
    </div>




  <div class="outer_page only_ie6_border       not_visible" id="outer_page_188" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page188" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/188-6d0b11e64f.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 188};

        pageParams.containerElem = document.getElementById("outer_page_188");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/188-6d0b11e64f.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_188" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(188);
      </script>
    </div>




  <div class="outer_page only_ie6_border      not_visible" id="outer_page_189" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page189" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/189-9d430c1d83.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 189};

        pageParams.containerElem = document.getElementById("outer_page_189");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/189-9d430c1d83.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_189" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(189);
      </script>
    </div>




  <div class="outer_page only_ie6_border      not_visible" id="outer_page_190" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page190" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/190-5d8e42d100.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 190};

        pageParams.containerElem = document.getElementById("outer_page_190");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/190-5d8e42d100.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_190" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(190);
      </script>
    </div>




  <div class="outer_page only_ie6_border     not_visible" id="outer_page_191" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page191" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/191-08e3e775a6.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 191};

        pageParams.containerElem = document.getElementById("outer_page_191");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/191-08e3e775a6.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_191" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(191);
      </script>
    </div>




  <div class="outer_page only_ie6_border    not_visible" id="outer_page_192" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page192" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/192-bd5216921c.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 192};

        pageParams.containerElem = document.getElementById("outer_page_192");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/192-bd5216921c.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_192" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(192);
      </script>
    </div>




  <div class="outer_page only_ie6_border    not_visible" id="outer_page_193" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page193" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/193-4b561dff26.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 193};

        pageParams.containerElem = document.getElementById("outer_page_193");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/193-4b561dff26.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_193" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(193);
      </script>
    </div>




  <div class="outer_page only_ie6_border    not_visible" id="outer_page_194" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page194" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/194-d034f129fb.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 194};

        pageParams.containerElem = document.getElementById("outer_page_194");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/194-d034f129fb.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_194" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(194);
      </script>
    </div>




  <div class="outer_page only_ie6_border   not_visible" id="outer_page_195" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page195" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/195-e328ea770b.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 195};

        pageParams.containerElem = document.getElementById("outer_page_195");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/195-e328ea770b.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_195" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(195);
      </script>
    </div>




  <div class="outer_page only_ie6_border   not_visible" id="outer_page_196" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page196" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/196-4cc67763e8.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 196};

        pageParams.containerElem = document.getElementById("outer_page_196");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/196-4cc67763e8.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_196" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(196);
      </script>
    </div>




  <div class="outer_page only_ie6_border   not_visible" id="outer_page_197" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page197" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/197-35e5244ccc.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 197};

        pageParams.containerElem = document.getElementById("outer_page_197");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/197-35e5244ccc.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_197" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(197);
      </script>
    </div>




  <div class="outer_page only_ie6_border    not_visible" id="outer_page_198" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page198" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/198-3286c6df05.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 198};

        pageParams.containerElem = document.getElementById("outer_page_198");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/198-3286c6df05.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_198" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(198);
      </script>
    </div>




  <div class="outer_page only_ie6_border     not_visible" id="outer_page_199" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page199" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/199-d9ce4af4e3.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 199};

        pageParams.containerElem = document.getElementById("outer_page_199");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/199-d9ce4af4e3.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_199" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(199);
      </script>
    </div>




  <div class="outer_page only_ie6_border     not_visible" id="outer_page_200" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page200" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/200-e66e0e8690.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 200};

        pageParams.containerElem = document.getElementById("outer_page_200");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/200-e66e0e8690.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_200" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(200);
      </script>
    </div>




  <div class="outer_page only_ie6_border      not_visible" id="outer_page_201" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page201" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/201-56d10db0ac.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 201};

        pageParams.containerElem = document.getElementById("outer_page_201");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/201-56d10db0ac.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_201" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(201);
      </script>
    </div>




  <div class="outer_page only_ie6_border       not_visible" id="outer_page_202" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page202" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/202-c4d57e2298.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 202};

        pageParams.containerElem = document.getElementById("outer_page_202");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/202-c4d57e2298.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_202" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(202);
      </script>
    </div>




  <div class="outer_page only_ie6_border       not_visible" id="outer_page_203" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page203" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/203-58d06f8e8f.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 203};

        pageParams.containerElem = document.getElementById("outer_page_203");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/203-58d06f8e8f.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_203" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(203);
      </script>
    </div>




  <div class="outer_page only_ie6_border      not_visible" id="outer_page_204" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page204" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/204-6d5b2eff5d.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 204};

        pageParams.containerElem = document.getElementById("outer_page_204");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/204-6d5b2eff5d.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_204" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(204);
      </script>
    </div>




  <div class="outer_page only_ie6_border      not_visible" id="outer_page_205" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page205" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/205-b10f1d97b8.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 205};

        pageParams.containerElem = document.getElementById("outer_page_205");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/205-b10f1d97b8.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_205" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(205);
      </script>
    </div>




  <div class="outer_page only_ie6_border     not_visible" id="outer_page_206" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page206" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/206-8019ee2827.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 206};

        pageParams.containerElem = document.getElementById("outer_page_206");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/206-8019ee2827.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_206" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(206);
      </script>
    </div>




  <div class="outer_page only_ie6_border     not_visible" id="outer_page_207" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page207" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/207-e2384ee8b0.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 207};

        pageParams.containerElem = document.getElementById("outer_page_207");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/207-e2384ee8b0.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_207" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(207);
      </script>
    </div>




  <div class="outer_page only_ie6_border      not_visible" id="outer_page_208" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page208" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/208-bf1cbbabaa.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 208};

        pageParams.containerElem = document.getElementById("outer_page_208");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/208-bf1cbbabaa.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_208" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(208);
      </script>
    </div>




  <div class="outer_page only_ie6_border      not_visible" id="outer_page_209" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page209" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/209-207336ebdb.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 209};

        pageParams.containerElem = document.getElementById("outer_page_209");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/209-207336ebdb.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_209" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(209);
      </script>
    </div>




  <div class="outer_page only_ie6_border      not_visible" id="outer_page_210" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page210" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/210-a8779f2305.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 210};

        pageParams.containerElem = document.getElementById("outer_page_210");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/210-a8779f2305.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_210" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(210);
      </script>
    </div>




  <div class="outer_page only_ie6_border    not_visible" id="outer_page_211" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page211" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/211-165104ff7d.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 211};

        pageParams.containerElem = document.getElementById("outer_page_211");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/211-165104ff7d.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_211" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(211);
      </script>
    </div>




  <div class="outer_page only_ie6_border    not_visible" id="outer_page_212" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page212" style="width: 1167px; height:902px">
<div class="text_layer" style="z-index:2"><div class="ie_fix">
&nbsp;
<div class="ff0" style="font-size:89px">
<span class="a" style="left:5287px;top:4152px">&nbsp;</span></div>
</div>
</div>
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/212-648f150d54.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [0], "pageNum": 212};

        pageParams.containerElem = document.getElementById("outer_page_212");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/212-648f150d54.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_212" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(212);
      </script>
    </div>




  <div class="outer_page only_ie6_border    not_visible" id="outer_page_213" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page213" style="width: 1167px; height:902px">
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/213-b2d52c5c84.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [], "pageNum": 213};

        pageParams.containerElem = document.getElementById("outer_page_213");
          pageParams.contentUrl = "https://html1-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/213-b2d52c5c84.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_213" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(213);
      </script>
    </div>




  <div class="outer_page only_ie6_border   not_visible" id="outer_page_214" style="width: 1270px; height: 982px;">

  <div class="b_tl"></div>
  <div class="b_tr"></div>
  <div class="b_br"></div>
  <div class="b_bl"></div>
  <div class="b_t"></div>
  <div class="b_r"></div>
  <div class="b_b"></div>
  <div class="b_l"></div>

  <div style="display: none; -webkit-transform: scale(1.08826049700086); -webkit-transform-origin: 0% 0%;"><div class="newpage" id="page214" style="width: 1167px; height:902px">
<div class="text_layer" style="z-index:2"><div class="ie_fix">
&nbsp;
<div class="ff0" style="font-size:89px">
<span class="a" style="left:5287px;top:4152px">&nbsp;</span></div>
</div>
</div>
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" style="left: 51px; top: 51px; width: 1007px; height: 798px; clip: rect(1px 1006px 797px 1px); display: block;" src="https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/images/214-d2c3ad91c9.jpg">
</div>
</div>
</div>

</div></div>

  <script type="text/javascript">
    (function() {
        var pageParams = {"origHeight": 902, "origWidth": 1167, "fonts": [0], "pageNum": 214};

        pageParams.containerElem = document.getElementById("outer_page_214");
          pageParams.contentUrl = "https://html2-f.scribdassets.com/5wpi9v3o3k1jsy5k/pages/214-d2c3ad91c9.jsonp";
          pageParams.blur = false
        var page = docManager.addPage(pageParams);
      })();
  </script>


    <div id="between_page_ads_214" class="between_page_ads" style="display: block;">
      <script type="text/javascript">
        Scribd.Ads.addBetweenPageUnit(214);
      </script>
    </div>




  <!--[if IE]>
  <script type='text/javascript'>
    window.docManagerIEAdded = true;
    if (document.observe) {
      document.observe('dom:loaded', function () {
          docManager.allPagesAdded();
        });
    } else {
      window.attachEvent('onload', function () {
          docManager.allPagesAdded();
        });
    }
  </script>
  <![endif]-->

  <script type="text/javascript">
    if (window.docManagerIEAdded != true) {
      docManager.allPagesAdded();
    }
  </script>

</div>""")

def find_all_translations(soup):
	i = 0
	for slide in soup.find("div", class_="outer_page_container").find_all("div", class_="outer_page"):
		i += 1
		imgsrc = slide.find("img")['src']
		print(imgsrc)
		urllib.request.urlretrieve(imgsrc, os.path.join(download_path, ("%03d.jpg"%i)))

homepage = domain + 'doc/90484468/Rizal-by-Austin-Coates#scribd'

print('Parsing %s...'%homepage)
find_all_translations(getSoup(homepage))
