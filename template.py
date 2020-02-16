#!/usr/bin/env python3
# -*- coding: utf-8 -*

elem = '''	<li><div class="m-post  m-post-txt masonry-brick">
			<div class="ct"><div class="ctc box"><div class="text">
				<p dir="ltr"><b>{name}</b><br>{desc}</p>
			</div></div></div>
			<div class="info box">
				<a class="link" target="_blank" href="{link}">{site}</a>
			</div></div>
		</li>'''

left = '''
	<!-- left -->
	<ul style="top: 0px; left: 0px;">
	{elements}
	</ul>'''

right = '''
	<!-- right -->
	<ul style="position: absolute; top: 0px; left: 450px;">
	{elements}
	</ul>'''

home = '''<!-- Home page -->
	<div class="m-postlst box masonry" style="visibility: visible; width: 860px; position: relative;">
	{home}
	</div>'''

ga = '''
	<!-- Google analytics -->
	<script>
	(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
	(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
	m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
	})(window,document,'script','//www.google-analytics.com/analytics.js','ga');
	ga('create', 'UA-62244864-5', 'auto');
	ga('send', 'pageview');
	</script>'''

footer = '''
	<!-- Footer -->
	<div class="g-ft"><br /><br /><br /><br />
	<p class="m-cprt">©&nbsp;<a href="http://kfd.me/">KFD.ME</a>&nbsp;|&nbsp;Created by <a href="http://wrfly.kfd.me/">wrfly</a></p>
	</div>'''

page = """<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
	<meta http-equiv="content-type" content="text/html; charset=UTF-8">
	<meta charset="utf-8">
	<title>有趣的网站 | Interesting web sites</title>
	<link rel="shortcut icon" href="iws_files/favicon.ico">
	<meta name="Keywords" content="KFD.ME interesting web sites 有趣的网站">
	<meta name="Description" content="KFD.ME interesting web sites 有趣的网站">
	<link type="text/css" rel="stylesheet" href="iws_files/6597123642725761469.css">
	<style>
	</style>
	<!--[if gte IE 8]>
	<style>
		.m-post-leftimg .text ul,
		.m-post-leftimg .text ol,
		.m-detail-leftimg .text ul,
		.m-detail-leftimg .text ol{padding-left:0;}
		.m-post-leftimg .text ul li,
		.m-detail-leftimg .text ul li{list-style:disc inside none;}
		.m-post-leftimg .text ol li,
		.m-detail-leftimg .text ol li{list-style:decimal inside none;}
		.m-post-leftimg .text ul li p,
		.m-post-leftimg .text ol li p,
		.m-detail-leftimg .text ul li p,
		.m-detail-leftimg .text ol li p{vertical-align:bottom;*vertical-align:baseline;display:-moz-inline-box;display:inline-block;*display:inline;zoom:1;margin:0;}
		.m-post-leftimg .text ul li,
		.m-post-leftimg .text ol li,
		.m-detail-leftimg .text ul li,
		.m-detail-leftimg .text ol li{overflow:hidden;height:27px;line-height:27px;padding-left:2px;}
		.m-post-leftimg .text ul li p,
		.m-post-leftimg .text ol li p,
		.m-detail-leftimg .text ul li p,
		.m-detail-leftimg .text ol li p{overflow:hidden;width:90%;white-space:nowrap;text-overflow:ellipsis;-o-text-overflow:ellipsis;word-break:keep-all;}
	</style>
	<![endif]-->
</head>

<body class="p-homepage">

<div class="g-doc box">
	<div class="g-hd0">
		<div class="g-hdc box">
			<h1 class="m-ttl"><a href="http://123.kfd.me/">有趣的网站</a></h1>
		</div>
	</div>

	<div class="g-hd1">
		<div class="g-hdc box">
			<p class="m-about">你好，我是一个网址导航，搜集了互联网上好多有意思的网站，这些网站都是我的主人精挑细选的，质量上乘，品质可靠，如果你有好的建议，欢迎联系他哦～</p>
			<ul class="m-nav">
				<li><a href="https://kfd.me/" target="_blank">主页</a></li>
				<li><a href="mailto:root@kfd.me" target="_blank">联系</a></li>
				<li><a href="/comments/" target="_blank">留言</a></li>
			</ul>
		</div>
	</div>

	__BODY__

</div>

<!-- 这个模板是我从lofter上扒下来的，嘿嘿 -->
</body>

</html>"""