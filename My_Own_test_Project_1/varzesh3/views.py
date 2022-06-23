from django.shortcuts import render
from django.http import HttpResponse

def show_varzesh3(request):
    return HttpResponse('''
<!DOCTYPE html>
<html lang="fa">
<head>
    <title>مرجع فوتبال و ورزش - ورزش سه - Varzesh3</title>
    <meta charset="utf-8" />
    
    <meta name="viewport" content="width=1170" />
    
<meta name="description" content="پایگاه اطلاع رسانی ورزشی برای فارسی زبانان كه اخبار حوزه ورزش (فوتبال،والیبال ،بسكتبال و...)ونتایج بازیها و جداول لیگ های ورزشی را بصورت زنده ارائه می کند" />

<link href="https://www.varzesh3.com/" rel="canonical" />

<meta property="og:site_name" content="ورزش سه">
<meta property="og:title" content="مرجع فوتبال و ورزش - ورزش سه - Varzesh3" />
<meta property="og:url" content="https://www.varzesh3.com/" />
<meta property="og:description" content="پایگاه اطلاع رسانی ورزشی برای فارسی زبانان كه اخبار حوزه ورزش (فوتبال،والیبال ،بسكتبال و...)ونتایج بازیها و جداول لیگ های ورزشی را بصورت زنده ارائه می کند" />
<meta property="og:type" content="website" />
<meta property="og:locale" content="fa_IR" />
<meta property="og:image" itemprop="image primaryImageOfPage" content="https://static.varzeshe3.com/img/varzesh3-logo.png?v=1" />

<meta name="twitter:site" content="ورزش سه">
<meta name="twitter:card" content="summary" />
<meta name="twitter:title" content="مرجع فوتبال و ورزش - ورزش سه - Varzesh3" />
<meta name="twitter:description" content="پایگاه اطلاع رسانی ورزشی برای فارسی زبانان كه اخبار حوزه ورزش (فوتبال،والیبال ،بسكتبال و...)ونتایج بازیها و جداول لیگ های ورزشی را بصورت زنده ارائه می کند" />
<meta name="twitter:url" content="https://www.varzesh3.com/" />


    

    <link rel="dns-prefetch" href="https://static.varzeshe3.com" />
    <link rel="preconnect" href="https://static.varzeshe3.com" />
    <link rel="dns-prefetch" href="https://biz1.varzeshe3.com/banners" />
    <link rel="preconnect" href="https://biz1.varzeshe3.com/banners" />
    <link rel="dns-prefetch" href="https://match.varzeshe3.com" />
    <link rel="preconnect" href="https://match.varzeshe3.com" />
    <link rel="dns-prefetch" href="https://news.varzeshe3.com" />
    <link rel="preconnect" href="https://news.varzeshe3.com" />
    <link rel="dns-prefetch" href="https://newspaper.varzeshe3.com" />
    <link rel="preconnect" href="https://newspaper.varzeshe3.com" />
    <link rel="dns-prefetch" href="https://video-images1.varzeshe3.com" />
    <link rel="preconnect" href="https://video-images1.varzeshe3.com" />
    <link rel="dns-prefetch" href="https://static2.farakav.com" />
    <link rel="preconnect" href="https://static2.farakav.com" />

    <link rel="preload" as="font" type="font/woff" crossorigin href="https://static.varzesh3.com/fonts/iransans/woff/IRANSansXFaNum-Regular.woff" />
    <link rel="preload" as="font" type="font/woff" crossorigin href="https://static.varzesh3.com/fonts/iransans/woff/IRANSansXFaNum-Medium.woff" />
    <link rel="preload" as="font" type="font/woff" crossorigin href="https://static.varzesh3.com/fonts/iransans/woff/IRANSansXFaNum-DemiBold.woff" />
    <link rel="preload" as="font" type="font/woff" crossorigin href="https://static.varzesh3.com/fonts/iransans/woff/IRANSansXFaNum-Bold.woff" />
    <link rel="preload" as="style" href="https://static.varzesh3.com/css/global.vendor.css?v=1.5.1" />
    <link rel="preload" as="style" href="https://static.varzesh3.com/css/sharedLayout.css?v=1.5.1" />
    <link rel="preload" as="script" href="https://static.varzesh3.com/js/global.vendor.js?v=1.5.1" />
    <link rel="preload" as="script" href="https://static.varzesh3.com/js/sharedLayout.js?v=1.5.1" />
    
    <link rel="preload" as="style" href="https://static.varzesh3.com/css/home.css?v=1.5.1" />


    <link rel="shortcut icon" href="/img/favicon.ico" type="image/x-icon" />
    <link rel="stylesheet" href="https://static.varzesh3.com/css/global.vendor.css?v=1.5.1" />
    <link rel="stylesheet" href="https://static.varzesh3.com/css/sharedLayout.css?v=1.5.1" />
    
    <link rel="stylesheet" href="https://static.varzesh3.com/css/home.css?v=1.5.1" />

    <script type="application/ld+json">
        {
            "@context": "http://schema.org/",
            "@type": "Organization",
            "url": "http://www.varzesh3.com/",
            "logo": "https://static.varzeshe3.com/img/varzesh3-logo.png",
            "potentialAction": {
                "@type": "SearchAction",
                "target": "https://www.varzesh3.com/search?q={search_term_string}",
                "query-input": "required name=search_term_string"
            },
            "sameAs" : [
                "https://facebook.com/varzesh3",
                "https://twitter.com/varzesh3",
                "https://instagram.com/varzesh3"
            ]
        }
    </script>
    

    <!-- Google Tag Manager -->
    <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
    new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
    j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
    'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
    })(window,document,'script','dataLayer','GTM-5BWLB69');</script>
    <!-- End Google Tag Manager -->
</head>
<body>
    <!-- Google Tag Manager (noscript) -->
    <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-5BWLB69"
    height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
    <!-- End Google Tag Manager (noscript) -->
    
    <header>
        <section class="allhead">
    <div class="container">

         
<ul class="allhead-menu">
            <li class="">

                    <a target="_blank" href="https://pishbini.varzesh3.com">پیش بینی </a>
            </li>
            <li class="">

                    <a target="_blank" href="https://video.varzesh3.com">ویدیو </a>
            </li>
            <li class="">

                    <a target="_blank" href="https://lenz.varzesh3.com">لنز</a>
            </li>
            <li class="">

                    <a target="_blank" href="https://www.anten.ir">پخش زنده</a>
            </li>
            <li class="">

                    <a href="https://www.varzesh3.com/contact">ثبت نظر</a>
            </li>
</ul></partial>

        <div class="allhead-auth">
            <span class="allhead-date"><span class="today-time">
    <img src="https://static.varzesh3.com/img/icons/icon-general-today.svg" />
    <span class="datetime"><span>پنج شنبه 2 تیر</span><span> - </span><span>13:18</span></span>
</span></span>
            <span class="search-btn"><img src="https://static.varzesh3.com/img/icons/search-icon-white.svg" /><span>جستجو </span></span>
            <div class="allhead-user-auth">
                <a class="login"> <span><img alt="ورود" width="9" height="9" src="https://static.varzesh3.com/img/shared/header/user.svg?w=9" /></span> ورود</a>
                <div class="user-is-loged-in">
                    <div class="dropdown">
                        <span class="user-menu-data"  id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                            <img src="/img/default/default-player.png" />
                        </span>
                        <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                            <a class="dropdown-item" href="https://sso.varzesh3.com/profile">
                                  <span>
                                     <img alt="حساب کاربری" width="25" src="https://static.varzesh3.com/img/default/default-player.png?w=25" class="user-profile-icon" />
                                </span> 
                                مشاهده حساب کاربری
                            </a>
                             <a class="dropdown-item logout"> 
                                 <span>
                                     <img alt="خروج" width="25" src="https://static.varzesh3.com/img/icons/logout.svg?w=25" class="logout-icon" />
                                </span> 
                                خروج
                                </a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<nav class="navbar navbar-expand-lg has-tb">
    <div class="container">
        <a class="navbar-brand" href="/">
            <img src="https://static.varzesh3.com/img/logo/vrz3-logo.svg" />
        </a>
        <div class="navbar-collapse d-none  d-lg-inline-flex flex-lg-row-reverse">
            <ul class="navbar-nav flex-grow-1">
<li class="nav-item first-parent-item  ">
                <a class="menu-link-item" href="https://www.varzesh3.com/"  title="صفحه اصلی">
                    صفحه اصلی
                </a>
        </li>
<li class="nav-item first-parent-item  ">
                <a class="menu-link-item" href="https://www.varzesh3.com/news"  title="اخبار">
                    اخبار 
                </a>
        </li>
<li class="nav-item first-parent-item  ">
                <a class="menu-link-item" href="https://www.varzesh3.com/football/league/900578/لیگ-برتر-ایران-1400-1401"  title="جدول لیگ برتر">
                    جدول لیگ برتر
                </a>
        </li>
<li class="nav-item first-parent-item  ">
                <a class="menu-link-item" href="https://www.varzesh3.com/football/playoffs/900591/جام-حذفی-ایران-1400-1401"  title="جام حذفی">
                    جام حذفی
                </a>
        </li>
<li class="nav-item first-parent-item  ">
                <a class="menu-link-item" href="https://www.varzesh3.com/newspaper"  title="روزنامه">
                    روزنامه
                </a>
        </li>
<li class="nav-item first-parent-item highlight ">
                <a class="menu-link-item" href="https://www.varzesh3.com/football/transfers/iran/نقل-و-انتقالات-لیگ-برتر"  target="_blank" title="نقل انتقالات">
                    نقل و انتقالات
                </a>
        </li>
<li class="nav-item first-parent-item  ">
                <a class="menu-link-item" href="https://video.varzesh3.com"  target="_blank" title="ویدیو">
                    ویدیو
                </a>
        </li>
<li class="nav-item first-parent-item  live">
                <a class="menu-link-item" href="https://www.varzesh3.com/livescore"  title="نتایج زنده">
                    نتایج زنده
                </a>
        </li>
</ul>
        </div>
        <div class="left-menu-box home-left-menu-box">
            <button class="navbar-toggler" type="button">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
                    <g fill="none" fill-rule="evenodd">
                        <g>
                            <g>
                                <path d="M0 0L24 0 24 24 0 24z" transform="translate(-320 -16) translate(320 16)" />
                                <path fill="#757575" d="M3 18h18v-2H3v2zm0-5h18v-2H3v2zm0-7v2h18V6H3z" transform="translate(-320 -16) translate(320 16)" />
                            </g>
                        </g>
                    </g>
                </svg>
            </button>

            <div class="tb-holder banner-zone justify-content-center header-ad">
                

<div class="adbox" data-id="322">
            <a  style="display:none;" class="adlink vrz-lazy" target="_blank" href="https://biz.varzesh3.com/events/click/322">
                <img class="adimage" id="img-322" src="https://static.varzeshe3.com/img/blank.png" data-origin="https://biz-cdn.varzesh3.com/banners/2022/06/01/7d686999-bd10-4f94-a95f-ed350659b043.gif" width="468" />
            </a>
</div>
            </div>
        </div>
    </div>
</nav></partial>


    </header>
    <section class="mainbody">
        <main role="main">
            


<div class="home-page">
    <div class="home-holder">
        
        <div class="right-side-big-col">
            <div class="v2-inner-col">
                <div class="v600-col">
                    
<div class="widget-holder">
    <div class="widget slider">
        <div class="homepage-slider v2 owl-carousel">
                    <div class="slider-item">
                        <div class="slider-image">
                                <img width="350" src="https://news-cdn.varzesh3.com/pictures/2022/06/23/C/zsmcmwrz.jpg?w=350" />
                        </div>
                        <div class="slider-info">
                                <a href="https://www.varzesh3.com/news/1830328/دو-ستاره-ای-که-استقلال-را-فاتح-نقل-و-انتقالات-می-کنند"  class="slider-item-link">
                                    <p class="subhead">نامه رسمی به پرتغال، مذاکره در امارات</p>
                                    <h2 class="headline"> دو ستاره‌ای که استقلال را فاتح نقل‌و‌انتقالات می‌کنند!</h2>
                                    <p class="lead">بعد از جذب سرمربی پرتغالی، حالا مدیریت استقلال دو هدف جذاب نقل‌و‌انتقالاتی را در پیش گرفته که در صورت تحقق آنها، با توجه به اسکواد آبی‌ها از فصل قبل، مدافع عنوان قهرمانی مدعی اول فصل بعد خواهد بود.</p>
                                </a>
                        </div>
                    </div>
                    <div class="slider-item">
                        <div class="slider-image">
                                <img width="350" src="https://news-cdn.varzesh3.com/pictures/2022/06/23/B/4hiiprkm.png?w=350" />
                        </div>
                        <div class="slider-info">
                                <a href="https://www.varzesh3.com/news/1830327/سکوت-زیدان-شکست-حرکتی-تاریخی-به-افتخار-فوق-ستاره"  class="slider-item-link">
                                    <p class="subhead">لوگوی نشریه معروف به نام زیزو شد؛</p>
                                    <h2 class="headline"> سکوت زیدان شکست؛ حرکتی تاریخی به افتخار فوق‌ستاره!</h2>
                                    <p class="lead">نشریه اکیپ لوگوی خود را به افتخار 50 سالگی زین الدین زیدان عوض کرده؛ مصاحبه‌ای مفصل با فوق ستاره فوتبال فرانسه.</p>
                                </a>
                        </div>
                    </div>
                    <div class="slider-item">
                        <div class="slider-image">
                                <img width="350" src="https://news-cdn.varzesh3.com/pictures/2022/06/22/B/kmyb21q5.jpg?w=350" />
                        </div>
                        <div class="slider-info">
                                <a href="https://www.varzesh3.com/news/1830160/تیم-ملی-در-دادگاه-جنجالی-پیشنهاد-انصراف-عکس"  class="slider-item-link">
                                    <p class="subhead">تلویزیون‌هایی که وسط بازی خاموش شد؛</p>
                                    <h2 class="headline"> تیم ملی در دادگاه جنجالی؛ پیشنهاد انصراف (عکس)</h2>
                                    <p class="lead">عملکرد تیم ملی والیبال ایران با واکنش تند هواداران این رشته ورزشی پرطرفدار روبرو شده است.</p>
                                </a>
                        </div>
                    </div>
                    <div class="slider-item">
                        <div class="slider-image">
                                <img width="350" src="https://news-cdn.varzesh3.com/pictures/2022/06/22/C/d12imq45.jpg?w=350" />
                        </div>
                        <div class="slider-info">
                                <a href="https://www.varzesh3.com/news/1830190/پرسپولیس-برای-سعید-صادقی-جا-باز-می-کند"  class="slider-item-link">
                                    <p class="subhead">ترابی در حمله، امیری در دفاع؟</p>
                                    <h2 class="headline"> پرسپولیس برای سعید صادقی جا باز می‌کند!</h2>
                                    <p class="lead">با انتقال سعید صادقی به پرسپولیس، یحیی گل‌محمدی ناچار به تغییر پست در خط میانی خواهد بود.</p>
                                </a>
                        </div>
                    </div>
        </div>
    </div>
</div>
                </div>
                <div class="v50-r-col">
                    

        

        

<div class="adbox" data-id="330">
            <a  style="display:none;" class="adlink vrz-lazy" target="_blank" href="https://biz.varzesh3.com/events/click/330">
                <img class="adimage" id="img-330" src="https://static.varzeshe3.com/img/blank.png" data-origin="https://biz-cdn.varzesh3.com/banners/2022/06/21/cdde73ad-4db7-4b41-b04d-f364b0860267.gif" width="300" />
            </a>
</div>
        

<div class="adbox" data-id="140">
            <a  style="display:none;" class="adlink vrz-lazy" target="_blank" href="https://biz.varzesh3.com/events/click/140">
                <img class="adimage" id="img-140" src="https://static.varzeshe3.com/img/blank.png" data-origin="https://biz-cdn.varzesh3.com/banners/2022/05/26/2051b1a7-d617-43fd-a1b2-4930014e934c.gif" width="300" />
            </a>
</div>


        <div class="widget-holder">
            <div class="widget league schedual football" id="77">
                            

<div class="widget-header">
    <h2>لیگ های ایران</h2>
    <div class="select-options">
        <select id="stage">
                    <option value="901902" selected="selected" data-api="https://football-api.varzesh3.com/v1.0/widgets/77/league/901902">لیگ برتر ایران </option>
                    <option value="901955" data-api="https://football-api.varzesh3.com/v1.0/widgets/77/league/901955">لیگ دسته یک آزادگان </option>
                    <option value="901890" data-api="https://futsal-api.varzesh3.com/v1.0/widgets/77/league/901890">لیگ برتر فوتسال </option>
        </select>
        <select id="round">
                    <option value="1">هفته 1</option>
                    <option value="2">هفته 2</option>
                    <option value="3">هفته 3</option>
                    <option value="4">هفته 4</option>
                    <option value="5">هفته 5</option>
                    <option value="6">هفته 6</option>
                    <option value="7">هفته 7</option>
                    <option value="8">هفته 8</option>
                    <option value="9">هفته 9</option>
                    <option value="10">هفته 10</option>
                    <option value="11">هفته 11</option>
                    <option value="12">هفته 12</option>
                    <option value="13">هفته 13</option>
                    <option value="14">هفته 14</option>
                    <option value="15">هفته 15</option>
                    <option value="16">هفته 16</option>
                    <option value="17">هفته 17</option>
                    <option value="18">هفته 18</option>
                    <option value="19">هفته 19</option>
                    <option value="20">هفته 20</option>
                    <option value="21">هفته 21</option>
                    <option value="22">هفته 22</option>
                    <option value="23">هفته 23</option>
                    <option value="24">هفته 24</option>
                    <option value="25">هفته 25</option>
                    <option value="26">هفته 26</option>
                    <option value="27">هفته 27</option>
                    <option value="28">هفته 28</option>
                    <option value="29">هفته 29</option>
                    <option value="30" selected="selected">هفته 30</option>
        </select>
    </div>
</div>
<div class="widget-body">
    <div class="scrollable-box" style="max-height:auto">
        <div class="scroll-list-content">
             <div class="widget-subtitle" style="background-color:#f3b500"><h3>لیگ برتر ایران</h3></div>
            <div class="widget-schedual">
                        <div class="date-seprator"><h4>دوشنبه 9 خرداد</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/172364/پیکان-مس-رفسنجان"> <img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                    
                                </div>
                                <div class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><a href="/football/team/11/پیکان">پیکان</a></div>
                                    <div class="fixture-result-match-goals"><span class="host">1</span><span> - </span><span class="guest">1</span></div>
                                    <div class="fixture-result-match-guest"><a href="/football/team/28/مس-رفسنجان">مس رفسنجان</a></div>
                                </div>
                                <div class="fixture-result-match-time">
                                    <a target="_blank" href="https://video.varzesh3.com/video/252860/"> <img src="https://static.varzesh3.com/img/icons/video-link.svg" /></a>
                                    <span class="match-clock"></span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/172366/استقلال-نفت-مسجد-سلیمان"> <img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                    
                                </div>
                                <div class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><a href="/football/team/4/استقلال">استقلال</a></div>
                                    <div class="fixture-result-match-goals"><span class="host">0</span><span> - </span><span class="guest">0</span></div>
                                    <div class="fixture-result-match-guest"><a href="/football/team/300/نفت-مسجد-سلیمان">نفت مسجد سلیمان</a></div>
                                </div>
                                <div class="fixture-result-match-time">
                                    <a target="_blank" href="https://video.varzesh3.com/video/252859/"> <img src="https://static.varzesh3.com/img/icons/video-link.svg" /></a>
                                    <span class="match-clock"></span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                        <div class="date-seprator"><h4>سه شنبه 10 خرداد</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/172370/نساجی-مازندران-تراکتور"> <img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                    
                                </div>
                                <div class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><a href="/football/team/37/نساجی-مازندران">نساجی مازندران</a></div>
                                    <div class="fixture-result-match-goals"><span class="host">0</span><span> - </span><span class="guest">3</span></div>
                                    <div class="fixture-result-match-guest"><a href="/football/team/18/تراکتور">تراکتور</a></div>
                                </div>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock"></span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                        <div class="date-seprator"><h4>پنج شنبه 12 خرداد</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/172363/شهرخودرو-مشهد-فولاد"> <img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                    
                                </div>
                                <div class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><a href="/football/team/902744/شهرخودرو-مشهد">شهرخودرو مشهد</a></div>
                                    <div class="fixture-result-match-goals"><span class="host">0</span><span> - </span><span class="guest">0</span></div>
                                    <div class="fixture-result-match-guest"><a href="/football/team/9/فولاد">فولاد</a></div>
                                </div>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock"></span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/172365/گل-گهرسیرجان-ذوب-آهن"> <img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                    
                                </div>
                                <div class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><a href="/football/team/44/گل-گهرسیرجان">گل گهرسیرجان</a></div>
                                    <div class="fixture-result-match-goals"><span class="host">3</span><span> - </span><span class="guest">2</span></div>
                                    <div class="fixture-result-match-guest"><a href="/football/team/1/ذوب-آهن">ذوب آهن</a></div>
                                </div>
                                <div class="fixture-result-match-time">
                                    <a target="_blank" href="https://video.varzesh3.com/video/253101/"> <img src="https://static.varzesh3.com/img/icons/video-link.svg" /></a>
                                    <span class="match-clock"></span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/172367/فجر-سپاسی-پرسپولیس"> <img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                    
                                </div>
                                <div class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><a href="/football/team/2/فجر-سپاسی">فجر سپاسی</a></div>
                                    <div class="fixture-result-match-goals"><span class="host">0</span><span> - </span><span class="guest">1</span></div>
                                    <div class="fixture-result-match-guest"><a href="/football/team/6/پرسپولیس">پرسپولیس</a></div>
                                </div>
                                <div class="fixture-result-match-time">
                                    <a target="_blank" href="https://video.varzesh3.com/video/253099/"> <img src="https://static.varzesh3.com/img/icons/video-link.svg" /></a>
                                    <span class="match-clock"></span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/172368/سپاهان-آلومینیوم-اراک"> <img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                    
                                </div>
                                <div class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><a href="/football/team/10/سپاهان">سپاهان</a></div>
                                    <div class="fixture-result-match-goals"><span class="host">1</span><span> - </span><span class="guest">1</span></div>
                                    <div class="fixture-result-match-guest"><a href="/football/team/901631/آلومینیوم-اراک">آلومینیوم اراک</a></div>
                                </div>
                                <div class="fixture-result-match-time">
                                    <a target="_blank" href="https://video.varzesh3.com/video/253100/"> <img src="https://static.varzesh3.com/img/icons/video-link.svg" /></a>
                                    <span class="match-clock"></span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/172369/صنعت-نفت-آبادان-هوادار"> <img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                    
                                </div>
                                <div class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><a href="/football/team/21/صنعت-نفت-آبادان">صنعت نفت آبادان</a></div>
                                    <div class="fixture-result-match-goals"><span class="host">3</span><span> - </span><span class="guest">0</span></div>
                                    <div class="fixture-result-match-guest"><a href="/football/team/902565/هوادار">هوادار</a></div>
                                </div>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock"></span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
            </div>
        </div>
    </div>
    
</div>
<div class="widget-footer"> <a href="/football/league/900578/لیگ-برتر-ایران-1400-1401" >مشاهده جدول کامل لیگ برتر ایران</a></div>
            </div>
        </div>
        

        

<div class="adbox" data-id="210">
            <div class="native-holder">
                <div id="pos-article-display-3546"></div>
            </div>
</div>


        <div class="widget-holder">
            <div class="widget league schedual football" id="78">
                            

<div class="widget-header">
    <h2>جدول لیگ های ایران</h2>
    <div class="select-options">
        <select id="stage">
                    <option value="901902" selected="selected" data-api="https://football-api.varzesh3.com/v1.0/widgets/78/league/901902">لیگ برتر ایران </option>
                    <option value="901955" data-api="https://football-api.varzesh3.com/v1.0/widgets/78/league/901955">لیگ دسته یک آزادگان </option>
                    <option value="901890" data-api="https://futsal-api.varzesh3.com/v1.0/widgets/78/league/901890">لیگ برتر فوتسال </option>
        </select>
        
    </div>
</div>
<div class="widget-body">
    
    <div class="widget-table">
        <div class="widget-subtitle" style="background-color:#f3b500"><h3>جدول لیگ برتر ایران</h3></div>
        <div class="table-holder">
            <table class=" league-standing widget-standing">
                <thead>
                    <tr>
                        <th scope="col">رتبه</th>
                        <th scope="col">تيم</th>
                        <th scope="col">بازی</th>
                        <th scope="col">امتياز</th>
                    </tr>
                </thead>
                <tbody>
                            <tr>
                                <td scope="row">1</td>
                                <td><a href="/football/team/4/استقلال"> استقلال</a></td>
                                <td>30</td>
                                <td>68</td>
                            </tr>
                            <tr>
                                <td scope="row">2</td>
                                <td><a href="/football/team/6/پرسپولیس"> پرسپولیس</a></td>
                                <td>30</td>
                                <td>63</td>
                            </tr>
                            <tr>
                                <td scope="row">3</td>
                                <td><a href="/football/team/10/سپاهان"> سپاهان</a></td>
                                <td>30</td>
                                <td>56</td>
                            </tr>
                            <tr>
                                <td scope="row">4</td>
                                <td><a href="/football/team/44/گل-گهرسیرجان"> گل گهرسیرجان</a></td>
                                <td>30</td>
                                <td>51</td>
                            </tr>
                            <tr>
                                <td scope="row">5</td>
                                <td><a href="/football/team/9/فولاد"> فولاد</a></td>
                                <td>30</td>
                                <td>49</td>
                            </tr>
                            <tr>
                                <td scope="row">6</td>
                                <td><a href="/football/team/28/مس-رفسنجان"> مس رفسنجان</a></td>
                                <td>30</td>
                                <td>45</td>
                            </tr>
                            <tr>
                                <td scope="row">7</td>
                                <td><a href="/football/team/1/ذوب-آهن"> ذوب آهن</a></td>
                                <td>30</td>
                                <td>37</td>
                            </tr>
                            <tr>
                                <td scope="row">8</td>
                                <td><a href="/football/team/901631/آلومینیوم-اراک"> آلومینیوم اراک</a></td>
                                <td>30</td>
                                <td>37</td>
                            </tr>
                            <tr>
                                <td scope="row">9</td>
                                <td><a href="/football/team/11/پیکان"> پیکان</a></td>
                                <td>30</td>
                                <td>36</td>
                            </tr>
                            <tr>
                                <td scope="row">10</td>
                                <td><a href="/football/team/21/صنعت-نفت-آبادان"> صنعت نفت آبادان</a></td>
                                <td>30</td>
                                <td>36</td>
                            </tr>
                            <tr>
                                <td scope="row">11</td>
                                <td><a href="/football/team/902565/هوادار"> هوادار</a></td>
                                <td>30</td>
                                <td>34</td>
                            </tr>
                            <tr>
                                <td scope="row">12</td>
                                <td><a href="/football/team/37/نساجی-مازندران"> نساجی مازندران</a></td>
                                <td>30</td>
                                <td>33</td>
                            </tr>
                            <tr>
                                <td scope="row">13</td>
                                <td><a href="/football/team/18/تراکتور"> تراکتور</a></td>
                                <td>30</td>
                                <td>31</td>
                            </tr>
                            <tr>
                                <td scope="row">14</td>
                                <td><a href="/football/team/300/نفت-مسجد-سلیمان"> نفت مسجد سلیمان</a></td>
                                <td>30</td>
                                <td>22</td>
                            </tr>
                            <tr>
                                <td scope="row">15</td>
                                <td><a href="/football/team/902744/شهرخودرو-مشهد"> شهرخودرو مشهد</a></td>
                                <td>30</td>
                                <td>17</td>
                            </tr>
                            <tr>
                                <td scope="row">16</td>
                                <td><a href="/football/team/2/فجر-سپاسی"> فجر سپاسی</a></td>
                                <td>30</td>
                                <td>17</td>
                            </tr>
                </tbody>
            </table>
        </div>
    </div>
</div>
<div class="widget-footer"> <a href="/football/league/900578/لیگ-برتر-ایران-1400-1401" >مشاهده جدول کامل لیگ برتر ایران</a></div>
            </div>
        </div>
        

        

<div class="adbox" data-id="168">
            <div class="native-holder">
                <div id="YmB8" ></div>

            </div>
</div>


        <div class="widget-holder">
            <div class="widget news" id="79">
                            
<div class="widget-header"><h2>آخرین اخبار سایر ورزش‌ها</h2></div>
<div class="widget-body">
    
    <div class="news-content" data-type="Latest">
        
        <div class="alert-message">حداقل یکی از گزینه ها باید فعال باشد.</div>
        <div class="news-main-list scrollable-box" data-height="1000" style="max-height: 1000px">
            <div class="scroll-list-content">
                <ul>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="صحبت های عطایی قبل از بازی با آمریکا" href="https://video.varzesh3.com/video/254281/صحبت-های-عطایی-قبل-از-بازی-با-آمریکا"> <span class="news-type"></span>صحبت های عطایی قبل از بازی با آمریکا</a></li>
                            <li class="text-type" data-origin="2" data-media="1" data-tag="" data-sport="3"><a title="اسپراو: این بازیکنان ایران را تا به حال ندیده‌ام" href="https://www.varzesh3.com/news/1830331/اسپراو-این-بازیکنان-ایران-را-تا-به-حال-ندیده-ام"> <span class="news-type"></span>اسپراو: این بازیکنان ایران را تا به حال ندیده‌ام</a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="خلاصه والیبال فرانسه 3 - هلند 0" href="https://video.varzesh3.com/video/254276/خلاصه-والیبال-فرانسه-3-هلند-0"> <span class="news-type"></span>خلاصه والیبال فرانسه 3 - هلند 0</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="16"><a title="کسب طلا مقابل چشمان همسر و دختر" href="https://www.varzesh3.com/news/1830323/کسب-طلا-مقابل-چشمان-همسر-و-دختر"> <span class="news-type"></span>کسب طلا مقابل چشمان همسر و دختر</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="12"><a title="تغییر تاریخ برگزاری مسابقات بوکس قهرمانی جوانان کشور" href="https://www.varzesh3.com/news/1830310/تغییر-تاریخ-برگزاری-مسابقات-بوکس-قهرمانی-جوانان-کشور"> <span class="news-type"></span>تغییر تاریخ برگزاری مسابقات بوکس قهرمانی جوانان کشور</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="16"><a title="کسب یک طلا و یک برنز  در پیکارهای هفت وزن نخست" href="https://www.varzesh3.com/news/1830309/کسب-یک-طلا-و-یک-برنز-در-پیکارهای-هفت-وزن-نخست"> <span class="news-type"></span>کسب یک طلا و یک برنز  در پیکارهای هفت وزن نخست</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="3"><a title="عطایی: کار سختی مقابل تیم بدون باخت مسابقات داریم" href="https://www.varzesh3.com/news/1830308/عطایی-کار-سختی-مقابل-تیم-بدون-باخت-مسابقات-داریم"> <span class="news-type"></span>عطایی: کار سختی مقابل تیم بدون باخت مسابقات داریم</a></li>
                            <li class="text-type" data-origin="2" data-media="1" data-tag="" data-sport="3"><a title="لیگ ملت‌ها؛ آمریکا قصد شکست خوردن ندارد" href="https://www.varzesh3.com/news/1830307/لیگ-ملت-ها-آمریکا-قصد-شکست-خوردن-ندارد"> <span class="news-type"></span>لیگ ملت‌ها؛ آمریکا قصد شکست خوردن ندارد</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="33"><a title="فیروزجا روی دور تساوی در رقابت‌های کاندیداهای شطرنج!" href="https://www.varzesh3.com/news/1830304/فیروزجا-روی-دور-تساوی-در-رقابت-های-کاندیداهای-شطرنج"> <span class="news-type"></span>فیروزجا روی دور تساوی در رقابت‌های کاندیداهای شطرنج!</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="10"><a title="فینال B،شرط  اعزام رویینگ سواران به قهرمانی جهان" href="https://www.varzesh3.com/news/1830303/فینال-bشرط-اعزام-رویینگ-سواران-به-قهرمانی-جهان"> <span class="news-type"></span>فینال B،شرط  اعزام رویینگ سواران به قهرمانی جهان</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="14"><a title="کدام دوومیدانی‌کاران ایران در اردوی خارجی هستند؟" href="https://www.varzesh3.com/news/1830302/کدام-دوومیدانی-کاران-ایران-در-اردوی-خارجی-هستند"> <span class="news-type"></span>کدام دوومیدانی‌کاران ایران در اردوی خارجی هستند؟</a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="خلاصه والیبال صربستان 1 - آمریکا 3" href="https://video.varzesh3.com/video/254265/خلاصه-والیبال-صربستان-1-آمریکا-3"> <span class="news-type"></span>خلاصه والیبال صربستان 1 - آمریکا 3</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="7"><a title="معرفی سرمربیان تیم‌جوانان و نوجوانان تفنگ و تپانچه" href="https://www.varzesh3.com/news/1830286/معرفی-سرمربیان-تیم-جوانان-و-نوجوانان-تفنگ-و-تپانچه"> <span class="news-type"></span>معرفی سرمربیان تیم‌جوانان و نوجوانان تفنگ و تپانچه</a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="خلاصه والیبال برزیل 1 - لهستان 3" href="https://video.varzesh3.com/video/254260/خلاصه-والیبال-برزیل-1-لهستان-3"> <span class="news-type"></span>خلاصه والیبال برزیل 1 - لهستان 3</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="3"><a title="لیگ ملت‌های والیبال؛ لهستان فاتح دوئل بزرگ" href="https://www.varzesh3.com/news/1830281/لیگ-ملت-های-والیبال-لهستان-فاتح-دوئل-بزرگ"> <span class="news-type"></span>لیگ ملت‌های والیبال؛ لهستان فاتح دوئل بزرگ</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="5"><a title="صعود هندبال ساحلی به مرحله دوم رقابت‌های جهانی" href="https://www.varzesh3.com/news/1830252/صعود-هندبال-ساحلی-به-مرحله-دوم-رقابت-های-جهانی"> <span class="news-type"></span>صعود هندبال ساحلی به مرحله دوم رقابت‌های جهانی</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="5"><a title="ثبت نخستین امتیاز جهانی دختران هندبالیست" href="https://www.varzesh3.com/news/1830247/ثبت-نخستین-امتیاز-جهانی-دختران-هندبالیست"> <span class="news-type"></span>ثبت نخستین امتیاز جهانی دختران هندبالیست</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="17"><a title="تكواندوى ايران به دنبال باز پس گیری تاج و تخت آسیا" href="https://www.varzesh3.com/news/1830274/تكواندوى-ايران-به-دنبال-باز-پس-گیری-تاج-و-تخت-آسیا"> <span class="news-type"></span>تكواندوى ايران به دنبال باز پس گیری تاج و تخت آسیا</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="3"><a title="رونمایی از لیست ۱۶ نفره تیم ملی والیبال نوجوانان" href="https://www.varzesh3.com/news/1830266/رونمایی-از-لیست-۱۶-نفره-تیم-ملی-والیبال-نوجوانان"> <span class="news-type"></span>رونمایی از لیست ۱۶ نفره تیم ملی والیبال نوجوانان</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="34"><a title="معرفى اعضاى جديد فدراسيون كبدى" href="https://www.varzesh3.com/news/1830264/معرفى-اعضاى-جديد-فدراسيون-كبدى"> <span class="news-type"></span>معرفى اعضاى جديد فدراسيون كبدى</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="4"><a title="بسکتبال دختران نوجوان آسیا| ایران راهی امان شد" href="https://www.varzesh3.com/news/1830263/بسکتبال-دختران-نوجوان-آسیا-ایران-راهی-امان-شد"> <span class="news-type"></span>بسکتبال دختران نوجوان آسیا| ایران راهی امان شد</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="3"><a title="اسماعیل‌نژاد: امیدوارم فردا مردم را خوشحال کنیم" href="https://www.varzesh3.com/news/1830256/اسماعیل-نژاد-امیدوارم-فردا-مردم-را-خوشحال-کنیم"> <span class="news-type"></span>اسماعیل‌نژاد: امیدوارم فردا مردم را خوشحال کنیم</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="29"><a title="برترین‌های اسنوکر دسته برتر کشور معرفی شدند" href="https://www.varzesh3.com/news/1830253/برترین-های-اسنوکر-دسته-برتر-کشور-معرفی-شدند"> <span class="news-type"></span>برترین‌های اسنوکر دسته برتر کشور معرفی شدند</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="38"><a title="همایش خانواده هاکی روی یخ ایران برگزار شد" href="https://www.varzesh3.com/news/1830251/همایش-خانواده-هاکی-روی-یخ-ایران-برگزار-شد"> <span class="news-type"></span>همایش خانواده هاکی روی یخ ایران برگزار شد</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="17"><a title="ملی‌پوشان پومسه ایران حریفان خود را شناختند" href="https://www.varzesh3.com/news/1830250/ملی-پوشان-پومسه-ایران-حریفان-خود-را-شناختند"> <span class="news-type"></span>ملی‌پوشان پومسه ایران حریفان خود را شناختند</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="14"><a title="برگزاری همایش دو میدانی جام مسافر" href="https://www.varzesh3.com/news/1830249/برگزاری-همایش-دو-میدانی-جام-مسافر"> <span class="news-type"></span>برگزاری همایش دو میدانی جام مسافر</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="16"><a title="حسینوند طلا گرفت، تلاش بالی و رضایی برای برنز" href="https://www.varzesh3.com/news/1830248/حسینوند-طلا-گرفت-تلاش-بالی-و-رضایی-برای-برنز"> <span class="news-type"></span>حسینوند طلا گرفت، تلاش بالی و رضایی برای برنز</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="10"><a title="مسیر دسترسی قایقرانان اهوازی به آب باز شد" href="https://www.varzesh3.com/news/1830246/مسیر-دسترسی-قایقرانان-اهوازی-به-آب-باز-شد"> <span class="news-type"></span>مسیر دسترسی قایقرانان اهوازی به آب باز شد</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="19"><a title="سرمربی تیم ملی تنیس انتخاب شد" href="https://www.varzesh3.com/news/1830244/سرمربی-تیم-ملی-تنیس-انتخاب-شد"> <span class="news-type"></span>سرمربی تیم ملی تنیس انتخاب شد</a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="خلاصه والیبال آلمان 0 - ایتالیا 3" href="https://video.varzesh3.com/video/254245/خلاصه-والیبال-آلمان-0-ایتالیا-3"> <span class="news-type"></span>خلاصه والیبال آلمان 0 - ایتالیا 3</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="3"><a title="اولین واکنش داورزنی به نتایج ناامیدکننده تیم‌ملی" href="https://www.varzesh3.com/news/1830209/اولین-واکنش-داورزنی-به-نتایج-ناامیدکننده-تیم-ملی"> <span class="news-type"></span>اولین واکنش داورزنی به نتایج ناامیدکننده تیم‌ملی</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="3"><a title="لیگ ملت‌ها؛ چالش سخت ایران برابر تیم بدون باخت" href="https://www.varzesh3.com/news/1830181/لیگ-ملت-ها-چالش-سخت-ایران-برابر-تیم-بدون-باخت"> <span class="news-type"></span>لیگ ملت‌ها؛ چالش سخت ایران برابر تیم بدون باخت</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="16"><a title="دبیر در فدراسیون وزنه برداری(عکس)" href="https://www.varzesh3.com/news/1830177/دبیر-در-فدراسیون-وزنه-برداریعکس"> <span class="news-type"></span>دبیر در فدراسیون وزنه برداری(عکس)</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="13"><a title="بربط: طلای کشورهای اسلامی افتخاراتم را تکمیل می‌کند" href="https://www.varzesh3.com/news/1830172/بربط-طلای-کشورهای-اسلامی-افتخاراتم-را-تکمیل-می-کند"> <span class="news-type"></span>بربط: طلای کشورهای اسلامی افتخاراتم را تکمیل می‌کند</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="16"><a title="سه آزادکار ایران فینالیست شدند" href="https://www.varzesh3.com/news/1830171/سه-آزادکار-ایران-فینالیست-شدند"> <span class="news-type"></span>سه آزادکار ایران فینالیست شدند</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="20"><a title="نعمتی: سطح کشورهای اسلامی از قهرمانی آسیا بالاتر است" href="https://www.varzesh3.com/news/1830168/نعمتی-سطح-کشورهای-اسلامی-از-قهرمانی-آسیا-بالاتر-است"> <span class="news-type"></span>نعمتی: سطح کشورهای اسلامی از قهرمانی آسیا بالاتر است</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="9"><a title="دومین مدال رکابزن ایرانی در قهرمانی آسیا" href="https://www.varzesh3.com/news/1830165/دومین-مدال-رکابزن-ایرانی-در-قهرمانی-آسیا"> <span class="news-type"></span>دومین مدال رکابزن ایرانی در قهرمانی آسیا</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="16"><a title="واکنش آزادکار سنگین‌وزن طلایی آسیا درباره رقابت با زارع" href="https://www.varzesh3.com/news/1830164/واکنش-آزادکار-سنگین-وزن-طلایی-آسیا-درباره-رقابت-با-زارع"> <span class="news-type"></span>واکنش آزادکار سنگین‌وزن طلایی آسیا درباره رقابت با زارع</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="3"><a title="والیبالیست‌های جوانان در اسلوونی اردو می‌زنند" href="https://www.varzesh3.com/news/1830163/والیبالیست-های-جوانان-در-اسلوونی-اردو-می-زنند"> <span class="news-type"></span>والیبالیست‌های جوانان در اسلوونی اردو می‌زنند</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="3"><a title="تیم ملی در دادگاه جنجالی؛ پیشنهاد انصراف (عکس)" href="https://www.varzesh3.com/news/1830160/تیم-ملی-در-دادگاه-جنجالی-پیشنهاد-انصراف-عکس"> <span class="news-type"></span>تیم ملی در دادگاه جنجالی؛ پیشنهاد انصراف (عکس)</a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="صحبتهای عطایی و بازیکنان پس از شکست مقابل بلغارستان" href="https://video.varzesh3.com/video/254222/صحبتهای-عطایی-و-بازیکنان-پس-از-شکست-مقابل-بلغارستان"> <span class="news-type"></span>صحبتهای عطایی و بازیکنان پس از شکست مقابل بلغارستان</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="4"><a title="جزئیات اردوی تیم ملی بسکتبال در صربستان" href="https://www.varzesh3.com/news/1830153/جزئیات-اردوی-تیم-ملی-بسکتبال-در-صربستان"> <span class="news-type"></span>جزئیات اردوی تیم ملی بسکتبال در صربستان</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="3"><a title="نمی‌توانید بگویید شانسی ایران را بردیم" href="https://www.varzesh3.com/news/1830158/نمی-توانید-بگویید-شانسی-ایران-را-بردیم"> <span class="news-type"></span>نمی‌توانید بگویید شانسی ایران را بردیم</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="17"><a title="برنامه رقابت‌های تکواندو تورنمنت آزاد کره‌جنوبی اعلام شد" href="https://www.varzesh3.com/news/1830152/برنامه-رقابت-های-تکواندو-تورنمنت-آزاد-کره-جنوبی-اعلام-شد"> <span class="news-type"></span>برنامه رقابت‌های تکواندو تورنمنت آزاد کره‌جنوبی اعلام شد</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="16"><a title="5 فرنگی‌کار کشورمان امروز روی تشک می‌روند" href="https://www.varzesh3.com/news/1830151/5-فرنگی-کار-کشورمان-امروز-روی-تشک-می-روند"> <span class="news-type"></span>5 فرنگی‌کار کشورمان امروز روی تشک می‌روند</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="4"><a title="آغاز اردوی تیم ملی بسکتبال سه نفره از امروز" href="https://www.varzesh3.com/news/1830149/آغاز-اردوی-تیم-ملی-بسکتبال-سه-نفره-از-امروز"> <span class="news-type"></span>آغاز اردوی تیم ملی بسکتبال سه نفره از امروز</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="32"><a title="احمدکهنی: فکر کسب مدال در ژیمناستیک آسیا را می‌کردم" href="https://www.varzesh3.com/news/1830145/احمدکهنی-فکر-کسب-مدال-در-ژیمناستیک-آسیا-را-می-کردم"> <span class="news-type"></span>احمدکهنی: فکر کسب مدال در ژیمناستیک آسیا را می‌کردم</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="5"><a title="دختران هندبالیست ايران به دنبال اولین برد جهانی" href="https://www.varzesh3.com/news/1830147/دختران-هندبالیست-ايران-به-دنبال-اولین-برد-جهانی"> <span class="news-type"></span>دختران هندبالیست ايران به دنبال اولین برد جهانی</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="15"><a title="چراغ سبز «برخواه» برای بازگشت به تیم ملی وزنه‌برداری" href="https://www.varzesh3.com/news/1830143/چراغ-سبز-برخواه-برای-بازگشت-به-تیم-ملی-وزنه-برداری"> <span class="news-type"></span>چراغ سبز «برخواه» برای بازگشت به تیم ملی وزنه‌برداری</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="15"><a title="سلیمی: علی‌حسینی سرمایه وزنه‌برداری است" href="https://www.varzesh3.com/news/1830142/سلیمی-علی-حسینی-سرمایه-وزنه-برداری-است"> <span class="news-type"></span>سلیمی: علی‌حسینی سرمایه وزنه‌برداری است</a></li>
                            <li class="text-type" data-origin="3" data-media="1" data-tag="" data-sport="3"><a title="کلید غلبه بر ایران از نگاه سرمربی بلغارستان" href="https://www.varzesh3.com/news/1830141/کلید-غلبه-بر-ایران-از-نگاه-سرمربی-بلغارستان"> <span class="news-type"></span>کلید غلبه بر ایران از نگاه سرمربی بلغارستان</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="4"><a title="شاه‌علی: مسئولیت ناکامی بسکتبال نوجوانان با من است" href="https://www.varzesh3.com/news/1830138/شاه-علی-مسئولیت-ناکامی-بسکتبال-نوجوانان-با-من-است"> <span class="news-type"></span>شاه‌علی: مسئولیت ناکامی بسکتبال نوجوانان با من است</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="16"><a title="چرا انتخابی وزن 60 کیلوگرم کشتی فرنگی لغو شد؟" href="https://www.varzesh3.com/news/1830136/چرا-انتخابی-وزن-60-کیلوگرم-کشتی-فرنگی-لغو-شد"> <span class="news-type"></span>چرا انتخابی وزن 60 کیلوگرم کشتی فرنگی لغو شد؟</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="14"><a title="فدراسیون می‌گوید بودجه‌ای برای خرید نیزه نداریم!" href="https://www.varzesh3.com/news/1830135/فدراسیون-می-گوید-بودجه-ای-برای-خرید-نیزه-نداریم"> <span class="news-type"></span>فدراسیون می‌گوید بودجه‌ای برای خرید نیزه نداریم!</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="16"><a title="سرلک: امیدوارم در تونس باخت جام تختی را جبران کنم" href="https://www.varzesh3.com/news/1830134/سرلک-امیدوارم-در-تونس-باخت-جام-تختی-را-جبران-کنم"> <span class="news-type"></span>سرلک: امیدوارم در تونس باخت جام تختی را جبران کنم</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="33"><a title="اولین شکست فیروزجا در رقابت‌های کاندیداهای شطرنج" href="https://www.varzesh3.com/news/1830133/اولین-شکست-فیروزجا-در-رقابت-های-کاندیداهای-شطرنج"> <span class="news-type"></span>اولین شکست فیروزجا در رقابت‌های کاندیداهای شطرنج</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="3"><a title="عبادی‌پور: نمی‌توانم بگویم‌ مقابل بلغارستان بد بودیم!" href="https://www.varzesh3.com/news/1830132/عبادی-پور-نمی-توانم-بگویم-مقابل-بلغارستان-بد-بودیم"> <span class="news-type"></span>عبادی‌پور: نمی‌توانم بگویم‌ مقابل بلغارستان بد بودیم!</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="16"><a title="۷ آزادکار ایران از امروز به میدان می‌روند" href="https://www.varzesh3.com/news/1830131/۷-آزادکار-ایران-از-امروز-به-میدان-می-روند"> <span class="news-type"></span>۷ آزادکار ایران از امروز به میدان می‌روند</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="15"><a title="واکنش‌ها به رفتن مرادی و سرپرستی انوشیروانی" href="https://www.varzesh3.com/news/1830130/واکنش-ها-به-رفتن-مرادی-و-سرپرستی-انوشیروانی"> <span class="news-type"></span>واکنش‌ها به رفتن مرادی و سرپرستی انوشیروانی</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="14"><a title="استارت بانوی دونده نابینا برای حضور در پارالمپیک " href="https://www.varzesh3.com/news/1830129/استارت-بانوی-دونده-نابینا-برای-حضور-در-پارالمپیک"> <span class="news-type"></span>استارت بانوی دونده نابینا برای حضور در پارالمپیک </a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="3"><a title="عطایی: کم‌تجربگی تیم باعث واگذاری نتیجه شد" href="https://www.varzesh3.com/news/1830128/عطایی-کم-تجربگی-تیم-باعث-واگذاری-نتیجه-شد"> <span class="news-type"></span>عطایی: کم‌تجربگی تیم باعث واگذاری نتیجه شد</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="15"><a title="حسین رضازاده در کره جنوبی به کرونا مبتلا شد" href="https://www.varzesh3.com/news/1830124/حسین-رضازاده-در-کره-جنوبی-به-کرونا-مبتلا-شد"> <span class="news-type"></span>حسین رضازاده در کره جنوبی به کرونا مبتلا شد</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="4"><a title="حدادی: می‌توانیم گله کنیم ولی این کار را انجام نمی‌دهیم" href="https://www.varzesh3.com/news/1830123/حدادی-می-توانیم-گله-کنیم-ولی-این-کار-را-انجام-نمی-دهیم"> <span class="news-type"></span>حدادی: می‌توانیم گله کنیم ولی این کار را انجام نمی‌دهیم</a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="تحلیل شکست و عملکرد ضعیف تیم ملی والیبال" href="https://video.varzesh3.com/video/254220/تحلیل-شکست-و-عملکرد-ضعیف-تیم-ملی-والیبال"> <span class="news-type"></span>تحلیل شکست و عملکرد ضعیف تیم ملی والیبال</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="3"><a title="داور اذیت‌مان کرد؛ بلغارستان فراتر از حد انتظار بود" href="https://www.varzesh3.com/news/1830122/داور-اذیت-مان-کرد-بلغارستان-فراتر-از-حد-انتظار-بود"> <span class="news-type"></span>داور اذیت‌مان کرد؛ بلغارستان فراتر از حد انتظار بود</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="3"><a title="توجیه عجیب اسفندیار؛ داور چند اشتباه داشت!" href="https://www.varzesh3.com/news/1830120/توجیه-عجیب-اسفندیار-داور-چند-اشتباه-داشت"> <span class="news-type"></span>توجیه عجیب اسفندیار؛ داور چند اشتباه داشت!</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="3"><a title="اسماعیل‌نژاد امتیاز آورترین بازیکن ایران مقابل بلغارستان " href="https://www.varzesh3.com/news/1830119/اسماعیل-نژاد-امتیاز-آورترین-بازیکن-ایران-مقابل-بلغارستان"> <span class="news-type"></span>اسماعیل‌نژاد امتیاز آورترین بازیکن ایران مقابل بلغارستان </a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="خلاصه والیبال ایران 0 - بلغارستان 3" href="https://video.varzesh3.com/video/254218/خلاصه-والیبال-ایران-0-بلغارستان-3"> <span class="news-type"></span>خلاصه والیبال ایران 0 - بلغارستان 3</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="3"><a title="بلغارستان ۳-۰ ایران؛ نگران کننده، اعصاب خردکن و تلخ" href="https://www.varzesh3.com/news/1830109/بلغارستان-۳-۰-ایران-نگران-کننده-اعصاب-خردکن-و-تلخ"> <span class="news-type"></span>بلغارستان ۳-۰ ایران؛ نگران کننده، اعصاب خردکن و تلخ</a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="خلاصه والیبال کانادا 3 - استرالیا 1" href="https://video.varzesh3.com/video/254217/خلاصه-والیبال-کانادا-3-استرالیا-1"> <span class="news-type"></span>خلاصه والیبال کانادا 3 - استرالیا 1</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="6"><a title="نتایج کماندران ایران در دور مقدماتی جام جهانی پاریس" href="https://www.varzesh3.com/news/1830125/نتایج-کماندران-ایران-در-دور-مقدماتی-جام-جهانی-پاریس"> <span class="news-type"></span>نتایج کماندران ایران در دور مقدماتی جام جهانی پاریس</a></li>
                            <li class="text-type" data-origin="2" data-media="1" data-tag="" data-sport="3"><a title="لیگ ملت‌ها؛ کامبک کانادا علیه اولین برد استرالیا" href="https://www.varzesh3.com/news/1830106/لیگ-ملت-ها-کامبک-کانادا-علیه-اولین-برد-استرالیا"> <span class="news-type"></span>لیگ ملت‌ها؛ کامبک کانادا علیه اولین برد استرالیا</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="17"><a title="معرفی نونهالان اعزامی به رقابتهای تکواندو قهرمانی جهان" href="https://www.varzesh3.com/news/1830098/معرفی-نونهالان-اعزامی-به-رقابتهای-تکواندو-قهرمانی-جهان"> <span class="news-type"></span>معرفی نونهالان اعزامی به رقابتهای تکواندو قهرمانی جهان</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="16"><a title="کشتی آزاد نوجوانان آسیا؛ شفیعی به مدال برنز رسید" href="https://www.varzesh3.com/news/1830099/کشتی-آزاد-نوجوانان-آسیا-شفیعی-به-مدال-برنز-رسید"> <span class="news-type"></span>کشتی آزاد نوجوانان آسیا؛ شفیعی به مدال برنز رسید</a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="صحبت های عطایی قبل از بازی با بلغارستان" href="https://video.varzesh3.com/video/254204/صحبت-های-عطایی-قبل-از-بازی-با-بلغارستان"> <span class="news-type"></span>صحبت های عطایی قبل از بازی با بلغارستان</a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="خلاصه والیبال ژاپن 3 - آرژانتین 1" href="https://video.varzesh3.com/video/254205/خلاصه-والیبال-ژاپن-3-آرژانتین-1"> <span class="news-type"></span>خلاصه والیبال ژاپن 3 - آرژانتین 1</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="5"><a title="ساحلی‌بازان ایران در آستانه حذف از رقابت‌های جهانی" href="https://www.varzesh3.com/news/1830101/ساحلی-بازان-ایران-در-آستانه-حذف-از-رقابت-های-جهانی"> <span class="news-type"></span>ساحلی‌بازان ایران در آستانه حذف از رقابت‌های جهانی</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="3"><a title="ژاپن با این فوق ستاره در مسیر خوشبختی" href="https://www.varzesh3.com/news/1830088/ژاپن-با-این-فوق-ستاره-در-مسیر-خوشبختی"> <span class="news-type"></span>ژاپن با این فوق ستاره در مسیر خوشبختی</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="3"><a title="لیگ ملت‌ها؛ ژاپن تیم سوم المپیک را هم به زانو درآورد" href="https://www.varzesh3.com/news/1830085/لیگ-ملت-ها-ژاپن-تیم-سوم-المپیک-را-هم-به-زانو-درآورد"> <span class="news-type"></span>لیگ ملت‌ها؛ ژاپن تیم سوم المپیک را هم به زانو درآورد</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="3"><a title="آشنایی با اولین حریف ایران در هفته دوم لیگ‌ملت‌ها" href="https://www.varzesh3.com/news/1830051/آشنایی-با-اولین-حریف-ایران-در-هفته-دوم-لیگ-ملت-ها"> <span class="news-type"></span>آشنایی با اولین حریف ایران در هفته دوم لیگ‌ملت‌ها</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="3"><a title="لیگ ملت‌ها؛ غیرقابل مهار مثل نیمیر عبدالعزیز" href="https://www.varzesh3.com/news/1830050/لیگ-ملت-ها-غیرقابل-مهار-مثل-نیمیر-عبدالعزیز"> <span class="news-type"></span>لیگ ملت‌ها؛ غیرقابل مهار مثل نیمیر عبدالعزیز</a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="خلاصه والیبال اسلوونی 0 - هلند 3" href="https://video.varzesh3.com/video/254193/خلاصه-والیبال-اسلوونی-0-هلند-3"> <span class="news-type"></span>خلاصه والیبال اسلوونی 0 - هلند 3</a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="5 لحظه مهیج از موتو جی پی آلمان 2022" href="https://video.varzesh3.com/video/254140/5-لحظه-مهیج-از-موتو-جی-پی-آلمان-2022"> <span class="news-type"></span>5 لحظه مهیج از موتو جی پی آلمان 2022</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="3"><a title="رونمایی از ۲۲ بازیکن منتخب تیم‌ملی والیبال زنان" href="https://www.varzesh3.com/news/1830028/رونمایی-از-۲۲-بازیکن-منتخب-تیم-ملی-والیبال-زنان"> <span class="news-type"></span>رونمایی از ۲۲ بازیکن منتخب تیم‌ملی والیبال زنان</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="5"><a title="شکست ایران در دیدار نخست هندبال ساحلی " href="https://www.varzesh3.com/news/1830019/شکست-ایران-در-دیدار-نخست-هندبال-ساحلی"> <span class="news-type"></span>شکست ایران در دیدار نخست هندبال ساحلی </a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="3"><a title="دعوت رسمی فدراسیون والیبال روسیه از تیم ملی" href="https://www.varzesh3.com/news/1830012/دعوت-رسمی-فدراسیون-والیبال-روسیه-از-تیم-ملی"> <span class="news-type"></span>دعوت رسمی فدراسیون والیبال روسیه از تیم ملی</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="24"><a title="مردان والیبال نشسته اعزامی به ترکیه معرفی شدند" href="https://www.varzesh3.com/news/1830010/مردان-والیبال-نشسته-اعزامی-به-ترکیه-معرفی-شدند"> <span class="news-type"></span>مردان والیبال نشسته اعزامی به ترکیه معرفی شدند</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="11"><a title="سرمربی تیم ملی سابر: فخری جدا از کادرفنی نیست" href="https://www.varzesh3.com/news/1830009/سرمربی-تیم-ملی-سابر-فخری-جدا-از-کادرفنی-نیست"> <span class="news-type"></span>سرمربی تیم ملی سابر: فخری جدا از کادرفنی نیست</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="3"><a title="حمایت حضوری رئیس فدراسیون از ملی‌پوشان‌ والیبال" href="https://www.varzesh3.com/news/1830005/حمایت-حضوری-رئیس-فدراسیون-از-ملی-پوشان-والیبال"> <span class="news-type"></span>حمایت حضوری رئیس فدراسیون از ملی‌پوشان‌ والیبال</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="4"><a title="لیگ NBA؛ تمایل لیکرز برای جذب اروینگ" href="https://www.varzesh3.com/news/1829999/لیگ-nba-تمایل-لیکرز-برای-جذب-اروینگ"> <span class="news-type"></span>لیگ NBA؛ تمایل لیکرز برای جذب اروینگ</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="3"><a title="ستاره مغضوب ایرانی‌ها بسکتبالیست شد! (عکس)" href="https://www.varzesh3.com/news/1830000/ستاره-مغضوب-ایرانی-ها-بسکتبالیست-شد-عکس"> <span class="news-type"></span>ستاره مغضوب ایرانی‌ها بسکتبالیست شد! (عکس)</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="15"><a title="بهترين خبر براى وزنه برداران؛ اعتصاب به پايان مى‌رسد" href="https://www.varzesh3.com/news/1830003/بهترين-خبر-براى-وزنه-برداران-اعتصاب-به-پايان-مى-رسد"> <span class="news-type"></span>بهترين خبر براى وزنه برداران؛ اعتصاب به پايان مى‌رسد</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="22"><a title="سجادی: از شرکت توسعه انتظار سوددهی نداریم" href="https://www.varzesh3.com/news/1829997/سجادی-از-شرکت-توسعه-انتظار-سوددهی-نداریم"> <span class="news-type"></span>سجادی: از شرکت توسعه انتظار سوددهی نداریم</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="36"><a title="حضور گلف در سومین دوره المپیاد استعدادهای برتر ورزش کشور" href="https://www.varzesh3.com/news/1829996/حضور-گلف-در-سومین-دوره-المپیاد-استعدادهای-برتر-ورزش-کشور"> <span class="news-type"></span>حضور گلف در سومین دوره المپیاد استعدادهای برتر ورزش کشور</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="3"><a title="می دانیم‌ که بازی راحتی مقابل ایران نداریم" href="https://www.varzesh3.com/news/1829992/می-دانیم-که-بازی-راحتی-مقابل-ایران-نداریم"> <span class="news-type"></span>می دانیم‌ که بازی راحتی مقابل ایران نداریم</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="22"><a title="افتتاح استخر قهرمانی مجموعه کشوری با حضور وزیر ورزش" href="https://www.varzesh3.com/news/1829990/افتتاح-استخر-قهرمانی-مجموعه-کشوری-با-حضور-وزیر-ورزش"> <span class="news-type"></span>افتتاح استخر قهرمانی مجموعه کشوری با حضور وزیر ورزش</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="16"><a title="عدم برگزاری مسابقه انتخابی در 60 کیلوگرم کشتی فرنگی " href="https://www.varzesh3.com/news/1829989/عدم-برگزاری-مسابقه-انتخابی-در-60-کیلوگرم-کشتی-فرنگی"> <span class="news-type"></span>عدم برگزاری مسابقه انتخابی در 60 کیلوگرم کشتی فرنگی </a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="3"><a title="عطایی: کار دشواری داریم اما به پیروزی امیدوارم" href="https://www.varzesh3.com/news/1829987/عطایی-کار-دشواری-داریم-اما-به-پیروزی-امیدوارم"> <span class="news-type"></span>عطایی: کار دشواری داریم اما به پیروزی امیدوارم</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="3"><a title="لیگ ملت‌ها؛ کرونایی‌های ژاپن به موقع رسیدند" href="https://www.varzesh3.com/news/1829986/لیگ-ملت-ها-کرونایی-های-ژاپن-به-موقع-رسیدند"> <span class="news-type"></span>لیگ ملت‌ها؛ کرونایی‌های ژاپن به موقع رسیدند</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="19"><a title="اسطوره‌ها در ویمبلدون راکت به‌دست شدند" href="https://www.varzesh3.com/news/1829984/اسطوره-ها-در-ویمبلدون-راکت-به-دست-شدند"> <span class="news-type"></span>اسطوره‌ها در ویمبلدون راکت به‌دست شدند</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="15"><a title="انوشيروانى سرپرست فدراسيون وزنه بردارى شد" href="https://www.varzesh3.com/news/1829982/انوشيروانى-سرپرست-فدراسيون-وزنه-بردارى-شد"> <span class="news-type"></span>انوشيروانى سرپرست فدراسيون وزنه بردارى شد</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="15"><a title="ریاست علی مرادی به انتخابات IWF نرسید" href="https://www.varzesh3.com/news/1829981/ریاست-علی-مرادی-به-انتخابات-iwf-نرسید"> <span class="news-type"></span>ریاست علی مرادی به انتخابات IWF نرسید</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="3"><a title="مشکل جدید در بلغارستان؛ تاخیر اتوبوس تیم ملی" href="https://www.varzesh3.com/news/1829972/مشکل-جدید-در-بلغارستان-تاخیر-اتوبوس-تیم-ملی"> <span class="news-type"></span>مشکل جدید در بلغارستان؛ تاخیر اتوبوس تیم ملی</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="33"><a title="سرمربیان تیم‌های ملی شطرنج معرفی شدند" href="https://www.varzesh3.com/news/1829970/سرمربیان-تیم-های-ملی-شطرنج-معرفی-شدند"> <span class="news-type"></span>سرمربیان تیم‌های ملی شطرنج معرفی شدند</a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="برترین های کلی تامپسون در رقابتهای فینال NBA" href="https://video.varzesh3.com/video/254089/برترین-های-کلی-تامپسون-در-رقابتهای-فینال-nba"> <span class="news-type"></span>برترین های کلی تامپسون در رقابتهای فینال NBA</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="14"><a title="کسب چهارمین سهمیه رقابت‌های دوومیدانی جهانی" href="https://www.varzesh3.com/news/1829961/کسب-چهارمین-سهمیه-رقابت-های-دوومیدانی-جهانی"> <span class="news-type"></span>کسب چهارمین سهمیه رقابت‌های دوومیدانی جهانی</a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="صحبتهای کاپیتان عبادی‌پور پیش از آغاز هفته دوم " href="https://video.varzesh3.com/video/254141/صحبتهای-کاپیتان-عبادی-پور-پیش-از-آغاز-هفته-دوم"> <span class="news-type"></span>صحبتهای کاپیتان عبادی‌پور پیش از آغاز هفته دوم </a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="3"><a title="برنامه تیم ملی تا مسابقه با بلغارستان مشخص شد" href="https://www.varzesh3.com/news/1829952/برنامه-تیم-ملی-تا-مسابقه-با-بلغارستان-مشخص-شد"> <span class="news-type"></span>برنامه تیم ملی تا مسابقه با بلغارستان مشخص شد</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="3"><a title="لیگ ملت‌ها؛ فرانسه بدون بازی سه امتیاز گرفت!" href="https://www.varzesh3.com/news/1829949/لیگ-ملت-ها-فرانسه-بدون-بازی-سه-امتیاز-گرفت"> <span class="news-type"></span>لیگ ملت‌ها؛ فرانسه بدون بازی سه امتیاز گرفت!</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="16"><a title="کشتی فرنگی نوجوانان ایران نایب قهرمان آسیا شد" href="https://www.varzesh3.com/news/1829947/کشتی-فرنگی-نوجوانان-ایران-نایب-قهرمان-آسیا-شد"> <span class="news-type"></span>کشتی فرنگی نوجوانان ایران نایب قهرمان آسیا شد</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="36"><a title="تاریخ انتخابات گلف اعلام شد" href="https://www.varzesh3.com/news/1829945/تاریخ-انتخابات-گلف-اعلام-شد"> <span class="news-type"></span>تاریخ انتخابات گلف اعلام شد</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="3"><a title="معرفی سرمربی تیم والیبال بانوان پیکان" href="https://www.varzesh3.com/news/1829941/معرفی-سرمربی-تیم-والیبال-بانوان-پیکان"> <span class="news-type"></span>معرفی سرمربی تیم والیبال بانوان پیکان</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="15"><a title="واکنش وزنه‌برداران معترض به تغییر رئیس فدراسیون" href="https://www.varzesh3.com/news/1829930/واکنش-وزنه-برداران-معترض-به-تغییر-رئیس-فدراسیون"> <span class="news-type"></span>واکنش وزنه‌برداران معترض به تغییر رئیس فدراسیون</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="9"><a title="دوچرخه‌سواری پیست آسیا؛ گنج خانلو به برنز رسید" href="https://www.varzesh3.com/news/1829926/دوچرخه-سواری-پیست-آسیا-گنج-خانلو-به-برنز-رسید"> <span class="news-type"></span>دوچرخه‌سواری پیست آسیا؛ گنج خانلو به برنز رسید</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="16"><a title="انتخابی وزن 60 کیلوگرم فرنگی لغو شد!" href="https://www.varzesh3.com/news/1829911/انتخابی-وزن-60-کیلوگرم-فرنگی-لغو-شد"> <span class="news-type"></span>انتخابی وزن 60 کیلوگرم فرنگی لغو شد!</a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="خلاصه هندبال بارسلونا - کیلتسه (فینال قهرمانی اروپا)" href="https://video.varzesh3.com/video/254133/خلاصه-هندبال-بارسلونا-کیلتسه-فینال-قهرمانی-اروپا"> <span class="news-type"></span>خلاصه هندبال بارسلونا - کیلتسه (فینال قهرمانی اروپا)</a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="خلاصه بسکتبال رئال مادرید - بارسلونا (فینال)" href="https://video.varzesh3.com/video/254129/خلاصه-بسکتبال-رئال-مادرید-بارسلونا-فینال"> <span class="news-type"></span>خلاصه بسکتبال رئال مادرید - بارسلونا (فینال)</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="3"><a title="آنالیز بلغارستان برای شروع خوب در هفته دوم (عکس)" href="https://www.varzesh3.com/news/1829900/آنالیز-بلغارستان-برای-شروع-خوب-در-هفته-دوم-عکس"> <span class="news-type"></span>آنالیز بلغارستان برای شروع خوب در هفته دوم (عکس)</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="15"><a title="دورخیز پاورلیفتینگ ایران برای فتح قاره کهن" href="https://www.varzesh3.com/news/1829899/دورخیز-پاورلیفتینگ-ایران-برای-فتح-قاره-کهن"> <span class="news-type"></span>دورخیز پاورلیفتینگ ایران برای فتح قاره کهن</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="5"><a title="مدال تاریخی هندبال ایران چگونه به ثبت رسید؟" href="https://www.varzesh3.com/news/1829893/مدال-تاریخی-هندبال-ایران-چگونه-به-ثبت-رسید"> <span class="news-type"></span>مدال تاریخی هندبال ایران چگونه به ثبت رسید؟</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="5"><a title="اعزام ملی‌پوشان هندبال ساحلی بزرگسالان ایران به یونان" href="https://www.varzesh3.com/news/1829883/اعزام-ملی-پوشان-هندبال-ساحلی-بزرگسالان-ایران-به-یونان"> <span class="news-type"></span>اعزام ملی‌پوشان هندبال ساحلی بزرگسالان ایران به یونان</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="16"><a title="مرادی و آذرشب فینالیست‌های کشتی فرنگی نوجوانان آسیا" href="https://www.varzesh3.com/news/1829877/مرادی-و-آذرشب-فینالیست-های-کشتی-فرنگی-نوجوانان-آسیا"> <span class="news-type"></span>مرادی و آذرشب فینالیست‌های کشتی فرنگی نوجوانان آسیا</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="3"><a title="لیگ ملت‌ها؛ ژاپن در بخش زنان هم قدرت‌نمایی می‌کند" href="https://www.varzesh3.com/news/1829873/لیگ-ملت-ها-ژاپن-در-بخش-زنان-هم-قدرت-نمایی-می-کند"> <span class="news-type"></span>لیگ ملت‌ها؛ ژاپن در بخش زنان هم قدرت‌نمایی می‌کند</a></li>
                            <li class="text-type" data-origin="2" data-media="1" data-tag="" data-sport="4"><a title="سی و ششمین قهرمانی بسکتبال رئال با شکست بارسا" href="https://www.varzesh3.com/news/1829870/سی-و-ششمین-قهرمانی-بسکتبال-رئال-با-شکست-بارسا"> <span class="news-type"></span>سی و ششمین قهرمانی بسکتبال رئال با شکست بارسا</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="15"><a title="رییس وزنه برداری بالاخره رفتنی شد؟" href="https://www.varzesh3.com/news/1829868/رییس-وزنه-برداری-بالاخره-رفتنی-شد"> <span class="news-type"></span>رییس وزنه برداری بالاخره رفتنی شد؟</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="16"><a title="صفایی: فقر ورزشكار و كشتي‌گير در تهران بيداد مي‌كند" href="https://www.varzesh3.com/news/1829912/صفایی-فقر-ورزشكار-و-كشتي-گير-در-تهران-بيداد-مي-كند"> <span class="news-type"></span>صفایی: فقر ورزشكار و كشتي‌گير در تهران بيداد مي‌كند</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="3"><a title="لیگ ملت‌ها؛ بلغارستان به دنبال طلسم‌شکنی برابر ایران" href="https://www.varzesh3.com/news/1829864/لیگ-ملت-ها-بلغارستان-به-دنبال-طلسم-شکنی-برابر-ایران"> <span class="news-type"></span>لیگ ملت‌ها؛ بلغارستان به دنبال طلسم‌شکنی برابر ایران</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="12"><a title="پیروزی دو فایتر ایرانی در رینگ K1 ژاپن" href="https://www.varzesh3.com/news/1829863/پیروزی-دو-فایتر-ایرانی-در-رینگ-k1-ژاپن"> <span class="news-type"></span>پیروزی دو فایتر ایرانی در رینگ K1 ژاپن</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="9"><a title="اولین مدال دوچرخه سواری پیست به نام دختر ایرانی" href="https://www.varzesh3.com/news/1829857/اولین-مدال-دوچرخه-سواری-پیست-به-نام-دختر-ایرانی"> <span class="news-type"></span>اولین مدال دوچرخه سواری پیست به نام دختر ایرانی</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="3"><a title="شروع تمرینات تیم والیبال سپاهان با اهداف جدید" href="https://www.varzesh3.com/news/1829853/شروع-تمرینات-تیم-والیبال-سپاهان-با-اهداف-جدید"> <span class="news-type"></span>شروع تمرینات تیم والیبال سپاهان با اهداف جدید</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="12"><a title="10 بوکسور به اردوی تیم‌ملی راه پیدا کردند" href="https://www.varzesh3.com/news/1829849/10-بوکسور-به-اردوی-تیم-ملی-راه-پیدا-کردند"> <span class="news-type"></span>10 بوکسور به اردوی تیم‌ملی راه پیدا کردند</a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="تحلیل مسابقات لیگ والیبال ملت ها و عملکرد ایران" href="https://video.varzesh3.com/video/254122/تحلیل-مسابقات-لیگ-والیبال-ملت-ها-و-عملکرد-ایران"> <span class="news-type"></span>تحلیل مسابقات لیگ والیبال ملت ها و عملکرد ایران</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="25"><a title="فرمول یک| برتری فرستاپن در گرندپری مونترئال" href="https://www.varzesh3.com/news/1829848/فرمول-یک-برتری-فرستاپن-در-گرندپری-مونترئال"> <span class="news-type"></span>فرمول یک| برتری فرستاپن در گرندپری مونترئال</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="8"><a title="قارداشی: عملکرد نوشاد در کرواسی امیدوارکننده بود" href="https://www.varzesh3.com/news/1829847/قارداشی-عملکرد-نوشاد-در-کرواسی-امیدوارکننده-بود"> <span class="news-type"></span>قارداشی: عملکرد نوشاد در کرواسی امیدوارکننده بود</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="16"><a title="تیم منتخب کشتی فرنگی ایران راهی ایتالیا شد" href="https://www.varzesh3.com/news/1829844/تیم-منتخب-کشتی-فرنگی-ایران-راهی-ایتالیا-شد"> <span class="news-type"></span>تیم منتخب کشتی فرنگی ایران راهی ایتالیا شد</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="16"><a title="عباس‌پور: بعد از مسابقات جهانی شرایط برایم سخت شد" href="https://www.varzesh3.com/news/1829842/عباس-پور-بعد-از-مسابقات-جهانی-شرایط-برایم-سخت-شد"> <span class="news-type"></span>عباس‌پور: بعد از مسابقات جهانی شرایط برایم سخت شد</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="19"><a title="خط‌و‌نشان برتینی و هورکاچ برای ویمبلدون" href="https://www.varzesh3.com/news/1829841/خط-و-نشان-برتینی-و-هورکاچ-برای-ویمبلدون"> <span class="news-type"></span>خط‌و‌نشان برتینی و هورکاچ برای ویمبلدون</a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="دست رد ستاره فرانسوی به سینه بهترین تیم دنیا" href="https://video.varzesh3.com/video/254111/دست-رد-ستاره-فرانسوی-به-سینه-بهترین-تیم-دنیا"> <span class="news-type"></span>دست رد ستاره فرانسوی به سینه بهترین تیم دنیا</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="3"><a title="عبادی پور: کسب تجربه اولویت ما در لیگ ملت‌هاست" href="https://www.varzesh3.com/news/1829826/عبادی-پور-کسب-تجربه-اولویت-ما-در-لیگ-ملت-هاست"> <span class="news-type"></span>عبادی پور: کسب تجربه اولویت ما در لیگ ملت‌هاست</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="3"><a title="عطایی: چند روز اول خوابم نمی‌برد و شرایط سخت بود" href="https://www.varzesh3.com/news/1829825/عطایی-چند-روز-اول-خوابم-نمی-برد-و-شرایط-سخت-بود"> <span class="news-type"></span>عطایی: چند روز اول خوابم نمی‌برد و شرایط سخت بود</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="3"><a title="در تمرین امروز تیم ملی والیبال چه گذشت؟" href="https://www.varzesh3.com/news/1829819/در-تمرین-امروز-تیم-ملی-والیبال-چه-گذشت"> <span class="news-type"></span>در تمرین امروز تیم ملی والیبال چه گذشت؟</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="3"><a title="جدایی ستاره ملی‌پوش از تیم قهرمان تایید شد" href="https://www.varzesh3.com/news/1829818/جدایی-ستاره-ملی-پوش-از-تیم-قهرمان-تایید-شد"> <span class="news-type"></span>جدایی ستاره ملی‌پوش از تیم قهرمان تایید شد</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="9"><a title="دختر رکابزن ایران مدال برنز گرفت" href="https://www.varzesh3.com/news/1829811/دختر-رکابزن-ایران-مدال-برنز-گرفت"> <span class="news-type"></span>دختر رکابزن ایران مدال برنز گرفت</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="37"><a title="موتوجی‌پی؛ موتورسوار فرانسوی فاتح مرحله دهم شد" href="https://www.varzesh3.com/news/1829809/موتوجی-پی-موتورسوار-فرانسوی-فاتح-مرحله-دهم-شد"> <span class="news-type"></span>موتوجی‌پی؛ موتورسوار فرانسوی فاتح مرحله دهم شد</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="16"><a title="کسب ۶ مدال رنگارنگ توسط فرنگی‌کاران ایران" href="https://www.varzesh3.com/news/1829807/کسب-۶-مدال-رنگارنگ-توسط-فرنگی-کاران-ایران"> <span class="news-type"></span>کسب ۶ مدال رنگارنگ توسط فرنگی‌کاران ایران</a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="برترین های دریموند گرین در رقابتهای فینال NBA" href="https://video.varzesh3.com/video/254091/برترین-های-دریموند-گرین-در-رقابتهای-فینال-nba"> <span class="news-type"></span>برترین های دریموند گرین در رقابتهای فینال NBA</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="5"><a title="نخستین مدال جهانی تاریخ هندبال ایران به نام نوجوانان" href="https://www.varzesh3.com/news/1829801/نخستین-مدال-جهانی-تاریخ-هندبال-ایران-به-نام-نوجوانان"> <span class="news-type"></span>نخستین مدال جهانی تاریخ هندبال ایران به نام نوجوانان</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="4"><a title="پایان ناامید کننده نوجوانان بسکتبال در آسیا" href="https://www.varzesh3.com/news/1829810/پایان-ناامید-کننده-نوجوانان-بسکتبال-در-آسیا"> <span class="news-type"></span>پایان ناامید کننده نوجوانان بسکتبال در آسیا</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="3"><a title="تقابل ایران و بلغارستان مانند یک دربی است" href="https://www.varzesh3.com/news/1829794/تقابل-ایران-و-بلغارستان-مانند-یک-دربی-است"> <span class="news-type"></span>تقابل ایران و بلغارستان مانند یک دربی است</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="3"><a title="اسطوره بلغارستان، مهمان ویژه تمرین تیم ملی والیبال" href="https://www.varzesh3.com/news/1829784/اسطوره-بلغارستان-مهمان-ویژه-تمرین-تیم-ملی-والیبال"> <span class="news-type"></span>اسطوره بلغارستان، مهمان ویژه تمرین تیم ملی والیبال</a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="صحبت‌های رمضانی و سعادت در آستانه هفته دوم" href="https://video.varzesh3.com/video/254105/صحبت-های-رمضانی-و-سعادت-در-آستانه-هفته-دوم"> <span class="news-type"></span>صحبت‌های رمضانی و سعادت در آستانه هفته دوم</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="3"><a title="پاسخ جالب ملی پوش والیبال به انتقاد از مربی ایرانی" href="https://www.varzesh3.com/news/1829781/پاسخ-جالب-ملی-پوش-والیبال-به-انتقاد-از-مربی-ایرانی"> <span class="news-type"></span>پاسخ جالب ملی پوش والیبال به انتقاد از مربی ایرانی</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="16"><a title="کشتی پایتخت، دور از روزهای اوج و طلایی" href="https://www.varzesh3.com/news/1829778/کشتی-پایتخت-دور-از-روزهای-اوج-و-طلایی"> <span class="news-type"></span>کشتی پایتخت، دور از روزهای اوج و طلایی</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="3"><a title="دردسرهای غیرمنتظره ملی پوشان والیبال در بلغارستان" href="https://www.varzesh3.com/news/1829774/دردسرهای-غیرمنتظره-ملی-پوشان-والیبال-در-بلغارستان"> <span class="news-type"></span>دردسرهای غیرمنتظره ملی پوشان والیبال در بلغارستان</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="4"><a title="بسکتبال زیر 16 سال آسیا؛ ایران هشتم شد" href="https://www.varzesh3.com/news/1829772/بسکتبال-زیر-16-سال-آسیا-ایران-هشتم-شد"> <span class="news-type"></span>بسکتبال زیر 16 سال آسیا؛ ایران هشتم شد</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="3"><a title="انگیزه زیادی دارم؛ می‌خواهیم دل مردم را شاد کنیم" href="https://www.varzesh3.com/news/1829767/انگیزه-زیادی-دارم-می-خواهیم-دل-مردم-را-شاد-کنیم"> <span class="news-type"></span>انگیزه زیادی دارم؛ می‌خواهیم دل مردم را شاد کنیم</a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="محمدی: ببخشید؛ اجازه صحبت ندارم" href="https://video.varzesh3.com/video/254101/محمدی-ببخشید-اجازه-صحبت-ندارم"> <span class="news-type"></span>محمدی: ببخشید؛ اجازه صحبت ندارم</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="15"><a title="دیدار وزنه‌برداران معترض با معاون وزیر ورزش" href="https://www.varzesh3.com/news/1829762/دیدار-وزنه-برداران-معترض-با-معاون-وزیر-ورزش"> <span class="news-type"></span>دیدار وزنه‌برداران معترض با معاون وزیر ورزش</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="3"><a title="تمرین با وزنه برای شروع قدرتمند در هفته دوم (عکس)" href="https://www.varzesh3.com/news/1829751/تمرین-با-وزنه-برای-شروع-قدرتمند-در-هفته-دوم-عکس"> <span class="news-type"></span>تمرین با وزنه برای شروع قدرتمند در هفته دوم (عکس)</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="3"><a title="مطمئن هستم بلغارستان را شکست خواهیم داد" href="https://www.varzesh3.com/news/1829749/مطمئن-هستم-بلغارستان-را-شکست-خواهیم-داد"> <span class="news-type"></span>مطمئن هستم بلغارستان را شکست خواهیم داد</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="3"><a title="وعده ویژه مربی ایران برای هفته دوم لیگ ملت‌ها" href="https://www.varzesh3.com/news/1829744/وعده-ویژه-مربی-ایران-برای-هفته-دوم-لیگ-ملت-ها"> <span class="news-type"></span>وعده ویژه مربی ایران برای هفته دوم لیگ ملت‌ها</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="3"><a title="مورد عجیب تمرین تیم‌ ملی والیبال در بلغارستان" href="https://www.varzesh3.com/news/1829745/مورد-عجیب-تمرین-تیم-ملی-والیبال-در-بلغارستان"> <span class="news-type"></span>مورد عجیب تمرین تیم‌ ملی والیبال در بلغارستان</a></li>
                            <li class="text-type" data-origin="2" data-media="1" data-tag="" data-sport="3"><a title="فوق ستاره دنیای والیبال با عبادی‌پور هم‌تیمی می‌شود؟" href="https://www.varzesh3.com/news/1829738/فوق-ستاره-دنیای-والیبال-با-عبادی-پور-هم-تیمی-می-شود"> <span class="news-type"></span>فوق ستاره دنیای والیبال با عبادی‌پور هم‌تیمی می‌شود؟</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="16"><a title="چهار فرنگی‌کار ایران راهی فینال شدند" href="https://www.varzesh3.com/news/1829726/چهار-فرنگی-کار-ایران-راهی-فینال-شدند"> <span class="news-type"></span>چهار فرنگی‌کار ایران راهی فینال شدند</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="7"><a title="آغاز اردوی ملی‌پوشان تپانچه از امروز" href="https://www.varzesh3.com/news/1829725/آغاز-اردوی-ملی-پوشان-تپانچه-از-امروز"> <span class="news-type"></span>آغاز اردوی ملی‌پوشان تپانچه از امروز</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="4"><a title="می‌ودر NBA را به لاس وگاس می‌برد؟" href="https://www.varzesh3.com/news/1829724/می-ودر-nba-را-به-لاس-وگاس-می-برد"> <span class="news-type"></span>می‌ودر NBA را به لاس وگاس می‌برد؟</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="3"><a title="لیگ ملت‌ها؛ دوئل جدید در پستی که مدعی زیاد دارد" href="https://www.varzesh3.com/news/1829723/لیگ-ملت-ها-دوئل-جدید-در-پستی-که-مدعی-زیاد-دارد"> <span class="news-type"></span>لیگ ملت‌ها؛ دوئل جدید در پستی که مدعی زیاد دارد</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="16"><a title="خداحافظی مرد یخی با چاشنی باخت عمدی گرایی!" href="https://www.varzesh3.com/news/1829715/خداحافظی-مرد-یخی-با-چاشنی-باخت-عمدی-گرایی"> <span class="news-type"></span>خداحافظی مرد یخی با چاشنی باخت عمدی گرایی!</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="11"><a title="پاکدامن: تیم سابر اتفاقات بزرگی را رقم می‌زند" href="https://www.varzesh3.com/news/1829712/پاکدامن-تیم-سابر-اتفاقات-بزرگی-را-رقم-می-زند"> <span class="news-type"></span>پاکدامن: تیم سابر اتفاقات بزرگی را رقم می‌زند</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="3"><a title="والیبال روسیه علیه محرومیت؛ ایران هم دعوت می‌شود" href="https://www.varzesh3.com/news/1829710/والیبال-روسیه-علیه-محرومیت-ایران-هم-دعوت-می-شود"> <span class="news-type"></span>والیبال روسیه علیه محرومیت؛ ایران هم دعوت می‌شود</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="16"><a title="تیم منتخب کشتی فرنگی بامداد فردا راهی ایتالیا می‌شود" href="https://www.varzesh3.com/news/1829703/تیم-منتخب-کشتی-فرنگی-بامداد-فردا-راهی-ایتالیا-می-شود"> <span class="news-type"></span>تیم منتخب کشتی فرنگی بامداد فردا راهی ایتالیا می‌شود</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="14"><a title="اعزام 6 دوومیدانی‌کار به جام کازانوف قزاقستان" href="https://www.varzesh3.com/news/1829702/اعزام-6-دوومیدانی-کار-به-جام-کازانوف-قزاقستان"> <span class="news-type"></span>اعزام 6 دوومیدانی‌کار به جام کازانوف قزاقستان</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="3"><a title="یک خواهش عاجزانه؛ لطفا این بازیکنان را نسوزانید " href="https://www.varzesh3.com/news/1829693/یک-خواهش-عاجزانه-لطفا-این-بازیکنان-را-نسوزانید"> <span class="news-type"></span>یک خواهش عاجزانه؛ لطفا این بازیکنان را نسوزانید </a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="3"><a title="زمان بازگشت سرعتی زن تیم ملی والیبال مشخص شد" href="https://www.varzesh3.com/news/1829691/زمان-بازگشت-سرعتی-زن-تیم-ملی-والیبال-مشخص-شد"> <span class="news-type"></span>زمان بازگشت سرعتی زن تیم ملی والیبال مشخص شد</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="33"><a title="دومین تساوی فیروزجا در رقابت‌های کاندیداها" href="https://www.varzesh3.com/news/1829688/دومین-تساوی-فیروزجا-در-رقابت-های-کاندیداها"> <span class="news-type"></span>دومین تساوی فیروزجا در رقابت‌های کاندیداها</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="16"><a title="فرنگی‌کاران ایران از امروز در قرقیزستان به میدان می‌روند" href="https://www.varzesh3.com/news/1829687/فرنگی-کاران-ایران-از-امروز-در-قرقیزستان-به-میدان-می-روند"> <span class="news-type"></span>فرنگی‌کاران ایران از امروز در قرقیزستان به میدان می‌روند</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="16"><a title="ملی‌پوش کشتی فرنگی ایران در تیم نایب‌ قهرمان بوندس‌لیگا" href="https://www.varzesh3.com/news/1829686/ملی-پوش-کشتی-فرنگی-ایران-در-تیم-نایب-قهرمان-بوندس-لیگا"> <span class="news-type"></span>ملی‌پوش کشتی فرنگی ایران در تیم نایب‌ قهرمان بوندس‌لیگا</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="5"><a title="کار سخت نماینده هندبال ایران در آسیا" href="https://www.varzesh3.com/news/1829685/کار-سخت-نماینده-هندبال-ایران-در-آسیا"> <span class="news-type"></span>کار سخت نماینده هندبال ایران در آسیا</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="16"><a title="سرپرست هیأت کشتی استان تهران منصوب شد" href="https://www.varzesh3.com/news/1829684/سرپرست-هیأت-کشتی-استان-تهران-منصوب-شد"> <span class="news-type"></span>سرپرست هیأت کشتی استان تهران منصوب شد</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="5"><a title="تیم ملی هندبال دختران جوان ایران راهی اسلوونی شد" href="https://www.varzesh3.com/news/1829681/تیم-ملی-هندبال-دختران-جوان-ایران-راهی-اسلوونی-شد"> <span class="news-type"></span>تیم ملی هندبال دختران جوان ایران راهی اسلوونی شد</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="4"><a title="تیم بسکتبال نوجوانان ایران مقابل هند شکست خورد" href="https://www.varzesh3.com/news/1829680/تیم-بسکتبال-نوجوانان-ایران-مقابل-هند-شکست-خورد"> <span class="news-type"></span>تیم بسکتبال نوجوانان ایران مقابل هند شکست خورد</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="5"><a title="توقف هندبالیست‌های نوجوان ایران پشت سد فينال" href="https://www.varzesh3.com/news/1829677/توقف-هندبالیست-های-نوجوان-ایران-پشت-سد-فينال"> <span class="news-type"></span>توقف هندبالیست‌های نوجوان ایران پشت سد فينال</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="4"><a title="بسکتبال زیر 16 سال آسیا| ایران حریف هندنشد" href="https://www.varzesh3.com/news/1829653/بسکتبال-زیر-16-سال-آسیا-ایران-حریف-هندنشد"> <span class="news-type"></span>بسکتبال زیر 16 سال آسیا| ایران حریف هندنشد</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="3"><a title="این دو ستاره برگشتند؛ والیبال برزیل امیدوار شد " href="https://www.varzesh3.com/news/1829651/این-دو-ستاره-برگشتند-والیبال-برزیل-امیدوار-شد"> <span class="news-type"></span>این دو ستاره برگشتند؛ والیبال برزیل امیدوار شد </a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="صعود نوجوانان هندبال ساحلی به جمع 4 تیم برتر جهان" href="https://video.varzesh3.com/video/254063/صعود-نوجوانان-هندبال-ساحلی-به-جمع-4-تیم-برتر-جهان"> <span class="news-type"></span>صعود نوجوانان هندبال ساحلی به جمع 4 تیم برتر جهان</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="3"><a title="کرونا کابوس ایتالیا؛ بدنساز در نقش سرمربی!" href="https://www.varzesh3.com/news/1829620/کرونا-کابوس-ایتالیا-بدنساز-در-نقش-سرمربی"> <span class="news-type"></span>کرونا کابوس ایتالیا؛ بدنساز در نقش سرمربی!</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="5"><a title="صعود تاریخی نوجوانان هندبال به 4 تیم برتر جهان" href="https://www.varzesh3.com/news/1829614/صعود-تاریخی-نوجوانان-هندبال-به-4-تیم-برتر-جهان"> <span class="news-type"></span>صعود تاریخی نوجوانان هندبال به 4 تیم برتر جهان</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="3"><a title="اتفاق تلخ برای والیبال ایران؛ انصراف قهرمان از لیگ" href="https://www.varzesh3.com/news/1829612/اتفاق-تلخ-برای-والیبال-ایران-انصراف-قهرمان-از-لیگ"> <span class="news-type"></span>اتفاق تلخ برای والیبال ایران؛ انصراف قهرمان از لیگ</a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="محمدی: تا هفتاد درصد لیست یحیی را فراهم کردیم" href="https://video.varzesh3.com/video/254062/محمدی-تا-هفتاد-درصد-لیست-یحیی-را-فراهم-کردیم"> <span class="news-type"></span>محمدی: تا هفتاد درصد لیست یحیی را فراهم کردیم</a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="از حضور بانوان در ورزشگاه‌ها تا زمان شروع لیگ" href="https://video.varzesh3.com/video/254061/از-حضور-بانوان-در-ورزشگاه-ها-تا-زمان-شروع-لیگ"> <span class="news-type"></span>از حضور بانوان در ورزشگاه‌ها تا زمان شروع لیگ</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="37"><a title="نفرات برتر مسابقات موتورکراس و موتورریس مشخص شدند" href="https://www.varzesh3.com/news/1829591/نفرات-برتر-مسابقات-موتورکراس-و-موتورریس-مشخص-شدند"> <span class="news-type"></span>نفرات برتر مسابقات موتورکراس و موتورریس مشخص شدند</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="9"><a title="طلای رکابزن ایران در قهرمانی آسیا" href="https://www.varzesh3.com/news/1829585/طلای-رکابزن-ایران-در-قهرمانی-آسیا"> <span class="news-type"></span>طلای رکابزن ایران در قهرمانی آسیا</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="25"><a title="مشخص شدن نفرات برتر راند دوم کارتینگ قهرمانی کشور" href="https://www.varzesh3.com/news/1829584/مشخص-شدن-نفرات-برتر-راند-دوم-کارتینگ-قهرمانی-کشور"> <span class="news-type"></span>مشخص شدن نفرات برتر راند دوم کارتینگ قهرمانی کشور</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="38"><a title="امضاء تفاهم نامه فدراسیون ورزش‌های همگانی با چند کشور" href="https://www.varzesh3.com/news/1829582/امضا-تفاهم-نامه-فدراسیون-ورزش-های-همگانی-با-چند-کشور"> <span class="news-type"></span>امضاء تفاهم نامه فدراسیون ورزش‌های همگانی با چند کشور</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="13"><a title="پایان جدال جودوکاران ایران، روسیه و صربستان" href="https://www.varzesh3.com/news/1829579/پایان-جدال-جودوکاران-ایران-روسیه-و-صربستان"> <span class="news-type"></span>پایان جدال جودوکاران ایران، روسیه و صربستان</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="3"><a title="رسمی؛ بمب نقل و انتقالات لیگ والیبال منفجر شد" href="https://www.varzesh3.com/news/1829578/رسمی-بمب-نقل-و-انتقالات-لیگ-والیبال-منفجر-شد"> <span class="news-type"></span>رسمی؛ بمب نقل و انتقالات لیگ والیبال منفجر شد</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="6"><a title="تیم دو نفره کامپوند کشورمان فردا راهی فرانسه می‌شود" href="https://www.varzesh3.com/news/1829573/تیم-دو-نفره-کامپوند-کشورمان-فردا-راهی-فرانسه-می-شود"> <span class="news-type"></span>تیم دو نفره کامپوند کشورمان فردا راهی فرانسه می‌شود</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="22"><a title="شکسته شدن ۴ رکورد ملی توسط شناگران نابینا و کم بینا" href="https://www.varzesh3.com/news/1829572/شکسته-شدن-۴-رکورد-ملی-توسط-شناگران-نابینا-و-کم-بینا"> <span class="news-type"></span>شکسته شدن ۴ رکورد ملی توسط شناگران نابینا و کم بینا</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="12"><a title="امروز، آغاز مسابقات انتخابی ورود به اردوی تیم ملی بوکس" href="https://www.varzesh3.com/news/1829570/امروز-آغاز-مسابقات-انتخابی-ورود-به-اردوی-تیم-ملی-بوکس"> <span class="news-type"></span>امروز، آغاز مسابقات انتخابی ورود به اردوی تیم ملی بوکس</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="4"><a title="رکورد خاص گلدن استیت در فینال NBA" href="https://www.varzesh3.com/news/1829569/رکورد-خاص-گلدن-استیت-در-فینال-nba"> <span class="news-type"></span>رکورد خاص گلدن استیت در فینال NBA</a></li>
                </ul>
            </div>
        </div>
    </div>
</div>

            </div>
        </div>
        



        <div class="widget-holder">
            <div class="widget league schedual volleyball" id="81">
                            <div class="widget-header">
    <h2>لیگ والیبال ملت‌ها</h2>
    <div class="select-options">
        <select id="stage">
                    <option value="901985" selected="selected" data-api="https://volleyball-api.varzesh3.com/v1.0/widgets/81/league/901985">
                        مرحله مقدماتی
                    </option>
        </select>
        <select id="round">
                    <option value="1">هفته 1</option>
                    <option value="2" selected="selected">هفته 2</option>
                    <option value="3">هفته 3</option>
        </select>
    </div>
</div>
<div class="widget-body">
    <div class="widget-volleyball">
        <div class="widget-subtitle" style="background-color:#a57300"><h3>مرحله مقدماتی</h3></div>
        <div class="table-holder setnum-box ">
            <table class="setnum">
                <tbody>
                    <tr>
                        <td></td>
                        <td></td>
                        <td>1st</td>
                        <td>2nd</td>
                        <td>3rd</td>
                        <td>4th</td>
                        <td>5th</td>
                        <td></td>
                        <td></td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
    <div class="scrollable-box" style="max-height:330px">
        <div class="scroll-list-content">
            <div class="widget-volleyball">
                        <div class="date-seprator"><h4>سه شنبه 31 خرداد</h4></div>
                        <div class="table-holder ">
                            <table class="game-table">
                                <tbody>
                                        <tr class="even">
                                            <td>
                                                <div class="info">
                                                    
                                                    <a href="/volleyball/match/104294/اسلوونی-هلند"><img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                                </div>
                                            </td>
                                            <td>اسلوونی<br />هلند</td>
                                            <td>17<br />25</td>
                                            <td>21<br />25</td>
                                            <td>24<br />26</td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td class="result">0<br />3</td>
                                            <td> 
                                                <a target="_blank" href="https://video.varzesh3.com/video/254193/"><img src="https://static.varzesh3.com/img/icons/video-link.svg" /></a>
                                                <span></span>
                                                <span class="match-status"></span>
                                            </td>
                                        </tr>
                                        <tr class="odd">
                                            <td>
                                                <div class="info">
                                                    
                                                    <a href="/volleyball/match/104295/آرژانتین-ژاپن"><img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                                </div>
                                            </td>
                                            <td>آرژانتین<br />ژاپن</td>
                                            <td>25<br />27</td>
                                            <td>18<br />25</td>
                                            <td>25<br />17</td>
                                            <td>16<br />25</td>
                                            <td><br /></td>
                                            <td class="result">1<br />3</td>
                                            <td> 
                                                <a target="_blank" href="https://video.varzesh3.com/video/254205/"><img src="https://static.varzesh3.com/img/icons/video-link.svg" /></a>
                                                <span></span>
                                                <span class="match-status"></span>
                                            </td>
                                        </tr>
                                        <tr class="even">
                                            <td>
                                                <div class="info">
                                                    
                                                    <a href="/volleyball/match/104296/استرالیا-کانادا"><img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                                </div>
                                            </td>
                                            <td>استرالیا<br />کانادا</td>
                                            <td>25<br />18</td>
                                            <td>26<br />28</td>
                                            <td>19<br />25</td>
                                            <td>22<br />25</td>
                                            <td><br /></td>
                                            <td class="result">1<br />3</td>
                                            <td> 
                                                <a target="_blank" href="https://video.varzesh3.com/video/254217/"><img src="https://static.varzesh3.com/img/icons/video-link.svg" /></a>
                                                <span></span>
                                                <span class="match-status"></span>
                                            </td>
                                        </tr>
                                        <tr class="odd">
                                            <td>
                                                <div class="info">
                                                    
                                                    <a href="/volleyball/match/104297/ایران-بلغارستان"><img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                                </div>
                                            </td>
                                            <td>ایران<br />بلغارستان</td>
                                            <td>19<br />25</td>
                                            <td>23<br />25</td>
                                            <td>24<br />26</td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td class="result">0<br />3</td>
                                            <td> 
                                                <a target="_blank" href="https://video.varzesh3.com/video/254218/"><img src="https://static.varzesh3.com/img/icons/video-link.svg" /></a>
                                                <span></span>
                                                <span class="match-status"></span>
                                            </td>
                                        </tr>
                                </tbody>
                            </table>
                        </div>
                        <div class="date-seprator"><h4>چهارشنبه 1 تیر</h4></div>
                        <div class="table-holder ">
                            <table class="game-table">
                                <tbody>
                                        <tr class="even">
                                            <td>
                                                <div class="info">
                                                    
                                                    <a href="/volleyball/match/104298/چین-فرانسه"><img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                                </div>
                                            </td>
                                            <td>چین<br />فرانسه</td>
                                            <td>0<br />25</td>
                                            <td>0<br />25</td>
                                            <td>0<br />25</td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td class="result">0<br />3</td>
                                            <td> 
                                                
                                                <span></span>
                                                <span class="match-status"></span>
                                            </td>
                                        </tr>
                                        <tr class="odd">
                                            <td>
                                                <div class="info">
                                                    
                                                    <a href="/volleyball/match/104299/آلمان-ایتالیا"><img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                                </div>
                                            </td>
                                            <td>آلمان<br />ایتالیا</td>
                                            <td>16<br />25</td>
                                            <td>21<br />25</td>
                                            <td>22<br />25</td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td class="result">0<br />3</td>
                                            <td> 
                                                <a target="_blank" href="https://video.varzesh3.com/video/254245/"><img src="https://static.varzesh3.com/img/icons/video-link.svg" /></a>
                                                <span></span>
                                                <span class="match-status"></span>
                                            </td>
                                        </tr>
                                        <tr class="even">
                                            <td>
                                                <div class="info">
                                                    
                                                    <a href="/volleyball/match/104300/برزیل-لهستان"><img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                                </div>
                                            </td>
                                            <td>برزیل<br />لهستان</td>
                                            <td>16<br />25</td>
                                            <td>25<br />22</td>
                                            <td>16<br />25</td>
                                            <td>22<br />25</td>
                                            <td><br /></td>
                                            <td class="result">1<br />3</td>
                                            <td> 
                                                <a target="_blank" href="https://video.varzesh3.com/video/254260/"><img src="https://static.varzesh3.com/img/icons/video-link.svg" /></a>
                                                <span></span>
                                                <span class="match-status"></span>
                                            </td>
                                        </tr>
                                        <tr class="odd">
                                            <td>
                                                <div class="info">
                                                    
                                                    <a href="/volleyball/match/104301/صربستان-آمریکا"><img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                                </div>
                                            </td>
                                            <td>صربستان<br />آمریکا</td>
                                            <td>24<br />26</td>
                                            <td>25<br />23</td>
                                            <td>23<br />25</td>
                                            <td>20<br />25</td>
                                            <td><br /></td>
                                            <td class="result">1<br />3</td>
                                            <td> 
                                                <a target="_blank" href="https://video.varzesh3.com/video/254265/"><img src="https://static.varzesh3.com/img/icons/video-link.svg" /></a>
                                                <span></span>
                                                <span class="match-status"></span>
                                            </td>
                                        </tr>
                                </tbody>
                            </table>
                        </div>
                        <div class="date-seprator"><h4>پنج شنبه 2 تیر</h4></div>
                        <div class="table-holder ">
                            <table class="game-table">
                                <tbody>
                                        <tr class="even">
                                            <td>
                                                <div class="info">
                                                    
                                                    <a href="/volleyball/match/104302/فرانسه-هلند"><img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                                </div>
                                            </td>
                                            <td>فرانسه<br />هلند</td>
                                            <td>25<br />14</td>
                                            <td>25<br />23</td>
                                            <td>25<br />13</td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td class="result">3<br />0</td>
                                            <td> 
                                                <a target="_blank" href="https://video.varzesh3.com/video/254276/"><img src="https://static.varzesh3.com/img/icons/video-link.svg" /></a>
                                                <span></span>
                                                <span class="match-status"></span>
                                            </td>
                                        </tr>
                                        <tr class="odd">
                                            <td>
                                                <div class="info">
                                                    
                                                    <a href="/volleyball/match/104303/چین-آلمان"><img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                                </div>
                                            </td>
                                            <td>چین<br />آلمان</td>
                                            <td>25<br />0</td>
                                            <td>25<br />0</td>
                                            <td>25<br />0</td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td class="result">3<br />0</td>
                                            <td> 
                                                
                                                <span></span>
                                                <span class="match-status"></span>
                                            </td>
                                        </tr>
                                        <tr class="even">
                                            <td>
                                                <div class="info">
                                                    <a target="_blank" href="https://www.anten.ir/program/45223/%D9%88%D8%A7%D9%84%DB%8C%D8%A8%D8%A7%D9%84-%D9%84%D9%87%D8%B3%D8%AA%D8%A7%D9%86-%DA%A9%D8%A7%D9%86%D8%A7%D8%AF%D8%A7"><img src="https://static.varzesh3.com/img/icons/anten-icon.svg" /></a>
                                                    <a href="/volleyball/match/104304/لهستان-کانادا"><img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                                </div>
                                            </td>
                                            <td>لهستان<br />کانادا</td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td class="result"> <br /> </td>
                                            <td> 
                                                
                                                <span>15:00</span>
                                                <span class="match-status"></span>
                                            </td>
                                        </tr>
                                        <tr class="odd">
                                            <td>
                                                <div class="info">
                                                    <a target="_blank" href="https://www.anten.ir/program/45224/%D9%88%D8%A7%D9%84%DB%8C%D8%A8%D8%A7%D9%84-%D8%A2%D8%B1%DA%98%D8%A7%D9%86%D8%AA%DB%8C%D9%86-%D8%A7%D8%B3%D9%84%D9%88%D9%88%D9%86%DB%8C"><img src="https://static.varzesh3.com/img/icons/anten-icon.svg" /></a>
                                                    <a href="/volleyball/match/104305/آرژانتین-اسلوونی"><img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                                </div>
                                            </td>
                                            <td>آرژانتین<br />اسلوونی</td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td class="result"> <br /> </td>
                                            <td> 
                                                
                                                <span>15:30</span>
                                                <span class="match-status"></span>
                                            </td>
                                        </tr>
                                        <tr class="even">
                                            <td>
                                                <div class="info">
                                                    <a target="_blank" href="https://www.anten.ir/program/45225/%D9%88%D8%A7%D9%84%DB%8C%D8%A8%D8%A7%D9%84-%D8%B5%D8%B1%D8%A8%D8%B3%D8%AA%D8%A7%D9%86-%D8%A8%D8%B1%D8%B2%DB%8C%D9%84"><img src="https://static.varzesh3.com/img/icons/anten-icon.svg" /></a>
                                                    <a href="/volleyball/match/104306/صربستان-برزیل"><img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                                </div>
                                            </td>
                                            <td>صربستان<br />برزیل</td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td class="result"> <br /> </td>
                                            <td> 
                                                
                                                <span>18:00</span>
                                                <span class="match-status"></span>
                                            </td>
                                        </tr>
                                        <tr class="odd">
                                            <td>
                                                <div class="info">
                                                    <a target="_blank" href="https://www.anten.ir/program/45226/%D9%88%D8%A7%D9%84%DB%8C%D8%A8%D8%A7%D9%84-%D8%A2%D9%85%D8%B1%DB%8C%DA%A9%D8%A7-%D8%A7%DB%8C%D8%B1%D8%A7%D9%86"><img src="https://static.varzesh3.com/img/icons/anten-icon.svg" /></a>
                                                    <a href="/volleyball/match/104307/آمریکا-ایران"><img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                                </div>
                                            </td>
                                            <td>آمریکا<br />ایران</td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td class="result"> <br /> </td>
                                            <td> 
                                                
                                                <span>21:30</span>
                                                <span class="match-status"></span>
                                            </td>
                                        </tr>
                                </tbody>
                            </table>
                        </div>
                        <div class="date-seprator"><h4>جمعه 3 تیر</h4></div>
                        <div class="table-holder ">
                            <table class="game-table">
                                <tbody>
                                        <tr class="even">
                                            <td>
                                                <div class="info">
                                                    <a target="_blank" href="https://www.anten.ir/program/45227/%D9%88%D8%A7%D9%84%DB%8C%D8%A8%D8%A7%D9%84-%D8%A2%D9%84%D9%85%D8%A7%D9%86-%D9%87%D9%84%D9%86%D8%AF"><img src="https://static.varzesh3.com/img/icons/anten-icon.svg" /></a>
                                                    <a href="/volleyball/match/104308/آلمان-هلند"><img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                                </div>
                                            </td>
                                            <td>آلمان<br />هلند</td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td class="result"> <br /> </td>
                                            <td> 
                                                
                                                <span>07:30</span>
                                                <span class="match-status"></span>
                                            </td>
                                        </tr>
                                        <tr class="odd">
                                            <td>
                                                <div class="info">
                                                    <a target="_blank" href="https://www.anten.ir/program/45228/%D9%88%D8%A7%D9%84%DB%8C%D8%A8%D8%A7%D9%84-%D8%A2%D8%B1%DA%98%D8%A7%D9%86%D8%AA%DB%8C%D9%86-%DA%86%DB%8C%D9%86"><img src="https://static.varzesh3.com/img/icons/anten-icon.svg" /></a>
                                                    <a href="/volleyball/match/104309/آرژانتین-چین"><img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                                </div>
                                            </td>
                                            <td>آرژانتین<br />چین</td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td class="result"> <br /> </td>
                                            <td> 
                                                
                                                <span>11:30</span>
                                                <span class="match-status"></span>
                                            </td>
                                        </tr>
                                        <tr class="even">
                                            <td>
                                                <div class="info">
                                                    <a target="_blank" href="https://www.anten.ir/program/45229/%D9%88%D8%A7%D9%84%DB%8C%D8%A8%D8%A7%D9%84-%D8%B5%D8%B1%D8%A8%D8%B3%D8%AA%D8%A7%D9%86-%DA%A9%D8%A7%D9%86%D8%A7%D8%AF%D8%A7"><img src="https://static.varzesh3.com/img/icons/anten-icon.svg" /></a>
                                                    <a href="/volleyball/match/104310/صربستان-کانادا"><img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                                </div>
                                            </td>
                                            <td>صربستان<br />کانادا</td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td class="result"> <br /> </td>
                                            <td> 
                                                
                                                <span>15:00</span>
                                                <span class="match-status"></span>
                                            </td>
                                        </tr>
                                        <tr class="odd">
                                            <td>
                                                <div class="info">
                                                    <a target="_blank" href="https://www.anten.ir/program/45231/%D9%88%D8%A7%D9%84%DB%8C%D8%A8%D8%A7%D9%84-%DA%98%D8%A7%D9%BE%D9%86-%D8%A7%DB%8C%D8%AA%D8%A7%D9%84%DB%8C%D8%A7"><img src="https://static.varzesh3.com/img/icons/anten-icon.svg" /></a>
                                                    <a href="/volleyball/match/104311/ژاپن-ایتالیا"><img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                                </div>
                                            </td>
                                            <td>ژاپن<br />ایتالیا</td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td class="result"> <br /> </td>
                                            <td> 
                                                
                                                <span>15:30</span>
                                                <span class="match-status"></span>
                                            </td>
                                        </tr>
                                        <tr class="even">
                                            <td>
                                                <div class="info">
                                                    <a target="_blank" href="https://www.anten.ir/program/45232/%D9%88%D8%A7%D9%84%DB%8C%D8%A8%D8%A7%D9%84-%D8%A7%DB%8C%D8%B1%D8%A7%D9%86-%D8%A8%D8%B1%D8%B2%DB%8C%D9%84"><img src="https://static.varzesh3.com/img/icons/anten-icon.svg" /></a>
                                                    <a href="/volleyball/match/104312/ایران-برزیل"><img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                                </div>
                                            </td>
                                            <td>ایران<br />برزیل</td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td class="result"> <br /> </td>
                                            <td> 
                                                
                                                <span>18:00</span>
                                                <span class="match-status"></span>
                                            </td>
                                        </tr>
                                        <tr class="odd">
                                            <td>
                                                <div class="info">
                                                    <a target="_blank" href="https://www.anten.ir/program/45233/%D9%88%D8%A7%D9%84%DB%8C%D8%A8%D8%A7%D9%84-%D8%A7%D8%B3%D8%AA%D8%B1%D8%A7%D9%84%DB%8C%D8%A7-%D8%A8%D9%84%D8%BA%D8%A7%D8%B1%D8%B3%D8%AA%D8%A7%D9%86"><img src="https://static.varzesh3.com/img/icons/anten-icon.svg" /></a>
                                                    <a href="/volleyball/match/104313/استرالیا-بلغارستان"><img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                                </div>
                                            </td>
                                            <td>استرالیا<br />بلغارستان</td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td class="result"> <br /> </td>
                                            <td> 
                                                
                                                <span>21:30</span>
                                                <span class="match-status"></span>
                                            </td>
                                        </tr>
                                </tbody>
                            </table>
                        </div>
                        <div class="date-seprator"><h4>شنبه 4 تیر</h4></div>
                        <div class="table-holder ">
                            <table class="game-table">
                                <tbody>
                                        <tr class="even">
                                            <td>
                                                <div class="info">
                                                    
                                                    <a href="/volleyball/match/104314/آرژانتین-هلند"><img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                                </div>
                                            </td>
                                            <td>آرژانتین<br />هلند</td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td class="result"> <br /> </td>
                                            <td> 
                                                
                                                <span>07:30</span>
                                                <span class="match-status"></span>
                                            </td>
                                        </tr>
                                        <tr class="odd">
                                            <td>
                                                <div class="info">
                                                    
                                                    <a href="/volleyball/match/104315/ژاپن-فرانسه"><img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                                </div>
                                            </td>
                                            <td>ژاپن<br />فرانسه</td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td class="result"> <br /> </td>
                                            <td> 
                                                
                                                <span>11:30</span>
                                                <span class="match-status"></span>
                                            </td>
                                        </tr>
                                        <tr class="even">
                                            <td>
                                                <div class="info">
                                                    
                                                    <a href="/volleyball/match/104316/کانادا-ایران"><img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                                </div>
                                            </td>
                                            <td>کانادا<br />ایران</td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td class="result"> <br /> </td>
                                            <td> 
                                                
                                                <span>15:00</span>
                                                <span class="match-status"></span>
                                            </td>
                                        </tr>
                                        <tr class="odd">
                                            <td>
                                                <div class="info">
                                                    
                                                    <a href="/volleyball/match/104317/ایتالیا-اسلوونی"><img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                                </div>
                                            </td>
                                            <td>ایتالیا<br />اسلوونی</td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td class="result"> <br /> </td>
                                            <td> 
                                                
                                                <span>15:30</span>
                                                <span class="match-status"></span>
                                            </td>
                                        </tr>
                                        <tr class="even">
                                            <td>
                                                <div class="info">
                                                    
                                                    <a href="/volleyball/match/104318/لهستان-استرالیا"><img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                                </div>
                                            </td>
                                            <td>لهستان<br />استرالیا</td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td class="result"> <br /> </td>
                                            <td> 
                                                
                                                <span>18:00</span>
                                                <span class="match-status"></span>
                                            </td>
                                        </tr>
                                        <tr class="odd">
                                            <td>
                                                <div class="info">
                                                    
                                                    <a href="/volleyball/match/104319/آمریکا-بلغارستان"><img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                                </div>
                                            </td>
                                            <td>آمریکا<br />بلغارستان</td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td class="result"> <br /> </td>
                                            <td> 
                                                
                                                <span>21:30</span>
                                                <span class="match-status"></span>
                                            </td>
                                        </tr>
                                </tbody>
                            </table>
                        </div>
                        <div class="date-seprator"><h4>یکشنبه 5 تیر</h4></div>
                        <div class="table-holder ">
                            <table class="game-table">
                                <tbody>
                                        <tr class="even">
                                            <td>
                                                <div class="info">
                                                    
                                                    <a href="/volleyball/match/104320/آلمان-فرانسه"><img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                                </div>
                                            </td>
                                            <td>آلمان<br />فرانسه</td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td class="result"> <br /> </td>
                                            <td> 
                                                
                                                <span>07:30</span>
                                                <span class="match-status"></span>
                                            </td>
                                        </tr>
                                        <tr class="odd">
                                            <td>
                                                <div class="info">
                                                    
                                                    <a href="/volleyball/match/104321/ژاپن-اسلوونی"><img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                                </div>
                                            </td>
                                            <td>ژاپن<br />اسلوونی</td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td class="result"> <br /> </td>
                                            <td> 
                                                
                                                <span>11:30</span>
                                                <span class="match-status"></span>
                                            </td>
                                        </tr>
                                        <tr class="even">
                                            <td>
                                                <div class="info">
                                                    
                                                    <a href="/volleyball/match/104322/صربستان-استرالیا"><img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                                </div>
                                            </td>
                                            <td>صربستان<br />استرالیا</td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td class="result"> <br /> </td>
                                            <td> 
                                                
                                                <span>15:00</span>
                                                <span class="match-status"></span>
                                            </td>
                                        </tr>
                                        <tr class="odd">
                                            <td>
                                                <div class="info">
                                                    
                                                    <a href="/volleyball/match/104323/ایتالیا-چین"><img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                                </div>
                                            </td>
                                            <td>ایتالیا<br />چین</td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td class="result"> <br /> </td>
                                            <td> 
                                                
                                                <span>15:30</span>
                                                <span class="match-status"></span>
                                            </td>
                                        </tr>
                                        <tr class="even">
                                            <td>
                                                <div class="info">
                                                    
                                                    <a href="/volleyball/match/104324/آمریکا-لهستان"><img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                                </div>
                                            </td>
                                            <td>آمریکا<br />لهستان</td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td class="result"> <br /> </td>
                                            <td> 
                                                
                                                <span>18:00</span>
                                                <span class="match-status"></span>
                                            </td>
                                        </tr>
                                        <tr class="odd">
                                            <td>
                                                <div class="info">
                                                    
                                                    <a href="/volleyball/match/104325/بلغارستان-برزیل"><img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                                </div>
                                            </td>
                                            <td>بلغارستان<br />برزیل</td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td><br /></td>
                                            <td class="result"> <br /> </td>
                                            <td> 
                                                
                                                <span>21:30</span>
                                                <span class="match-status"></span>
                                            </td>
                                        </tr>
                                </tbody>
                            </table>
                        </div>
            </div>
        </div>
    </div>
    <div class="widget-table">
        <div class="widget-subtitle" style="background-color:#a57300"><h3>جدول مرحله مقدماتی</h3></div>
        <div class="table-holder">
            <table class=" league-standing widget-standing">
                <thead>
                    <tr>
                        <th scope="col">رتبه</th>
                        <th scope="col">تيم</th>
                        <th scope="col">بازی</th>
                        <th scope="col">برد</th>
                    </tr>
                </thead>
                <tbody>
                            <tr>
                                <td scope="row">1</td>
                                <td>فرانسه</td>
                                <td>6</td>
                                <td>5</td>
                            </tr>
                            <tr>
                                <td scope="row">2</td>
                                <td>آمریکا</td>
                                <td>5</td>
                                <td>5</td>
                            </tr>
                            <tr>
                                <td scope="row">3</td>
                                <td>ژاپن</td>
                                <td>5</td>
                                <td>4</td>
                            </tr>
                            <tr>
                                <td scope="row">4</td>
                                <td>لهستان</td>
                                <td>5</td>
                                <td>4</td>
                            </tr>
                            <tr>
                                <td scope="row">5</td>
                                <td>ایتالیا</td>
                                <td>5</td>
                                <td>4</td>
                            </tr>
                            <tr>
                                <td scope="row">6</td>
                                <td>هلند</td>
                                <td>6</td>
                                <td>3</td>
                            </tr>
                            <tr>
                                <td scope="row">7</td>
                                <td>آلمان</td>
                                <td>6</td>
                                <td>3</td>
                            </tr>
                            <tr>
                                <td scope="row">8</td>
                                <td>اسلوونی</td>
                                <td>5</td>
                                <td>2</td>
                            </tr>
                            <tr>
                                <td scope="row">9</td>
                                <td>صربستان</td>
                                <td>5</td>
                                <td>2</td>
                            </tr>
                            <tr>
                                <td scope="row">10</td>
                                <td>چین</td>
                                <td>6</td>
                                <td>2</td>
                            </tr>
                            <tr>
                                <td scope="row">11</td>
                                <td>برزیل</td>
                                <td>5</td>
                                <td>2</td>
                            </tr>
                            <tr>
                                <td scope="row">12</td>
                                <td>ایران</td>
                                <td>5</td>
                                <td>2</td>
                            </tr>
                            <tr>
                                <td scope="row">13</td>
                                <td>کانادا</td>
                                <td>5</td>
                                <td>2</td>
                            </tr>
                            <tr>
                                <td scope="row">14</td>
                                <td>بلغارستان</td>
                                <td>5</td>
                                <td>1</td>
                            </tr>
                            <tr>
                                <td scope="row">15</td>
                                <td>آرژانتین</td>
                                <td>5</td>
                                <td>1</td>
                            </tr>
                            <tr>
                                <td scope="row">16</td>
                                <td>استرالیا</td>
                                <td>5</td>
                                <td>0</td>
                            </tr>
                </tbody>
            </table>
        </div>
    </div>
</div>
<div class="widget-footer"><a></a></div>
            </div>
        </div>
        



        

        

<div class="adbox" data-id="143">
            <div class="native-holder">
                <div id="pos-article-display-4200"></div>
            </div>
</div>


        <div class="widget-holder">
            <div class="widget broadcast" id="67">
                            

<div class="widget-header">
    <h2>جدول پخش زنده مسابقات ورزشی</h2>
</div>
<div class="widget-body">
            <div class="date-seprator"><h4>پنج شنبه 2 تیر</h4></div>
                <div class="broadcast-match even">
                    <div class="broadcast-match-bottom-row"  >
                        <div class="broadcast-match-time">11:30</div>
                        
                        <div class="broadcast-match-teams">
                            <div class="broadcast-match-host">چین</div>
                            <div class="broadcast-match-sep"><span> - </span></div>
                            <div class="broadcast-match-guest"> آلمان</div>
                            <div class="broadcast-info">لیگ والیبال ملت‌ها</div>
                        </div>
                        <div class="broadcast-tvs">
                            <span> شبکه ورزش</span>
                            <span><a class="anten-text" target="_blank"  href="https://www.anten.ir/program/45222/%D9%88%D8%A7%D9%84%DB%8C%D8%A8%D8%A7%D9%84-%DA%86%DB%8C%D9%86-%D8%A2%D9%84%D9%85%D8%A7%D9%86"> آنتن</a></span>
                        </div>
                    </div>
                </div>
                <div class="broadcast-match odd">
                    <div class="broadcast-match-bottom-row"  >
                        <div class="broadcast-match-time">18:00</div>
                        
                        <div class="broadcast-match-teams">
                            <div class="broadcast-match-host">صربستان</div>
                            <div class="broadcast-match-sep"><span> - </span></div>
                            <div class="broadcast-match-guest"> برزیل</div>
                            <div class="broadcast-info">لیگ والیبال ملت‌ها</div>
                        </div>
                        <div class="broadcast-tvs">
                            <span> شبکه ورزش</span>
                            <span><a class="anten-text" target="_blank"  href="https://www.anten.ir/program/45225/%D9%88%D8%A7%D9%84%DB%8C%D8%A8%D8%A7%D9%84-%D8%B5%D8%B1%D8%A8%D8%B3%D8%AA%D8%A7%D9%86-%D8%A8%D8%B1%D8%B2%DB%8C%D9%84"> آنتن</a></span>
                        </div>
                    </div>
                </div>
                <div class="broadcast-match even">
                    <div class="broadcast-match-bottom-row"  >
                        <div class="broadcast-match-time">21:30</div>
                        
                        <div class="broadcast-match-teams">
                            <div class="broadcast-match-host">آمریکا</div>
                            <div class="broadcast-match-sep"><span> - </span></div>
                            <div class="broadcast-match-guest"> ایران</div>
                            <div class="broadcast-info">لیگ والیبال ملت‌ها</div>
                        </div>
                        <div class="broadcast-tvs">
                            <span> شبکه سه</span>
                            <span><a class="anten-text" target="_blank"  href="https://www.anten.ir/program/45226/%D9%88%D8%A7%D9%84%DB%8C%D8%A8%D8%A7%D9%84-%D8%A2%D9%85%D8%B1%DB%8C%DA%A9%D8%A7-%D8%A7%DB%8C%D8%B1%D8%A7%D9%86"> آنتن</a></span>
                        </div>
                    </div>
                </div>
            <div class="date-seprator"><h4>جمعه 3 تیر</h4></div>
                <div class="broadcast-match even">
                    <div class="broadcast-match-bottom-row"  >
                        <div class="broadcast-match-time">18:00</div>
                        
                        <div class="broadcast-match-teams">
                            <div class="broadcast-match-host">ایران</div>
                            <div class="broadcast-match-sep"><span> - </span></div>
                            <div class="broadcast-match-guest"> برزیل</div>
                            <div class="broadcast-info">لیگ والیبال ملت‌ها</div>
                        </div>
                        <div class="broadcast-tvs">
                            <span> شبکه سه</span>
                            <span><a class="anten-text" target="_blank"  href="https://www.anten.ir/program/45232/%D9%88%D8%A7%D9%84%DB%8C%D8%A8%D8%A7%D9%84-%D8%A7%DB%8C%D8%B1%D8%A7%D9%86-%D8%A8%D8%B1%D8%B2%DB%8C%D9%84"> آنتن</a></span>
                        </div>
                    </div>
                </div>
    
</div>
            </div>
        </div>
        

        

<div class="adbox" data-id="313">
            <a  style="display:none;" class="adlink vrz-lazy" target="_blank" href="https://biz.varzesh3.com/events/click/313">
                <img class="adimage" id="img-313" src="https://static.varzeshe3.com/img/blank.png" data-origin="https://biz-cdn.varzesh3.com/banners/2022/05/29/1b8c193e-0d92-4752-966b-566f3e16c40a.gif" width="300" />
            </a>
</div>



                </div>
                <div class="v50-l-col">
                    

        

        

<div class="adbox" data-id="331">
            <a  style="display:none;" class="adlink vrz-lazy" target="_blank" href="https://biz.varzesh3.com/events/click/331">
                <img class="adimage" id="img-331" src="https://static.varzeshe3.com/img/blank.png" data-origin="https://biz-cdn.varzesh3.com/banners/2022/06/21/fd805b30-8e0b-4160-b4d6-1ea6b1cc11c8.gif" width="300" />
            </a>
</div>


        <div class="widget-holder">
            <div class="widget video" id="68">
                            
<div class="widget-header"><h2>ویدیو</h2></div>
<div class="widget-body">
    <ul class="nav nav-tabs vrz-tab" id="myTab" role="tablist">
        <li class="nav-item"><a class="nav-link active" id="new-tab" data-toggle="tab" href="#new" role="tab" aria-controls="new" aria-selected="true">جدیدترین</a></li>
        <li class="nav-item"><a class="nav-link" id="featured-tab" data-toggle="tab" href="#featured" role="tab" aria-controls="featured" aria-selected="false">ویژه</a></li>
    </ul>
    <div class="tab-content" id="myTabContent">
        <div class="tab-pane fade show active" id="new" role="tabpanel" aria-labelledby="new-tab">
            <div class="video-carousel-holder">
                <div class="video-carousel owl-carousel">
                            <div class="video-carousel-item"><div class="videobox"> 
<a class="video-cover-box" target="_blank" href="https://video.varzesh3.com/video/254281/صحبت-های-عطایی-قبل-از-بازی-با-آمریکا">
    <div class="video-cover-image">
            <img alt="صحبت های عطایی قبل از بازی با آمریکا" width="300" height="155" src="https://video-images1.varzeshe3.com/covers/2022/06/23/C/1db54cby.jpg?w=300" />
    </div>
    <div class="timebox">
        <span class="playicon">
            <img alt="پخش ویدیو" width="10" height="10" src="https://static.varzesh3.com/img/icons/smallplay-icon.svg?w=10" />
        </span>

        <span class="duration">02:22</span>
    </div>
</a>
<div class="video-data">
    <span class="date"> 5 دقیقه پیش - </span>
    <span class="view">76 بازدید</span>
</div>
<a class="title" target="_blank" href="https://video.varzesh3.com/video/254281/صحبت-های-عطایی-قبل-از-بازی-با-آمریکا">
    <h4>صحبت های عطایی قبل از بازی با آمریکا</h4>
</a>
</div></div>
                            <div class="video-carousel-item"><div class="videobox"> 
<a class="video-cover-box" target="_blank" href="https://video.varzesh3.com/video/254280/عنایتی-هیچوقت-برای-حضور-در-استقلال-شرطی-نگذاشتم">
    <div class="video-cover-image">
            <img alt="عنایتی: هیچوقت برای حضور در استقلال شرطی نگذاشتم" width="300" height="155" src="https://video-images1.varzeshe3.com/covers/2022/06/23/B/z1lwsoay.jpg?w=300" />
    </div>
    <div class="timebox">
        <span class="playicon">
            <img alt="پخش ویدیو" width="10" height="10" src="https://static.varzesh3.com/img/icons/smallplay-icon.svg?w=10" />
        </span>

        <span class="duration">08:41</span>
    </div>
</a>
<div class="video-data">
    <span class="date"> 18 دقیقه پیش - </span>
    <span class="view">458 بازدید</span>
</div>
<a class="title" target="_blank" href="https://video.varzesh3.com/video/254280/عنایتی-هیچوقت-برای-حضور-در-استقلال-شرطی-نگذاشتم">
    <h4>عنایتی: هیچوقت برای حضور در استقلال شرطی نگذاشتم</h4>
</a>
</div></div>
                            <div class="video-carousel-item"><div class="videobox"> 
<a class="video-cover-box" target="_blank" href="https://video.varzesh3.com/video/254279/پول-نخواستیم-تنها-ذره-ای-احترام-برای-داوران-قائل-باشیم">
    <div class="video-cover-image">
            <img alt="پول نخواستیم، تنها ذره ای احترام برای داوران قائل باشیم" width="300" height="155" src="https://video-images1.varzeshe3.com/covers/2022/06/23/B/vrsgppcp.jpg?w=300" />
    </div>
    <div class="timebox">
        <span class="playicon">
            <img alt="پخش ویدیو" width="10" height="10" src="https://static.varzesh3.com/img/icons/smallplay-icon.svg?w=10" />
        </span>

        <span class="duration">04:28</span>
    </div>
</a>
<div class="video-data">
    <span class="date"> 22 دقیقه پیش - </span>
    <span class="view">192 بازدید</span>
</div>
<a class="title" target="_blank" href="https://video.varzesh3.com/video/254279/پول-نخواستیم-تنها-ذره-ای-احترام-برای-داوران-قائل-باشیم">
    <h4>پول نخواستیم، تنها ذره ای احترام برای داوران قائل باشیم</h4>
</a>
</div></div>
                            <div class="video-carousel-item"><div class="videobox"> 
<a class="video-cover-box" target="_blank" href="https://video.varzesh3.com/video/254278/واکنش-جواد-خیابانی-به-وایرال-شدن-ویدئوهایش">
    <div class="video-cover-image">
            <img alt="واکنش جواد خیابانی به وایرال شدن ویدئوهایش" width="300" height="155" src="https://static.varzesh3.com/img/blank.png" data-src="https://video-images1.varzeshe3.com/covers/2022/06/23/B/ghioqxz1.jpg?w=300" class="owl-lazy lazy" />
    </div>
    <div class="timebox">
        <span class="playicon">
            <img alt="پخش ویدیو" width="10" height="10" src="https://static.varzesh3.com/img/icons/smallplay-icon.svg?w=10" />
        </span>

        <span class="duration">00:49</span>
    </div>
</a>
<div class="video-data">
    <span class="date"> 25 دقیقه پیش - </span>
    <span class="view">1,666 بازدید</span>
</div>
<a class="title" target="_blank" href="https://video.varzesh3.com/video/254278/واکنش-جواد-خیابانی-به-وایرال-شدن-ویدئوهایش">
    <h4>واکنش جواد خیابانی به وایرال شدن ویدئوهایش</h4>
</a>
</div></div>
                            <div class="video-carousel-item"><div class="videobox"> 
<a class="video-cover-box" target="_blank" href="https://video.varzesh3.com/video/254276/خلاصه-والیبال-فرانسه-3-هلند-0">
    <div class="video-cover-image">
            <img alt="خلاصه والیبال فرانسه 3 - هلند 0" width="300" height="155" src="https://static.varzesh3.com/img/blank.png" data-src="https://video-images1.varzeshe3.com/covers/2022/06/23/B/svpxgtwu.jpg?w=300" class="owl-lazy lazy" />
    </div>
    <div class="timebox">
        <span class="playicon">
            <img alt="پخش ویدیو" width="10" height="10" src="https://static.varzesh3.com/img/icons/smallplay-icon.svg?w=10" />
        </span>

        <span class="duration">07:59</span>
    </div>
</a>
<div class="video-data">
    <span class="date"> 38 دقیقه پیش - </span>
    <span class="view">622 بازدید</span>
</div>
<a class="title" target="_blank" href="https://video.varzesh3.com/video/254276/خلاصه-والیبال-فرانسه-3-هلند-0">
    <h4>خلاصه والیبال فرانسه 3 - هلند 0</h4>
</a>
</div></div>
                            <div class="video-carousel-item"><div class="videobox"> 
<a class="video-cover-box" target="_blank" href="https://video.varzesh3.com/video/254277/تقدیر-از-ناظمی-و-مهرابی-افشار-در-دوره-داوری-فوتسال">
    <div class="video-cover-image">
            <img alt="تقدیر از ناظمی و مهرابی افشار در دوره داوری فوتسال" width="300" height="155" src="https://static.varzesh3.com/img/blank.png" data-src="https://video-images1.varzeshe3.com/covers/2022/06/23/B/iiuqsmw1.jpg?w=300" class="owl-lazy lazy" />
    </div>
    <div class="timebox">
        <span class="playicon">
            <img alt="پخش ویدیو" width="10" height="10" src="https://static.varzesh3.com/img/icons/smallplay-icon.svg?w=10" />
        </span>

        <span class="duration">00:58</span>
    </div>
</a>
<div class="video-data">
    <span class="date"> 1 ساعت پیش - </span>
    <span class="view">456 بازدید</span>
</div>
<a class="title" target="_blank" href="https://video.varzesh3.com/video/254277/تقدیر-از-ناظمی-و-مهرابی-افشار-در-دوره-داوری-فوتسال">
    <h4>تقدیر از ناظمی و مهرابی افشار در دوره داوری فوتسال</h4>
</a>
</div></div>
                            <div class="video-carousel-item"><div class="videobox"> 
<a class="video-cover-box" target="_blank" href="https://video.varzesh3.com/video/254275/صحبتهای-احساسی-خسروی-در-حضور-پدرو-گالان">
    <div class="video-cover-image">
            <img alt="صحبتهای احساسی خسروی در حضور پدرو گالان" width="300" height="155" src="https://static.varzesh3.com/img/blank.png" data-src="https://video-images1.varzeshe3.com/covers/2022/06/23/B/xloz1x1v.jpg?w=300" class="owl-lazy lazy" />
    </div>
    <div class="timebox">
        <span class="playicon">
            <img alt="پخش ویدیو" width="10" height="10" src="https://static.varzesh3.com/img/icons/smallplay-icon.svg?w=10" />
        </span>

        <span class="duration">12:30</span>
    </div>
</a>
<div class="video-data">
    <span class="date"> 1 ساعت پیش - </span>
    <span class="view">965 بازدید</span>
</div>
<a class="title" target="_blank" href="https://video.varzesh3.com/video/254275/صحبتهای-احساسی-خسروی-در-حضور-پدرو-گالان">
    <h4>صحبتهای احساسی خسروی در حضور پدرو گالان</h4>
</a>
</div></div>
                </div>
            </div>
        </div>
        <div class="tab-pane fade" id="featured" role="tabpanel" aria-labelledby="featured-tab">
            <div class="tab-pane fade show active" id="new" role="tabpanel" aria-labelledby="new-tab">
                <div class="video-carousel-holder">
                    <div class="video-carousel owl-carousel">
                                <div class="video-carousel-item"><div class="videobox">
<a class="video-cover-box" target="_blank" href="https://video.varzesh3.com/video/254276/خلاصه-والیبال-فرانسه-3-هلند-0">
    <div class="video-cover-image">
            <img alt="خلاصه والیبال فرانسه 3 - هلند 0" width="300" height="155" src="https://static.varzesh3.com/img/blank.png" data-src="https://video-images1.varzeshe3.com/covers/2022/06/23/B/svpxgtwu.jpg?w=300" class="owl-lazy lazy" />
    </div>
    <div class="timebox">
        <span class="playicon">
            <img alt="پخش ویدیو" width="10" height="10" src="https://static.varzesh3.com/img/icons/smallplay-icon.svg?w=10" />
        </span>

        <span class="duration">07:59</span>
    </div>
</a>
<div class="video-data">
    <span class="date">  - </span>
    <span class="view">622 بازدید</span>
</div>
<a class="title" target="_blank" href="https://video.varzesh3.com/video/254276/خلاصه-والیبال-فرانسه-3-هلند-0">
    <h4>خلاصه والیبال فرانسه 3 - هلند 0</h4>
</a>
</div></div>
                                <div class="video-carousel-item"><div class="videobox">
<a class="video-cover-box" target="_blank" href="https://video.varzesh3.com/video/254261/فازمتر-فروش-فالوور-تضمینی-فقط-با-یک-قرارداد">
    <div class="video-cover-image">
            <img alt="فازمتر: فروش فالوور تضمینی فقط با یک قرارداد" width="300" height="155" src="https://static.varzesh3.com/img/blank.png" data-src="https://video-images1.varzeshe3.com/covers/2022/06/22/D/irijg1hg.jpg?w=300" class="owl-lazy lazy" />
    </div>
    <div class="timebox">
        <span class="playicon">
            <img alt="پخش ویدیو" width="10" height="10" src="https://static.varzesh3.com/img/icons/smallplay-icon.svg?w=10" />
        </span>

        <span class="duration">06:47</span>
    </div>
</a>
<div class="video-data">
    <span class="date">  - </span>
    <span class="view">8,250 بازدید</span>
</div>
<a class="title" target="_blank" href="https://video.varzesh3.com/video/254261/فازمتر-فروش-فالوور-تضمینی-فقط-با-یک-قرارداد">
    <h4>فازمتر: فروش فالوور تضمینی فقط با یک قرارداد</h4>
</a>
</div></div>
                                <div class="video-carousel-item"><div class="videobox">
<a class="video-cover-box" target="_blank" href="https://video.varzesh3.com/video/254222/صحبتهای-عطایی-و-بازیکنان-پس-از-شکست-مقابل-بلغارستان">
    <div class="video-cover-image">
            <img alt="صحبتهای عطایی و بازیکنان پس از شکست مقابل بلغارستان" width="300" height="155" src="https://static.varzesh3.com/img/blank.png" data-src="https://video-images1.varzeshe3.com/covers/2022/06/22/B/qyqp24io.jpg?w=300" class="owl-lazy lazy" />
    </div>
    <div class="timebox">
        <span class="playicon">
            <img alt="پخش ویدیو" width="10" height="10" src="https://static.varzesh3.com/img/icons/smallplay-icon.svg?w=10" />
        </span>

        <span class="duration">03:16</span>
    </div>
</a>
<div class="video-data">
    <span class="date">  - </span>
    <span class="view">8,875 بازدید</span>
</div>
<a class="title" target="_blank" href="https://video.varzesh3.com/video/254222/صحبتهای-عطایی-و-بازیکنان-پس-از-شکست-مقابل-بلغارستان">
    <h4>صحبتهای عطایی و بازیکنان پس از شکست مقابل بلغارستان</h4>
</a>
</div></div>
                                <div class="video-carousel-item"><div class="videobox">
<a class="video-cover-box" target="_blank" href="https://video.varzesh3.com/video/254219/حذف-منچسترسیتی-مقابل-تیم-سرمربی-جدید-استقلال">
    <div class="video-cover-image">
            <img alt="حذف منچسترسیتی مقابل تیم سرمربی جدید استقلال" width="300" height="155" src="https://static.varzesh3.com/img/blank.png" data-src="https://video-images1.varzeshe3.com/covers/2022/06/21/D/taubrkea.jpg?w=300" class="owl-lazy lazy" />
    </div>
    <div class="timebox">
        <span class="playicon">
            <img alt="پخش ویدیو" width="10" height="10" src="https://static.varzesh3.com/img/icons/smallplay-icon.svg?w=10" />
        </span>

        <span class="duration">05:25</span>
    </div>
</a>
<div class="video-data">
    <span class="date">  - </span>
    <span class="view">20,163 بازدید</span>
</div>
<a class="title" target="_blank" href="https://video.varzesh3.com/video/254219/حذف-منچسترسیتی-مقابل-تیم-سرمربی-جدید-استقلال">
    <h4>حذف منچسترسیتی مقابل تیم سرمربی جدید استقلال</h4>
</a>
</div></div>
                                <div class="video-carousel-item"><div class="videobox">
<a class="video-cover-box" target="_blank" href="https://video.varzesh3.com/video/254218/خلاصه-والیبال-ایران-0-بلغارستان-3">
    <div class="video-cover-image">
            <img alt="خلاصه والیبال ایران 0 - بلغارستان 3" width="300" height="155" src="https://static.varzesh3.com/img/blank.png" data-src="https://video-images1.varzeshe3.com/covers/2022/06/21/A/2lxp4ti1.jpg?w=300" class="owl-lazy lazy" />
    </div>
    <div class="timebox">
        <span class="playicon">
            <img alt="پخش ویدیو" width="10" height="10" src="https://static.varzesh3.com/img/icons/smallplay-icon.svg?w=10" />
        </span>

        <span class="duration">07:32</span>
    </div>
</a>
<div class="video-data">
    <span class="date">  - </span>
    <span class="view">30,686 بازدید</span>
</div>
<a class="title" target="_blank" href="https://video.varzesh3.com/video/254218/خلاصه-والیبال-ایران-0-بلغارستان-3">
    <h4>خلاصه والیبال ایران 0 - بلغارستان 3</h4>
</a>
</div></div>
                                <div class="video-carousel-item"><div class="videobox">
<a class="video-cover-box" target="_blank" href="https://video.varzesh3.com/video/254214/اشجاری-دستور-اخراج-علی-دایی-از-بالا-آمده-بود">
    <div class="video-cover-image">
            <img alt="اشجاری: دستور اخراج علی دایی از بالا آمده بود " width="300" height="155" src="https://static.varzesh3.com/img/blank.png" data-src="https://video-images1.varzeshe3.com/covers/2022/06/21/D/5ivo5vtc.jpg?w=300" class="owl-lazy lazy" />
    </div>
    <div class="timebox">
        <span class="playicon">
            <img alt="پخش ویدیو" width="10" height="10" src="https://static.varzesh3.com/img/icons/smallplay-icon.svg?w=10" />
        </span>

        <span class="duration">04:34</span>
    </div>
</a>
<div class="video-data">
    <span class="date">  - </span>
    <span class="view">11,021 بازدید</span>
</div>
<a class="title" target="_blank" href="https://video.varzesh3.com/video/254214/اشجاری-دستور-اخراج-علی-دایی-از-بالا-آمده-بود">
    <h4>اشجاری: دستور اخراج علی دایی از بالا آمده بود </h4>
</a>
</div></div>
                                <div class="video-carousel-item"><div class="videobox">
<a class="video-cover-box" target="_blank" href="https://video.varzesh3.com/video/254203/فازمتر-خیلی-کار-قشنگی-کردی-بهش-افتخار-هم-میکنی">
    <div class="video-cover-image">
            <img alt="فازمتر؛ خیلی کار قشنگی کردی، بهش افتخار هم میکنی؟" width="300" height="155" src="https://static.varzesh3.com/img/blank.png" data-src="https://video-images1.varzeshe3.com/covers/2022/06/21/D/p50v0ifn.jpg?w=300" class="owl-lazy lazy" />
    </div>
    <div class="timebox">
        <span class="playicon">
            <img alt="پخش ویدیو" width="10" height="10" src="https://static.varzesh3.com/img/icons/smallplay-icon.svg?w=10" />
        </span>

        <span class="duration">05:30</span>
    </div>
</a>
<div class="video-data">
    <span class="date">  - </span>
    <span class="view">5,493 بازدید</span>
</div>
<a class="title" target="_blank" href="https://video.varzesh3.com/video/254203/فازمتر-خیلی-کار-قشنگی-کردی-بهش-افتخار-هم-میکنی">
    <h4>فازمتر؛ خیلی کار قشنگی کردی، بهش افتخار هم میکنی؟</h4>
</a>
</div></div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
<div class="widget-footer">
    <a href="https://video.varzesh3.com/" target="_blank">مشاهده ویدیوها</a>
</div>
            </div>
        </div>
        

        

<div class="adbox" data-id="111">
            <div class="native-holder">
                <div id='mediaad-aogE'></div>
            </div>
</div>


        <div class="widget-holder">
            <div class="widget newspaper" id="69">
                            
<div class="widget-header">
    <h2>گیشه روزنامه ورزشی</h2>
</div>
<div class="widget-body">
    <div class="newspaper-carousel-holder">
        <div class="newspaper-carousel owl-carousel">
                    <div class="newspaper-carousel-item">
                        <a href="/newspaper/8/1401-04-02/%D8%AE%D8%A8%D8%B1-%D9%88%D8%B1%D8%B2%D8%B4%DB%8C">
                                <img width="300" src="https://newspaper-cdn.varzesh3.com/newspapers/2022/06/23/A/mbgtsdop.jpg?w=300" />
                        
                            <p>خبر ورزشی پنج شنبه 2 تیر</p>
                        </a>
                    </div>
                    <div class="newspaper-carousel-item">
                        <a href="/newspaper/11/1401-04-02/%DA%AF%D9%84">
                                <img width="300" src="https://newspaper-cdn.varzesh3.com/newspapers/2022/06/23/A/t1og44rm.jpg?w=300" />
                        
                            <p>گل پنج شنبه 2 تیر</p>
                        </a>
                    </div>
                    <div class="newspaper-carousel-item">
                        <a href="/newspaper/1/1401-04-02/%D8%A7%D8%A8%D8%B1%D8%A7%D8%B1-%D9%88%D8%B1%D8%B2%D8%B4%DB%8C">
                                <img width="300" src="https://newspaper-cdn.varzesh3.com/newspapers/2022/06/23/A/ubmvndlb.jpg?w=300" />
                        
                            <p>ابرار ورزشی پنج شنبه 2 تیر</p>
                        </a>
                    </div>
                    <div class="newspaper-carousel-item">
                        <a href="/newspaper/4/1401-04-02/%D8%A7%DB%8C%D8%B1%D8%A7%D9%86-%D9%88%D8%B1%D8%B2%D8%B4%DB%8C">
                                <img width="300" src="https://static.varzesh3.com/img/blank.png" data-src="https://newspaper-cdn.varzesh3.com/newspapers/2022/06/23/A/miu2crd5.jpg?w=300" class="owl-lazy lazy" />
                        
                            <p>ایران ورزشی پنج شنبه 2 تیر</p>
                        </a>
                    </div>
                    <div class="newspaper-carousel-item">
                        <a href="/newspaper/2/1401-04-02/%D8%A7%D8%B3%D8%AA%D9%82%D9%84%D8%A7%D9%84">
                                <img width="300" src="https://static.varzesh3.com/img/blank.png" data-src="https://newspaper-cdn.varzesh3.com/newspapers/2022/06/23/A/to2cdnzy.jpg?w=300" class="owl-lazy lazy" />
                        
                            <p>استقلال پنج شنبه 2 تیر</p>
                        </a>
                    </div>
                    <div class="newspaper-carousel-item">
                        <a href="/newspaper/10/1401-04-02/%D8%B4%D9%88%D8%AA">
                                <img width="300" src="https://static.varzesh3.com/img/blank.png" data-src="https://newspaper-cdn.varzesh3.com/newspapers/2022/06/23/A/p35squxf.jpg?w=300" class="owl-lazy lazy" />
                        
                            <p>شوت پنج شنبه 2 تیر</p>
                        </a>
                    </div>
        </div>
    </div>
</div>
<div class="widget-footer"><a href="/newspaper">مشاهده روزنامه ها</a></div>
            </div>
        </div>
        

        

<div class="adbox" data-id="278">
            <a  style="display:none;" class="adlink vrz-lazy" target="_blank" href="https://biz.varzesh3.com/events/click/278">
                <img class="adimage" id="img-278" src="https://static.varzeshe3.com/img/blank.png" data-origin="https://biz-cdn.varzesh3.com/banners/2022/03/23/67e8b711-05b0-4de9-bbe5-ddf0893b2f38.gif" width="300" />
            </a>
</div>


        <div class="widget-holder">
            <div class="widget top-players" id="70">
                            
<div class="widget-header">
    <h2>گلزنان برتر</h2>
    <div class="select-options">
        <select id="league">
                    <option value="900578" data-api="https://football-api.varzesh3.com/v1.0/widgets/70/top-scorers/900578" data-landing="https://www.varzesh3.com/" selected="selected">لیگ برتر ایران</option>
                    <option value="900564" data-api="https://football-api.varzesh3.com/v1.0/widgets/70/top-scorers/900564" data-landing="https://www.varzesh3.com/">لیگ برتر انگلیس</option>
                    <option value="900584" data-api="https://football-api.varzesh3.com/v1.0/widgets/70/top-scorers/900584" data-landing="https://www.varzesh3.com/">لیگ قهرمانان اروپا</option>
                    <option value="900563" data-api="https://football-api.varzesh3.com/v1.0/widgets/70/top-scorers/900563" data-landing="https://www.varzesh3.com/">لالیگا اسپانیا</option>
                    <option value="900560" data-api="https://football-api.varzesh3.com/v1.0/widgets/70/top-scorers/900560" data-landing="https://www.varzesh3.com/">لیگ یک فرانسه</option>
                    <option value="900572" data-api="https://football-api.varzesh3.com/v1.0/widgets/70/top-scorers/900572" data-landing="https://www.varzesh3.com/">لیگ برتر پرتغال</option>
                    <option value="900561" data-api="https://football-api.varzesh3.com/v1.0/widgets/70/top-scorers/900561" data-landing="https://www.varzesh3.com/">سری آ ایتالیا</option>
                    <option value="900559" data-api="https://football-api.varzesh3.com/v1.0/widgets/70/top-scorers/900559" data-landing="https://www.varzesh3.com/">اردیویسه هلند</option>
                    <option value="900562" data-api="https://football-api.varzesh3.com/v1.0/widgets/70/top-scorers/900562" data-landing="https://www.varzesh3.com/">بوندسلیگا آلمان</option>
        </select>
    </div>
</div>
<div class="widget-body">
    <div class="table-holder">
        <table class="topscorers">
            <tbody>
                        <tr>
                            <td>
                                <div class="player"> <figure><img width="30" height="30" src="https://match-cdn.varzesh3.com/football-player/2022/05/09/C/qaylhans.jpg?w=30" /></figure>
                                    <span class="player-name"> <a href="/football/player/114913/گادوین-منشا">گادوین منشا</a> -</span>
                                    <span>مس رفسنجان</span>
                                </div>
                            </td>
                            <td>14</td>
                        </tr>
                        <tr>
                            <td>
                                <div class="player"> <figure><img width="30" height="30" src="https://match-cdn.varzesh3.com/football-player/2022/02/13/B/ujtttuk4.jpg?w=30" /></figure>
                                    <span class="player-name"> <a href="/football/player/139248/کوین-یامگا">کوین یامگا</a> -</span>
                                    <span>استقلال</span>
                                </div>
                            </td>
                            <td>10</td>
                        </tr>
                        <tr>
                            <td>
                                <div class="player"> <figure><img width="30" height="30" src="https://match-cdn.varzesh3.com/football-player/2022/02/13/B/aikzahfy.jpg?w=30" /></figure>
                                    <span class="player-name"> <a href="/football/player/39150/شهریار-مغانلو">شهریار مغانلو</a> -</span>
                                    <span>سپاهان</span>
                                </div>
                                <div class="player"> <figure><img width="30" height="30" src="https://match-cdn.varzesh3.com/football-player/2022/02/12/C/khhn3fyh.jpg?w=30" /></figure>
                                    <span class="player-name"> <a href="/football/player/6571/لوسیانو-پریرا">لوسیانو پریرا</a> -</span>
                                    <span>فولاد</span>
                                </div>
                            </td>
                            <td>9</td>
                        </tr>
                        <tr>
                            <td>
                                <div class="player"> <figure><img width="30" height="30" src="https://match-cdn.varzesh3.com/football-player/2022/03/02/B/z5k31qwd.jpg?w=30" /></figure>
                                    <span class="player-name"> <a href="/football/player/3719/محمد-عباس-زاده">محمد عباس زاده</a> -</span>
                                    <span>تراکتور</span>
                                </div>
                                <div class="player"> <figure><img width="30" height="30" src="https://match-cdn.varzesh3.com/football-player/2022/02/14/C/xtf1kf2y.jpg?w=30" /></figure>
                                    <span class="player-name"> <span>امیرحسین حسین زاده</span> -</span>
                                    <span>استقلال</span>
                                </div>
                            </td>
                            <td>8</td>
                        </tr>
                        <tr>
                            <td>
                                <div class="player"> <figure><img width="30" height="30" src="https://match-cdn.varzesh3.com/football-player/2022/02/13/B/gdweor3o.jpg?w=30" /></figure>
                                    <span class="player-name"> <a href="/football/player/39348/مهدی-عبدی">مهدی عبدی</a> -</span>
                                    <span>پرسپولیس</span>
                                </div>
                                <div class="player"> <figure><img width="30" height="30" src="https://match-cdn.varzesh3.com/football-player/2022/02/14/C/2aqslejl.jpg?w=30" /></figure>
                                    <span class="player-name"> <a href="/football/player/94801/مرتضی-تبریزی">مرتضی تبریزی</a> -</span>
                                    <span>گل گهرسیرجان</span>
                                </div>
                                <div class="player"> <figure><img width="30" height="30" src="https://match-cdn.varzesh3.com/football-player/2022/02/12/D/qfnqcvsm.jpg?w=30" /></figure>
                                    <span class="player-name"> <a href="/football/player/5081/سعید-صادقی">سعید صادقی</a> -</span>
                                    <span>گل گهرسیرجان</span>
                                </div>
                                <div class="player"> <figure><img width="30" height="30" src="https://match-cdn.varzesh3.com/football-player/2022/02/14/B/4s1rkscc.jpg?w=30" /></figure>
                                    <span class="player-name"> <a href="/football/player/9416/کریم-اسلامی">کریم اسلامی</a> -</span>
                                    <span>نساجی مازندران</span>
                                </div>
                            </td>
                            <td>7</td>
                        </tr>
            </tbody>
        </table>
    </div>
</div>

            </div>
        </div>
        

        

<div class="adbox" data-id="113">
            <div class="native-holder">
                <div id="pos-article-display-2922"></div>
            </div>
</div>


        <div class="widget-holder">
            <div class="widget top-players" id="71">
                            
<div class="widget-header">
    <h2>بهترین پاسورها</h2>
    <div class="select-options">
        <select id="league">
                    <option value="900578" data-api="https://football-api.varzesh3.com/v1.0/widgets/71/top-assisters/900578" data-landing="https://www.varzesh3.com/" selected="selected">لیگ برتر ایران</option>
                    <option value="900564" data-api="https://football-api.varzesh3.com/v1.0/widgets/71/top-assisters/900564" data-landing="https://www.varzesh3.com/">لیگ برتر انگلیس</option>
                    <option value="900563" data-api="https://football-api.varzesh3.com/v1.0/widgets/71/top-assisters/900563" data-landing="https://www.varzesh3.com/">لالیگا اسپانیا</option>
                    <option value="900562" data-api="https://football-api.varzesh3.com/v1.0/widgets/71/top-assisters/900562" data-landing="https://www.varzesh3.com/">بوندسلیگا آلمان</option>
                    <option value="900560" data-api="https://football-api.varzesh3.com/v1.0/widgets/71/top-assisters/900560" data-landing="https://www.varzesh3.com/">لیگ یک فرانسه</option>
                    <option value="900561" data-api="https://football-api.varzesh3.com/v1.0/widgets/71/top-assisters/900561" data-landing="https://www.varzesh3.com/">سری آ ایتالیا</option>
        </select>
    </div>
</div>
<div class="widget-body">
    <div class="table-holder">
        <table class="topscorers">
            <tbody>
                        <tr>
                            <td>
                                    <div class="player">
                                        <figure><img width="30" height="30" src="https://match-cdn.varzesh3.com/football-player/2022/02/12/D/qfnqcvsm.jpg?w=30" /></figure>
                                        <span class="player-name"> <a href="/football/player/5081/سعید-صادقی">سعید صادقی</a> -  </span>  
                                        <span>گل گهرسیرجان</span>
                                    </div>
                            </td>
                            <td>14</td>
                        </tr>
                        <tr>
                            <td>
                                    <div class="player">
                                        <figure><img width="30" height="30" src="https://match-cdn.varzesh3.com/football-player/2022/02/13/B/nfqzmhwk.jpg?w=30" /></figure>
                                        <span class="player-name"> <a href="/football/player/6153/مهدی-ترابی">مهدی ترابی</a> -  </span>  
                                        <span>پرسپولیس</span>
                                    </div>
                            </td>
                            <td>11</td>
                        </tr>
                        <tr>
                            <td>
                                    <div class="player">
                                        <figure><img width="30" height="30" src="https://match-cdn.varzesh3.com/football-player/2022/02/13/B/ftqj5sin.jpg?w=30" /></figure>
                                        <span class="player-name"> <a href="/football/player/153020/محسن-آذرباد">محسن آذرباد</a> -  </span>  
                                        <span>مس رفسنجان</span>
                                    </div>
                            </td>
                            <td>10</td>
                        </tr>
                        <tr>
                            <td>
                                    <div class="player">
                                        <figure><img width="30" height="30" src="https://match-cdn.varzesh3.com/football-player/2022/02/13/B/hyu2nrce.jpg?w=30" /></figure>
                                        <span class="player-name"> <a href="/football/player/94723/مهدی-مهدی-پور">مهدی مهدی پور</a> -  </span>  
                                        <span>استقلال</span>
                                    </div>
                            </td>
                            <td>7</td>
                        </tr>
                        <tr>
                            <td>
                                    <div class="player">
                                        <figure><img width="30" height="30" src="https://match-cdn.varzesh3.com/football-player/2022/05/07/B/htw1kbe4.jpg?w=30" /></figure>
                                        <span class="player-name"> <a href="/football/player/567/سجاد-شهباززاده">سجاد شهباززاده</a> -  </span>  
                                        <span>سپاهان</span>
                                    </div>
                                    <div class="player">
                                        <figure><img width="30" height="30" src="https://match-cdn.varzesh3.com/football-player/2022/02/26/B/hxqqpuwi.jpg?w=30" /></figure>
                                        <span class="player-name"> <a href="/football/player/1231/سروش-رفیعی">سروش رفیعی</a> -  </span>  
                                        <span>سپاهان</span>
                                    </div>
                            </td>
                            <td>6</td>
                        </tr>
            </tbody>
        </table>
    </div>
</div>

            </div>
        </div>
        

        

<div class="adbox" data-id="106">
            <div class="native-holder">
                <div id='mediaad-Tvmj'></div>
            </div>
</div>


        <div class="widget-holder">
            <div class="widget league schedual football" id="110">
                            

<div class="widget-header">
    <h2>جام جهانی</h2>
    <div class="select-options">
        <select id="stage">
                    <option value="902033" data-api="https://football-api.varzesh3.com/v1.0/widgets/110/league/902033">گروه A </option>
                    <option value="902034" selected="selected" data-api="https://football-api.varzesh3.com/v1.0/widgets/110/league/902034">گروه B </option>
                    <option value="902035" data-api="https://football-api.varzesh3.com/v1.0/widgets/110/league/902035">گروه C </option>
                    <option value="902036" data-api="https://football-api.varzesh3.com/v1.0/widgets/110/league/902036">گروه D </option>
                    <option value="902037" data-api="https://football-api.varzesh3.com/v1.0/widgets/110/league/902037">گروه E </option>
                    <option value="902038" data-api="https://football-api.varzesh3.com/v1.0/widgets/110/league/902038">گروه F </option>
                    <option value="902039" data-api="https://football-api.varzesh3.com/v1.0/widgets/110/league/902039">گروه G </option>
                    <option value="902040" data-api="https://football-api.varzesh3.com/v1.0/widgets/110/league/902040">گروه H </option>
        </select>
        
    </div>
</div>
<div class="widget-body">
    <div class="scrollable-box" style="max-height:auto">
        <div class="scroll-list-content">
             <div class="widget-subtitle" style="background-color:#ea4336"><h3>گروه B</h3></div>
            <div class="widget-schedual">
                        <div class="date-seprator"><h4>دوشنبه 30 آبان</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/164323/انگلیس-ایران"> <img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                    
                                </div>
                                <div class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><a href="/football/team/362/انگلیس">انگلیس</a></div>
                                    <div class="fixture-result-match-goals"><span class="host"> </span><span> - </span><span class="guest"> </span></div>
                                    <div class="fixture-result-match-guest"><a href="/football/team/313/ایران">ایران</a></div>
                                </div>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">16:30</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/173125/آمریکا-ولز"> <img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                    
                                </div>
                                <div class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>آمریکا</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"> </span><span> - </span><span class="guest"> </span></div>
                                    <div class="fixture-result-match-guest"><a href="/football/team/447/ولز">ولز</a></div>
                                </div>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">22:30</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                        <div class="date-seprator"><h4>جمعه 4 آذر</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/173126/ولز-ایران"> <img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                    
                                </div>
                                <div class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><a href="/football/team/447/ولز">ولز</a></div>
                                    <div class="fixture-result-match-goals"><span class="host"> </span><span> - </span><span class="guest"> </span></div>
                                    <div class="fixture-result-match-guest"><a href="/football/team/313/ایران">ایران</a></div>
                                </div>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">13:30</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/164325/انگلیس-آمریکا"> <img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                    
                                </div>
                                <div class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><a href="/football/team/362/انگلیس">انگلیس</a></div>
                                    <div class="fixture-result-match-goals"><span class="host"> </span><span> - </span><span class="guest"> </span></div>
                                    <div class="fixture-result-match-guest"><span>آمریکا</span></div>
                                </div>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">22:30</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                        <div class="date-seprator"><h4>سه شنبه 8 آذر</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/164324/ایران-آمریکا"> <img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                    
                                </div>
                                <div class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><a href="/football/team/313/ایران">ایران</a></div>
                                    <div class="fixture-result-match-goals"><span class="host"> </span><span> - </span><span class="guest"> </span></div>
                                    <div class="fixture-result-match-guest"><span>آمریکا</span></div>
                                </div>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">22:30</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/173127/ولز-انگلیس"> <img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                    
                                </div>
                                <div class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><a href="/football/team/447/ولز">ولز</a></div>
                                    <div class="fixture-result-match-goals"><span class="host"> </span><span> - </span><span class="guest"> </span></div>
                                    <div class="fixture-result-match-guest"><a href="/football/team/362/انگلیس">انگلیس</a></div>
                                </div>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">22:30</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
            </div>
        </div>
    </div>
    <div class="widget-table">
        <div class="widget-subtitle" style="background-color:#ea4336"><h3>جدول گروه B</h3></div>
        <div class="table-holder">
            <table class=" league-standing widget-standing">
                <thead>
                    <tr>
                        <th scope="col">رتبه</th>
                        <th scope="col">تيم</th>
                        <th scope="col">بازی</th>
                        <th scope="col">امتياز</th>
                    </tr>
                </thead>
                <tbody>
                            <tr>
                                <td scope="row">1</td>
                                <td><span> آمریکا</span></td>
                                <td>0</td>
                                <td>0</td>
                            </tr>
                            <tr>
                                <td scope="row">2</td>
                                <td><a href="/football/team/362/انگلیس"> انگلیس</a></td>
                                <td>0</td>
                                <td>0</td>
                            </tr>
                            <tr>
                                <td scope="row">3</td>
                                <td><a href="/football/team/313/ایران"> ایران</a></td>
                                <td>0</td>
                                <td>0</td>
                            </tr>
                            <tr>
                                <td scope="row">4</td>
                                <td><a href="/football/team/447/ولز"> ولز</a></td>
                                <td>0</td>
                                <td>0</td>
                            </tr>
                </tbody>
            </table>
        </div>
    </div>
</div>
<div class="widget-footer"> <a href="/football/group/902034/گروه-b-جام-جهانی-2022" >مشاهده جدول کامل جام جهانی  گروه B</a></div>
            </div>
        </div>
        <div class="widget-holder">
            <div class="widget league schedual football" id="73">
                            

<div class="widget-header">
    <h2>لیگ قهرمانان آسیا</h2>
    <div class="select-options">
        <select id="stage">
                    <option value="902020" data-api="https://football-api.varzesh3.com/v1.0/widgets/73/league/902020">گروه A </option>
                    <option value="902021" data-api="https://football-api.varzesh3.com/v1.0/widgets/73/league/902021">گروه B </option>
                    <option value="902022" data-api="https://football-api.varzesh3.com/v1.0/widgets/73/league/902022">گروه C </option>
                    <option value="902023" data-api="https://football-api.varzesh3.com/v1.0/widgets/73/league/902023">گروه D </option>
                    <option value="902024" data-api="https://football-api.varzesh3.com/v1.0/widgets/73/league/902024">گروه E </option>
                    <option value="902025" data-api="https://football-api.varzesh3.com/v1.0/widgets/73/league/902025">گروه F </option>
                    <option value="902026" data-api="https://football-api.varzesh3.com/v1.0/widgets/73/league/902026">گروه G </option>
                    <option value="902027" data-api="https://football-api.varzesh3.com/v1.0/widgets/73/league/902027">گروه H </option>
                    <option value="902028" data-api="https://football-api.varzesh3.com/v1.0/widgets/73/league/902028">گروه I </option>
                    <option value="902029" data-api="https://football-api.varzesh3.com/v1.0/widgets/73/league/902029">گروه J </option>
                    <option value="902046" selected="selected" data-api="https://football-api.varzesh3.com/v1.0/widgets/73/league/902046">یک هشتم نهایی </option>
        </select>
        
    </div>
</div>
<div class="widget-body">
    <div class="scrollable-box" style="max-height:300px">
        <div class="scroll-list-content">
             <div class="widget-subtitle" style="background-color:#e74c3c"><h3>یک هشتم نهایی</h3></div>
            <div class="widget-schedual">
                        <div class="date-seprator"><h4>جمعه 28 مرداد</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/172616/تگو-چونبوک-موتورز"> <img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                    
                                </div>
                                <div class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>تگو</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"> </span><span> - </span><span class="guest"> </span></div>
                                    <div class="fixture-result-match-guest"><a href="/football/team/384/چونبوک-موتورز">چونبوک موتورز</a></div>
                                </div>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">15:00</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/172617/پاتوم-تایلند-کیچه-هنگ-کنگ"> <img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                    
                                </div>
                                <div class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>پاتوم تایلند</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"> </span><span> - </span><span class="guest"> </span></div>
                                    <div class="fixture-result-match-guest"><span>کیچه هنگ کنگ</span></div>
                                </div>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">15:00</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/172618/جوهور-دارالتعظیم-اوراوا-ردز"> <img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                    
                                </div>
                                <div class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>جوهور دارالتعظیم</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"> </span><span> - </span><span class="guest"> </span></div>
                                    <div class="fixture-result-match-guest"><span>اوراوا ردز</span></div>
                                </div>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">15:00</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/172619/ویسل-کوبه-یوکوهاما-مارینوس"> <img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                    
                                </div>
                                <div class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>ویسل کوبه</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"> </span><span> - </span><span class="guest"> </span></div>
                                    <div class="fixture-result-match-guest"><span>یوکوهاما مارینوس</span></div>
                                </div>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">15:00</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                        <div class="date-seprator"><h4>جمعه 14 بهمن</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/172587/الهلال-عربستان-شباب-الاهلی-امارات"> <img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                    
                                </div>
                                <div class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><a href="/football/team/389/الهلال-عربستان">الهلال عربستان</a></div>
                                    <div class="fixture-result-match-goals"><span class="host"> </span><span> - </span><span class="guest"> </span></div>
                                    <div class="fixture-result-match-guest"><a href="/football/team/902816/شباب-الاهلی-امارات">شباب الاهلی امارات</a></div>
                                </div>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">20:00</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/172588/الشباب-عربستان-نسف-قارشی"> <img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                    
                                </div>
                                <div class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><a href="/football/team/399/الشباب-عربستان">الشباب عربستان</a></div>
                                    <div class="fixture-result-match-goals"><span class="host"> </span><span> - </span><span class="guest"> </span></div>
                                    <div class="fixture-result-match-guest"><a href="/football/team/642/نسف-قارشی">نسف قارشی</a></div>
                                </div>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">20:00</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/172589/الدحیل-الریان"> <img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                    
                                </div>
                                <div class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><a href="/football/team/645/الدحیل">الدحیل</a></div>
                                    <div class="fixture-result-match-goals"><span class="host"> </span><span> - </span><span class="guest"> </span></div>
                                    <div class="fixture-result-match-guest"><a href="/football/team/397/الریان">الریان </a></div>
                                </div>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">20:00</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/172590/الفیصلی-عربستان-فولاد"> <img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                    
                                </div>
                                <div class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>الفیصلی عربستان</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"> </span><span> - </span><span class="guest"> </span></div>
                                    <div class="fixture-result-match-guest"><a href="/football/team/9/فولاد">فولاد</a></div>
                                </div>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">20:00</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
            </div>
        </div>
    </div>
    
</div>
<div class="widget-footer"> <a href="/football/league/900604/لیگ-قهرمانان-آسیا-2022" >مشاهده لیگ قهرمانان آسیا</a></div>
            </div>
        </div>
        

        

<div class="adbox" data-id="166">
            <div class="native-holder">
                <div id="pos-article-display-10354"></div>
            </div>
</div>


        <div class="widget-holder">
            <div class="widget league schedual football" id="104">
                            

<div class="widget-header">
    <h2>لیگ قهرمانان اروپا</h2>
    <div class="select-options">
        <select id="stage">
                    <option value="901916" data-api="https://football-api.varzesh3.com/v1.0/widgets/104/league/901916">گروه A </option>
                    <option value="901917" data-api="https://football-api.varzesh3.com/v1.0/widgets/104/league/901917">گروه B </option>
                    <option value="901918" data-api="https://football-api.varzesh3.com/v1.0/widgets/104/league/901918">گروه C </option>
                    <option value="901919" data-api="https://football-api.varzesh3.com/v1.0/widgets/104/league/901919">گروه D </option>
                    <option value="901920" data-api="https://football-api.varzesh3.com/v1.0/widgets/104/league/901920">گروه E </option>
                    <option value="901921" data-api="https://football-api.varzesh3.com/v1.0/widgets/104/league/901921">گروه F </option>
                    <option value="901922" data-api="https://football-api.varzesh3.com/v1.0/widgets/104/league/901922">گروه G </option>
                    <option value="901923" data-api="https://football-api.varzesh3.com/v1.0/widgets/104/league/901923">گروه H </option>
                    <option value="901981" data-api="https://football-api.varzesh3.com/v1.0/widgets/104/league/901981">یک هشتم نهایی </option>
                    <option value="902030" data-api="https://football-api.varzesh3.com/v1.0/widgets/104/league/902030">یک چهارم نهایی </option>
                    <option value="902042" data-api="https://football-api.varzesh3.com/v1.0/widgets/104/league/902042">نیمه نهایی </option>
                    <option value="902047" selected="selected" data-api="https://football-api.varzesh3.com/v1.0/widgets/104/league/902047">فینال </option>
        </select>
        
    </div>
</div>
<div class="widget-body">
    <div class="scrollable-box" style="max-height:auto">
        <div class="scroll-list-content">
             <div class="widget-subtitle" style="background-color:#33ab54"><h3>فینال</h3></div>
            <div class="widget-schedual">
                        <div class="date-seprator"><h4>شنبه 7 خرداد</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/172640/لیورپول-رئال-مادرید"> <img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                    
                                </div>
                                <div class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><a href="/football/team/83/لیورپول">لیورپول</a></div>
                                    <div class="fixture-result-match-goals"><span class="host">0</span><span> - </span><span class="guest">1</span></div>
                                    <div class="fixture-result-match-guest"><a href="/football/team/102/رئال-مادرید">رئال مادرید</a></div>
                                </div>
                                <div class="fixture-result-match-time">
                                    <a target="_blank" href="https://video.varzesh3.com/video/252737/"> <img src="https://static.varzesh3.com/img/icons/video-link.svg" /></a>
                                    <span class="match-clock"></span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
            </div>
        </div>
    </div>
    
</div>
<div class="widget-footer"> <a href="/football/league/900584/لیگ-قهرمانان-اروپا-2021-2022" >مشاهده لیگ قهرمانان اروپا</a></div>
            </div>
        </div>
        <div class="widget-holder">
            <div class="widget league schedual football" id="74">
                            

<div class="widget-header">
    <h2>لیگ اروپا</h2>
    <div class="select-options">
        <select id="stage">
                    <option value="901924" data-api="https://football-api.varzesh3.com/v1.0/widgets/74/league/901924">گروه A </option>
                    <option value="901925" data-api="https://football-api.varzesh3.com/v1.0/widgets/74/league/901925">گروه B </option>
                    <option value="901926" data-api="https://football-api.varzesh3.com/v1.0/widgets/74/league/901926">گروه C </option>
                    <option value="901927" data-api="https://football-api.varzesh3.com/v1.0/widgets/74/league/901927">گروه D </option>
                    <option value="901928" data-api="https://football-api.varzesh3.com/v1.0/widgets/74/league/901928">گروه E </option>
                    <option value="901929" data-api="https://football-api.varzesh3.com/v1.0/widgets/74/league/901929">گروه F </option>
                    <option value="901930" data-api="https://football-api.varzesh3.com/v1.0/widgets/74/league/901930">گروه G </option>
                    <option value="901931" data-api="https://football-api.varzesh3.com/v1.0/widgets/74/league/901931">گروه H </option>
                    <option value="901982" data-api="https://football-api.varzesh3.com/v1.0/widgets/74/league/901982">پلی‌آف </option>
                    <option value="902017" data-api="https://football-api.varzesh3.com/v1.0/widgets/74/league/902017">یک هشتم نهایی </option>
                    <option value="902031" data-api="https://football-api.varzesh3.com/v1.0/widgets/74/league/902031">یک چهارم نهایی </option>
                    <option value="902043" data-api="https://football-api.varzesh3.com/v1.0/widgets/74/league/902043">نیمه نهایی </option>
                    <option value="902048" selected="selected" data-api="https://football-api.varzesh3.com/v1.0/widgets/74/league/902048">فینال </option>
        </select>
        
    </div>
</div>
<div class="widget-body">
    <div class="scrollable-box" style="max-height:auto">
        <div class="scroll-list-content">
             <div class="widget-subtitle" style="background-color:#33ab54"><h3>فینال</h3></div>
            <div class="widget-schedual">
                        <div class="date-seprator"><h4>چهارشنبه 28 اردیبهشت</h4></div>
                            <div class="fixture-result-match even has-penalty">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/172674/آینتراخت-فرانکفورت-گلاسکو-رنجرز"> <img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                    
                                </div>
                                <div class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><a href="/football/team/127/آینتراخت-فرانکفورت">آینتراخت فرانکفورت</a></div>
                                    <div class="fixture-result-match-goals"><span class="host">1 (5)</span><span> - </span><span class="guest">1 (4)</span></div>
                                    <div class="fixture-result-match-guest"><a href="/football/team/287/گلاسکو-رنجرز">گلاسکو رنجرز</a></div>
                                </div>
                                <div class="fixture-result-match-time">
                                    <a target="_blank" href="https://video.varzesh3.com/video/252044/"> <img src="https://static.varzesh3.com/img/icons/video-link.svg" /></a>
                                    <span class="match-clock"></span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
            </div>
        </div>
    </div>
    
</div>
<div class="widget-footer"> <a href="/football/league/900585/لیگ-اروپا-2021-2022" >مشاهده لیگ اروپا</a></div>
            </div>
        </div>
        



        <div class="widget-holder">
            <div class="widget league schedual football" id="75">
                            

<div class="widget-header">
    <h2>لیگ کنفرانس اروپا</h2>
    <div class="select-options">
        <select id="stage">
                    <option value="901932" data-api="https://football-api.varzesh3.com/v1.0/widgets/75/league/901932">گروه A </option>
                    <option value="901933" data-api="https://football-api.varzesh3.com/v1.0/widgets/75/league/901933">گروه B </option>
                    <option value="901934" data-api="https://football-api.varzesh3.com/v1.0/widgets/75/league/901934">گروه C </option>
                    <option value="901935" data-api="https://football-api.varzesh3.com/v1.0/widgets/75/league/901935">گروه D </option>
                    <option value="901936" data-api="https://football-api.varzesh3.com/v1.0/widgets/75/league/901936">گروه E </option>
                    <option value="901937" data-api="https://football-api.varzesh3.com/v1.0/widgets/75/league/901937">گروه F </option>
                    <option value="901938" data-api="https://football-api.varzesh3.com/v1.0/widgets/75/league/901938">گروه G </option>
                    <option value="901939" data-api="https://football-api.varzesh3.com/v1.0/widgets/75/league/901939">گروه H </option>
                    <option value="901984" data-api="https://football-api.varzesh3.com/v1.0/widgets/75/league/901984">پلی‌آف </option>
                    <option value="902018" data-api="https://football-api.varzesh3.com/v1.0/widgets/75/league/902018">یک هشتم نهایی </option>
                    <option value="902032" data-api="https://football-api.varzesh3.com/v1.0/widgets/75/league/902032">یک چهارم نهایی </option>
                    <option value="902044" data-api="https://football-api.varzesh3.com/v1.0/widgets/75/league/902044">نیمه نهایی </option>
                    <option value="902049" selected="selected" data-api="https://football-api.varzesh3.com/v1.0/widgets/75/league/902049">فینال </option>
        </select>
        
    </div>
</div>
<div class="widget-body">
    <div class="scrollable-box" style="max-height:auto">
        <div class="scroll-list-content">
             <div class="widget-subtitle" style="background-color:#33ab54"><h3>فینال</h3></div>
            <div class="widget-schedual">
                        <div class="date-seprator"><h4>چهارشنبه 4 خرداد</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/172675/آاس-رم-فاینورد"> <img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                    
                                </div>
                                <div class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><a href="/football/team/71/آاس-رم">آاس رم</a></div>
                                    <div class="fixture-result-match-goals"><span class="host">1</span><span> - </span><span class="guest">0</span></div>
                                    <div class="fixture-result-match-guest"><a href="/football/team/162/فاینورد">فاینورد</a></div>
                                </div>
                                <div class="fixture-result-match-time">
                                    <a target="_blank" href="https://video.varzesh3.com/video/252561/"> <img src="https://static.varzesh3.com/img/icons/video-link.svg" /></a>
                                    <span class="match-clock"></span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
            </div>
        </div>
    </div>
    
</div>
<div class="widget-footer"> <a href="/football/league/900586/لیگ-کنفرانس-اروپا-2021-2022" >مشاهده لیگ کنفرانس اروپا</a></div>
            </div>
        </div>
        <div class="widget-holder">
            <div class="widget league schedual football" id="112">
                            

<div class="widget-header">
    <h2>لیگ ملت‌های اروپا</h2>
    <div class="select-options">
        <select id="league">
                    <option value="318" selected="selected">لیگ A </option>
                    <option value="319">لیگ B </option>
                    <option value="320">لیگ C </option>
                    <option value="321">لیگ D </option>
        </select>
        <select id="stage">
                    <option style='display: block' value="902055" selected="selected" data-league="318" data-api="https://football-api.varzesh3.com/v1.0/widgets/112/multiple-league/902055">گروه 1 </option>
                    <option style='display: none' value="902059" data-league="319" data-api="https://football-api.varzesh3.com/v1.0/widgets/112/multiple-league/902059">گروه 1 </option>
                    <option style='display: none' value="902063" data-league="320" data-api="https://football-api.varzesh3.com/v1.0/widgets/112/multiple-league/902063">گروه ۱ </option>
                    <option style='display: none' value="902067" data-league="321" data-api="https://football-api.varzesh3.com/v1.0/widgets/112/multiple-league/902067">گروه ۱ </option>
                    <option style='display: block' value="902056" data-league="318" data-api="https://football-api.varzesh3.com/v1.0/widgets/112/multiple-league/902056">گروه 2 </option>
                    <option style='display: none' value="902060" data-league="319" data-api="https://football-api.varzesh3.com/v1.0/widgets/112/multiple-league/902060">گروه 2 </option>
                    <option style='display: none' value="902064" data-league="320" data-api="https://football-api.varzesh3.com/v1.0/widgets/112/multiple-league/902064">گروه ۲ </option>
                    <option style='display: none' value="902068" data-league="321" data-api="https://football-api.varzesh3.com/v1.0/widgets/112/multiple-league/902068">گروه ۲ </option>
                    <option style='display: block' value="902057" data-league="318" data-api="https://football-api.varzesh3.com/v1.0/widgets/112/multiple-league/902057">گروه 3 </option>
                    <option style='display: none' value="902061" data-league="319" data-api="https://football-api.varzesh3.com/v1.0/widgets/112/multiple-league/902061">گروه 3 </option>
                    <option style='display: none' value="902065" data-league="320" data-api="https://football-api.varzesh3.com/v1.0/widgets/112/multiple-league/902065">گروه ۳ </option>
                    <option style='display: block' value="902058" data-league="318" data-api="https://football-api.varzesh3.com/v1.0/widgets/112/multiple-league/902058">گروه 4 </option>
                    <option style='display: none' value="902062" data-league="319" data-api="https://football-api.varzesh3.com/v1.0/widgets/112/multiple-league/902062">گروه 4 </option>
                    <option style='display: none' value="902066" data-league="320" data-api="https://football-api.varzesh3.com/v1.0/widgets/112/multiple-league/902066">گروه ۴ </option>
        </select>
    </div>
</div>
<div class="widget-body">
    <div class="scrollable-box" style="max-height:300px">
        <div class="scroll-list-content">
            <div class="widget-subtitle" style="background-color:#47a0c2"><h3>گروه 1</h3></div>
            <div class="widget-schedual">
                        <div class="date-seprator"><h4>جمعه 13 خرداد</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/172947/کرواسی-اتریش"> <img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                    
                                </div>
                                <div class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>کرواسی</span></div>
                                    <div class="fixture-result-match-goals"><span class="host">0</span><span> - </span><span class="guest">3</span></div>
                                    <div class="fixture-result-match-guest"><span>اتریش</span></div>
                                </div>
                                <div class="fixture-result-match-time">
                                    <a target="_blank" href="https://video.varzesh3.com/video/253208/"> <img src="https://static.varzesh3.com/img/icons/video-link.svg" /></a>
                                    <span class="match-clock"></span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/172948/فرانسه-دانمارک"> <img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                    
                                </div>
                                <div class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><a href="/football/team/352/فرانسه">فرانسه</a></div>
                                    <div class="fixture-result-match-goals"><span class="host">1</span><span> - </span><span class="guest">2</span></div>
                                    <div class="fixture-result-match-guest"><a href="/football/team/361/دانمارک">دانمارک</a></div>
                                </div>
                                <div class="fixture-result-match-time">
                                    <a target="_blank" href="https://video.varzesh3.com/video/253207/"> <img src="https://static.varzesh3.com/img/icons/video-link.svg" /></a>
                                    <span class="match-clock"></span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                        <div class="date-seprator"><h4>دوشنبه 16 خرداد</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/172960/اتریش-دانمارک"> <img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                    
                                </div>
                                <div class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>اتریش</span></div>
                                    <div class="fixture-result-match-goals"><span class="host">1</span><span> - </span><span class="guest">2</span></div>
                                    <div class="fixture-result-match-guest"><a href="/football/team/361/دانمارک">دانمارک</a></div>
                                </div>
                                <div class="fixture-result-match-time">
                                    <a target="_blank" href="https://video.varzesh3.com/video/253356/"> <img src="https://static.varzesh3.com/img/icons/video-link.svg" /></a>
                                    <span class="match-clock"></span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/172961/کرواسی-فرانسه"> <img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                    
                                </div>
                                <div class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>کرواسی</span></div>
                                    <div class="fixture-result-match-goals"><span class="host">1</span><span> - </span><span class="guest">1</span></div>
                                    <div class="fixture-result-match-guest"><a href="/football/team/352/فرانسه">فرانسه</a></div>
                                </div>
                                <div class="fixture-result-match-time">
                                    <a target="_blank" href="https://video.varzesh3.com/video/253346/"> <img src="https://static.varzesh3.com/img/icons/video-link.svg" /></a>
                                    <span class="match-clock"></span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                        <div class="date-seprator"><h4>جمعه 20 خرداد</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/172968/اتریش-فرانسه"> <img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                    
                                </div>
                                <div class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>اتریش</span></div>
                                    <div class="fixture-result-match-goals"><span class="host">1</span><span> - </span><span class="guest">1</span></div>
                                    <div class="fixture-result-match-guest"><a href="/football/team/352/فرانسه">فرانسه</a></div>
                                </div>
                                <div class="fixture-result-match-time">
                                    <a target="_blank" href="https://video.varzesh3.com/video/253560/"> <img src="https://static.varzesh3.com/img/icons/video-link.svg" /></a>
                                    <span class="match-clock"></span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/172969/دانمارک-کرواسی"> <img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                    
                                </div>
                                <div class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><a href="/football/team/361/دانمارک">دانمارک</a></div>
                                    <div class="fixture-result-match-goals"><span class="host">0</span><span> - </span><span class="guest">1</span></div>
                                    <div class="fixture-result-match-guest"><span>کرواسی</span></div>
                                </div>
                                <div class="fixture-result-match-time">
                                    <a target="_blank" href="https://video.varzesh3.com/video/253561/"> <img src="https://static.varzesh3.com/img/icons/video-link.svg" /></a>
                                    <span class="match-clock"></span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                        <div class="date-seprator"><h4>دوشنبه 23 خرداد</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/172976/دانمارک-اتریش"> <img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                    
                                </div>
                                <div class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><a href="/football/team/361/دانمارک">دانمارک</a></div>
                                    <div class="fixture-result-match-goals"><span class="host">2</span><span> - </span><span class="guest">0</span></div>
                                    <div class="fixture-result-match-guest"><span>اتریش</span></div>
                                </div>
                                <div class="fixture-result-match-time">
                                    <a target="_blank" href="https://video.varzesh3.com/video/253758/"> <img src="https://static.varzesh3.com/img/icons/video-link.svg" /></a>
                                    <span class="match-clock"></span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/172977/فرانسه-کرواسی"> <img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                    
                                </div>
                                <div class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><a href="/football/team/352/فرانسه">فرانسه</a></div>
                                    <div class="fixture-result-match-goals"><span class="host">0</span><span> - </span><span class="guest">1</span></div>
                                    <div class="fixture-result-match-guest"><span>کرواسی</span></div>
                                </div>
                                <div class="fixture-result-match-time">
                                    <a target="_blank" href="https://video.varzesh3.com/video/253757/"> <img src="https://static.varzesh3.com/img/icons/video-link.svg" /></a>
                                    <span class="match-clock"></span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                        <div class="date-seprator"><h4>پنج شنبه 31 شهریور</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/172983/کرواسی-دانمارک"> <img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                    
                                </div>
                                <div class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>کرواسی</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"> </span><span> - </span><span class="guest"> </span></div>
                                    <div class="fixture-result-match-guest"><a href="/football/team/361/دانمارک">دانمارک</a></div>
                                </div>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">22:15</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/172984/فرانسه-اتریش"> <img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                    
                                </div>
                                <div class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><a href="/football/team/352/فرانسه">فرانسه</a></div>
                                    <div class="fixture-result-match-goals"><span class="host"> </span><span> - </span><span class="guest"> </span></div>
                                    <div class="fixture-result-match-guest"><span>اتریش</span></div>
                                </div>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">22:15</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                        <div class="date-seprator"><h4>یکشنبه 3 مهر</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/172990/اتریش-کرواسی"> <img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                    
                                </div>
                                <div class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>اتریش</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"> </span><span> - </span><span class="guest"> </span></div>
                                    <div class="fixture-result-match-guest"><span>کرواسی</span></div>
                                </div>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">22:15</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/172991/دانمارک-فرانسه"> <img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                    
                                </div>
                                <div class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><a href="/football/team/361/دانمارک">دانمارک</a></div>
                                    <div class="fixture-result-match-goals"><span class="host"> </span><span> - </span><span class="guest"> </span></div>
                                    <div class="fixture-result-match-guest"><a href="/football/team/352/فرانسه">فرانسه</a></div>
                                </div>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock">22:15</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
            </div>
        </div>
    </div>
    <div class="widget-table">
        <div class="widget-subtitle" style="background-color:#47a0c2"><h3>جدول گروه 1</h3></div>
        <div class="table-holder">
            <table class=" league-standing widget-standing">
                <thead>
                    <tr>
                        <th scope="col">رتبه</th>
                        <th scope="col">تيم</th>
                        <th scope="col">بازی</th>
                        <th scope="col">امتياز</th>
                    </tr>
                </thead>
                <tbody>
                            <tr>
                                <td scope="row">1</td>
                                <td><a href="/football/team/361/دانمارک"> دانمارک</a></td>
                                <td>4</td>
                                <td>9</td>
                            </tr>
                            <tr>
                                <td scope="row">2</td>
                                <td><span> کرواسی</span></td>
                                <td>4</td>
                                <td>7</td>
                            </tr>
                            <tr>
                                <td scope="row">3</td>
                                <td><span> اتریش</span></td>
                                <td>4</td>
                                <td>4</td>
                            </tr>
                            <tr>
                                <td scope="row">4</td>
                                <td><a href="/football/team/352/فرانسه"> فرانسه</a></td>
                                <td>4</td>
                                <td>2</td>
                            </tr>
                </tbody>
            </table>
        </div>
    </div>
</div>
<div class="widget-footer"> <a href="/football/group/902055/گروه-1-لیگ-ملت-های-اروپا-لیگ-a-2022-2023">مشاهده جدول کامل لیگ ملت‌های اروپا - لیگ A گروه 1</a></div>
            </div>
        </div>

                </div>
            </div>
            <div class="v300-col">
                

        

        

<div class="adbox" data-id="257">
            <a  style="display:none;" class="adlink vrz-lazy" target="_blank" href="https://biz.varzesh3.com/events/click/257">
                <img class="adimage" id="img-257" src="https://static.varzeshe3.com/img/blank.png" data-origin="https://biz-cdn.varzesh3.com/banners/2022/06/13/879e8604-1f47-4e50-9691-bc29b5a792f7.gif" width="300" />
            </a>
</div>


        <div class="widget-holder">
            <div class="widget news" id="66">
                            
<div class="widget-header"><h2>آخرین اخبار فوتبال</h2></div>
<div class="widget-body">
    <div class="news-tabs">
        <ul>
            <li data-type="Latest" class="active">جدیدترین‌ها</li>
            <li data-type="MostVisited" data-url="https://news-api.varzesh3.com/v1.0/news/most-visited">پربازدیدترین‌ها</li>
            <li data-type="MostCommented" data-url="https://news-api.varzesh3.com/v1.0/news/most-commented">پرحاشیه ترین‌ها</li>
        </ul>
    </div>
    <div class="news-content" data-type="Latest">
        <div class="news-filter">

                <div class="new-filter-item">
                    <input type="checkbox" name="66-newsFilter" id="66-origin-1" checked value="1" data-filter-type="origin" />
                    <label for="66-origin-1">داخلی</label>
                </div>
                <div class="new-filter-item">
                    <input type="checkbox" name="66-newsFilter" id="66-origin-2" checked value="2" data-filter-type="origin" />
                    <label for="66-origin-2">خارجی</label>
                </div>
                <div class="new-filter-item">
                    <input type="checkbox" name="66-newsFilter" id="66-media-2" checked value="2" data-filter-type="media" />
                    <label for="66-media-2">ویدیو</label>
                </div>
                        <div class="new-filter-item">
                            <input type="checkbox" name="66-newsFilter" id="66-sport-3" checked value="3" data-filter-type="sport" />
                            <label for="66-sport-3">والیبال</label>
                        </div>
        </div>
        <div class="alert-message">حداقل یکی از گزینه ها باید فعال باشد.</div>
        <div class="news-main-list scrollable-box" data-height="1500" style="max-height: 1500px">
            <div class="scroll-list-content">
                <ul>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="صحبت های عطایی قبل از بازی با آمریکا" href="https://video.varzesh3.com/video/254281/صحبت-های-عطایی-قبل-از-بازی-با-آمریکا"> <span class="news-type"></span>صحبت های عطایی قبل از بازی با آمریکا</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="ایران همچنان صدرنشین رنکینگ آسیا" href="https://www.varzesh3.com/news/1830332/ایران-همچنان-صدرنشین-رنکینگ-آسیا"> <span class="news-type"></span>ایران همچنان صدرنشین رنکینگ آسیا</a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="عنایتی: هیچوقت برای حضور در استقلال شرطی نگذاشتم" href="https://video.varzesh3.com/video/254280/عنایتی-هیچوقت-برای-حضور-در-استقلال-شرطی-نگذاشتم"> <span class="news-type"></span>عنایتی: هیچوقت برای حضور در استقلال شرطی نگذاشتم</a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="پول نخواستیم، تنها ذره ای احترام برای داوران قائل باشیم" href="https://video.varzesh3.com/video/254279/پول-نخواستیم-تنها-ذره-ای-احترام-برای-داوران-قائل-باشیم"> <span class="news-type"></span>پول نخواستیم، تنها ذره ای احترام برای داوران قائل باشیم</a></li>
                            <li class="text-type" data-origin="2" data-media="1" data-tag="" data-sport="3"><a title="اسپراو: این بازیکنان ایران را تا به حال ندیده‌ام" href="https://www.varzesh3.com/news/1830331/اسپراو-این-بازیکنان-ایران-را-تا-به-حال-ندیده-ام"> <span class="news-type"></span>اسپراو: این بازیکنان ایران را تا به حال ندیده‌ام</a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="واکنش جواد خیابانی به وایرال شدن ویدئوهایش" href="https://video.varzesh3.com/video/254278/واکنش-جواد-خیابانی-به-وایرال-شدن-ویدئوهایش"> <span class="news-type"></span>واکنش جواد خیابانی به وایرال شدن ویدئوهایش</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="ایمان باصفا: رفتن از استقلال بزرگ‌ترین اشتباهم بود " href="https://www.varzesh3.com/news/1830330/ایمان-باصفا-رفتن-از-استقلال-بزرگ-ترین-اشتباهم-بود"> <span class="news-type"></span>ایمان باصفا: رفتن از استقلال بزرگ‌ترین اشتباهم بود </a></li>
                            <li class="text-type" data-origin="2" data-media="1" data-tag="" data-sport="1"><a title="سکوت زیدان شکست؛ حرکتی تاریخی به افتخار فوق‌ستاره!" href="https://www.varzesh3.com/news/1830327/سکوت-زیدان-شکست-حرکتی-تاریخی-به-افتخار-فوق-ستاره"> <span class="news-type"></span>سکوت زیدان شکست؛ حرکتی تاریخی به افتخار فوق‌ستاره!</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="اولین تمدیدی فولاد معرفی شد (عکس)" href="https://www.varzesh3.com/news/1830329/اولین-تمدیدی-فولاد-معرفی-شد-عکس"> <span class="news-type"></span>اولین تمدیدی فولاد معرفی شد (عکس)</a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="خلاصه والیبال فرانسه 3 - هلند 0" href="https://video.varzesh3.com/video/254276/خلاصه-والیبال-فرانسه-3-هلند-0"> <span class="news-type"></span>خلاصه والیبال فرانسه 3 - هلند 0</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="دو ستاره‌ای که استقلال را فاتح نقل‌و‌انتقالات می‌کنند!" href="https://www.varzesh3.com/news/1830328/دو-ستاره-ای-که-استقلال-را-فاتح-نقل-و-انتقالات-می-کنند"> <span class="news-type"></span>دو ستاره‌ای که استقلال را فاتح نقل‌و‌انتقالات می‌کنند!</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="چرا مدافع سابق استقلال دستیار مرفاوی نشد؟ " href="https://www.varzesh3.com/news/1830326/چرا-مدافع-سابق-استقلال-دستیار-مرفاوی-نشد"> <span class="news-type"></span>چرا مدافع سابق استقلال دستیار مرفاوی نشد؟ </a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="تقدیر از ناظمی و مهرابی افشار در دوره داوری فوتسال" href="https://video.varzesh3.com/video/254277/تقدیر-از-ناظمی-و-مهرابی-افشار-در-دوره-داوری-فوتسال"> <span class="news-type"></span>تقدیر از ناظمی و مهرابی افشار در دوره داوری فوتسال</a></li>
                            <li class="text-type" data-origin="2" data-media="1" data-tag="" data-sport="1"><a title="تمدید قرارداد دیاز به شرط قهرمانی" href="https://www.varzesh3.com/news/1830325/تمدید-قرارداد-دیاز-به-شرط-قهرمانی"> <span class="news-type"></span>تمدید قرارداد دیاز به شرط قهرمانی</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="تیم ملی و وعده دو بازی دوستانه بزرگ!" href="https://www.varzesh3.com/news/1830324/تیم-ملی-و-وعده-دو-بازی-دوستانه-بزرگ"> <span class="news-type"></span>تیم ملی و وعده دو بازی دوستانه بزرگ!</a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="صحبتهای احساسی خسروی در حضور پدرو گالان" href="https://video.varzesh3.com/video/254275/صحبتهای-احساسی-خسروی-در-حضور-پدرو-گالان"> <span class="news-type"></span>صحبتهای احساسی خسروی در حضور پدرو گالان</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="اسپانسر البسه تیم ملی شاید خارجی باشد" href="https://www.varzesh3.com/news/1830322/اسپانسر-البسه-تیم-ملی-شاید-خارجی-باشد"> <span class="news-type"></span>اسپانسر البسه تیم ملی شاید خارجی باشد</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="مهدی رجب‌زاده سرمربی فجرسپاسی شد" href="https://www.varzesh3.com/news/1830321/مهدی-رجب-زاده-سرمربی-فجرسپاسی-شد"> <span class="news-type"></span>مهدی رجب‌زاده سرمربی فجرسپاسی شد</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="میرشاد مسئولیت فرشاد را گردن نگرفت!" href="https://www.varzesh3.com/news/1830320/میرشاد-مسئولیت-فرشاد-را-گردن-نگرفت"> <span class="news-type"></span>میرشاد مسئولیت فرشاد را گردن نگرفت!</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="میلیاردری که سرمایه‌گذاری در فوتبال را توصیه نمی‌کند!" href="https://www.varzesh3.com/news/1830319/میلیاردری-که-سرمایه-گذاری-در-فوتبال-را-توصیه-نمی-کند"> <span class="news-type"></span>میلیاردری که سرمایه‌گذاری در فوتبال را توصیه نمی‌کند!</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="نامجومطلق: ساپینتو می‌تواند نظر هواداران را جلب کند" href="https://www.varzesh3.com/news/1830318/نامجومطلق-ساپینتو-می-تواند-نظر-هواداران-را-جلب-کند"> <span class="news-type"></span>نامجومطلق: ساپینتو می‌تواند نظر هواداران را جلب کند</a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="ای کاش دستمزد داوران فوتسال به گوش فیفا نمی رسید" href="https://video.varzesh3.com/video/254273/ای-کاش-دستمزد-داوران-فوتسال-به-گوش-فیفا-نمی-رسید"> <span class="news-type"></span>ای کاش دستمزد داوران فوتسال به گوش فیفا نمی رسید</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="کریم باقری همچنان دست‌نیافتنی است " href="https://www.varzesh3.com/news/1830317/کریم-باقری-همچنان-دست-نیافتنی-است"> <span class="news-type"></span>کریم باقری همچنان دست‌نیافتنی است </a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="من وظیفه پاسخگویی به شایعات بی اساس راِ ندارم" href="https://video.varzesh3.com/video/254272/من-وظیفه-پاسخگویی-به-شایعات-بی-اساس-راِ-ندارم"> <span class="news-type"></span>من وظیفه پاسخگویی به شایعات بی اساس راِ ندارم</a></li>
                            <li class="text-type" data-origin="3" data-media="1" data-tag="" data-sport="2"><a title="طیبی گل زد ولی بنفیکا فینال دوم را هم باخت" href="https://www.varzesh3.com/news/1830316/طیبی-گل-زد-ولی-بنفیکا-فینال-دوم-را-هم-باخت"> <span class="news-type"></span>طیبی گل زد ولی بنفیکا فینال دوم را هم باخت</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="کاوه رضایی؛ بمبی که در ایران منفجر نمی‌شود!" href="https://www.varzesh3.com/news/1830315/کاوه-رضایی-بمبی-که-در-ایران-منفجر-نمی-شود"> <span class="news-type"></span>کاوه رضایی؛ بمبی که در ایران منفجر نمی‌شود!</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="تیموری: در استقلال اذیت شدم اما حرفی نزدم" href="https://www.varzesh3.com/news/1830314/تیموری-در-استقلال-اذیت-شدم-اما-حرفی-نزدم"> <span class="news-type"></span>تیموری: در استقلال اذیت شدم اما حرفی نزدم</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="قلی‌زاده و تمرین آن قیچی معروف (عکس)" href="https://www.varzesh3.com/news/1830313/قلی-زاده-و-تمرین-آن-قیچی-معروف-عکس"> <span class="news-type"></span>قلی‌زاده و تمرین آن قیچی معروف (عکس)</a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="صحبتهای ماجدی در مراسم دوره داورى فوتسال آقايان" href="https://video.varzesh3.com/video/254271/صحبتهای-ماجدی-در-مراسم-دوره-داورى-فوتسال-آقايان"> <span class="news-type"></span>صحبتهای ماجدی در مراسم دوره داورى فوتسال آقايان</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="فصل جدید لیگ برتر بدون VAR" href="https://www.varzesh3.com/news/1830312/فصل-جدید-لیگ-برتر-بدون-var"> <span class="news-type"></span>فصل جدید لیگ برتر بدون VAR</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="2"><a title="آغاز کلاس پیش فصل داوران فوتسال" href="https://www.varzesh3.com/news/1830311/آغاز-کلاس-پیش-فصل-داوران-فوتسال"> <span class="news-type"></span>آغاز کلاس پیش فصل داوران فوتسال</a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="مراسم افتتاح دوره داورى فوتسال آقايان" href="https://video.varzesh3.com/video/254270/مراسم-افتتاح-دوره-داورى-فوتسال-آقايان"> <span class="news-type"></span>مراسم افتتاح دوره داورى فوتسال آقايان</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="3"><a title="عطایی: کار سختی مقابل تیم بدون باخت مسابقات داریم" href="https://www.varzesh3.com/news/1830308/عطایی-کار-سختی-مقابل-تیم-بدون-باخت-مسابقات-داریم"> <span class="news-type"></span>عطایی: کار سختی مقابل تیم بدون باخت مسابقات داریم</a></li>
                            <li class="text-type" data-origin="2" data-media="1" data-tag="" data-sport="3"><a title="لیگ ملت‌ها؛ آمریکا قصد شکست خوردن ندارد" href="https://www.varzesh3.com/news/1830307/لیگ-ملت-ها-آمریکا-قصد-شکست-خوردن-ندارد"> <span class="news-type"></span>لیگ ملت‌ها؛ آمریکا قصد شکست خوردن ندارد</a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="صحبتهای الهامی پس از پیوستن به هوادار" href="https://video.varzesh3.com/video/254269/صحبتهای-الهامی-پس-از-پیوستن-به-هوادار"> <span class="news-type"></span>صحبتهای الهامی پس از پیوستن به هوادار</a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="بررسی مربیان موفق خارجی در فوتبال ایران" href="https://video.varzesh3.com/video/254268/بررسی-مربیان-موفق-خارجی-در-فوتبال-ایران"> <span class="news-type"></span>بررسی مربیان موفق خارجی در فوتبال ایران</a></li>
                            <li class="text-type" data-origin="3" data-media="1" data-tag="" data-sport="1"><a title="کاپیتان حاج‌صفی از یونان به قطر می‌رسد" href="https://www.varzesh3.com/news/1830306/کاپیتان-حاج-صفی-از-یونان-به-قطر-می-رسد"> <span class="news-type"></span>کاپیتان حاج‌صفی از یونان به قطر می‌رسد</a></li>
                            <li class="text-type" data-origin="2" data-media="1" data-tag="" data-sport="1"><a title="حمله تند ستاره جنجالی اینتر به زلاتان!" href="https://www.varzesh3.com/news/1830305/حمله-تند-ستاره-جنجالی-اینتر-به-زلاتان"> <span class="news-type"></span>حمله تند ستاره جنجالی اینتر به زلاتان!</a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="حواشی اولین روز حضور ساپینتو در استقلال" href="https://video.varzesh3.com/video/254267/حواشی-اولین-روز-حضور-ساپینتو-در-استقلال"> <span class="news-type"></span>حواشی اولین روز حضور ساپینتو در استقلال</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="الهامی: این فصل در هوادار دنبال آرامش هستم" href="https://www.varzesh3.com/news/1830301/الهامی-این-فصل-در-هوادار-دنبال-آرامش-هستم"> <span class="news-type"></span>الهامی: این فصل در هوادار دنبال آرامش هستم</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="رسمی؛ ساکت الهامی سرمربی هوادار شد" href="https://www.varzesh3.com/news/1830300/رسمی-ساکت-الهامی-سرمربی-هوادار-شد"> <span class="news-type"></span>رسمی؛ ساکت الهامی سرمربی هوادار شد</a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="بررسی وضعیت زاهدی و شایعه حضور در پرسپولیس" href="https://video.varzesh3.com/video/254266/بررسی-وضعیت-زاهدی-و-شایعه-حضور-در-پرسپولیس"> <span class="news-type"></span>بررسی وضعیت زاهدی و شایعه حضور در پرسپولیس</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="مجیدی در بین خارجی‌های معروف امارات (عکس)" href="https://www.varzesh3.com/news/1830299/مجیدی-در-بین-خارجی-های-معروف-امارات-عکس"> <span class="news-type"></span>مجیدی در بین خارجی‌های معروف امارات (عکس)</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="فولاد وارد بازار نقل و انتقالات شد" href="https://www.varzesh3.com/news/1830298/فولاد-وارد-بازار-نقل-و-انتقالات-شد"> <span class="news-type"></span>فولاد وارد بازار نقل و انتقالات شد</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="روز تلخ برای دو ستاره سپاهان" href="https://www.varzesh3.com/news/1830296/روز-تلخ-برای-دو-ستاره-سپاهان"> <span class="news-type"></span>روز تلخ برای دو ستاره سپاهان</a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="خلاصه والیبال صربستان 1 - آمریکا 3" href="https://video.varzesh3.com/video/254265/خلاصه-والیبال-صربستان-1-آمریکا-3"> <span class="news-type"></span>خلاصه والیبال صربستان 1 - آمریکا 3</a></li>
                            <li class="text-type" data-origin="2" data-media="1" data-tag="" data-sport="1"><a title="نفس راحت یونایتد؛ کونته، اریکسن را نخواست" href="https://www.varzesh3.com/news/1830295/نفس-راحت-یونایتد-کونته-اریکسن-را-نخواست"> <span class="news-type"></span>نفس راحت یونایتد؛ کونته، اریکسن را نخواست</a></li>
                            <li class="text-type" data-origin="2" data-media="1" data-tag="" data-sport="1"><a title="اهمیت مانه در انگلیس؛ هم‌ردیف دروگبا و یحیی توره" href="https://www.varzesh3.com/news/1830294/اهمیت-مانه-در-انگلیس-هم-ردیف-دروگبا-و-یحیی-توره"> <span class="news-type"></span>اهمیت مانه در انگلیس؛ هم‌ردیف دروگبا و یحیی توره</a></li>
                            <li class="text-type" data-origin="2" data-media="1" data-tag="" data-sport="1"><a title="مانه: تا ابد هوادار شماره یک لیورپول هستم" href="https://www.varzesh3.com/news/1830293/مانه-تا-ابد-هوادار-شماره-یک-لیورپول-هستم"> <span class="news-type"></span>مانه: تا ابد هوادار شماره یک لیورپول هستم</a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="افشاریان: قطعا در فصل آینده هم VAR نداریم" href="https://video.varzesh3.com/video/254262/افشاریان-قطعا-در-فصل-آینده-هم-var-نداریم"> <span class="news-type"></span>افشاریان: قطعا در فصل آینده هم VAR نداریم</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="گلر سابق تیم ملی در آستانه محرومیت قضایی!" href="https://www.varzesh3.com/news/1830292/گلر-سابق-تیم-ملی-در-آستانه-محرومیت-قضایی"> <span class="news-type"></span>گلر سابق تیم ملی در آستانه محرومیت قضایی!</a></li>
                            <li class="text-type" data-origin="2" data-media="1" data-tag="" data-sport="1"><a title="ناکامی دوباره میلان؛ بنفیکا هدف روسونری را دزدید" href="https://www.varzesh3.com/news/1830291/ناکامی-دوباره-میلان-بنفیکا-هدف-روسونری-را-دزدید"> <span class="news-type"></span>ناکامی دوباره میلان؛ بنفیکا هدف روسونری را دزدید</a></li>
                            <li class="text-type" data-origin="2" data-media="1" data-tag="" data-sport="1"><a title="مسی با کفش‌های نایک؟ عجیب ولی واقعی(عکس)" href="https://www.varzesh3.com/news/1830290/مسی-با-کفش-های-نایک-عجیب-ولی-واقعیعکس"> <span class="news-type"></span>مسی با کفش‌های نایک؟ عجیب ولی واقعی(عکس)</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="واکنش رسمی هوادار به خداحافظی رضا عنایتی" href="https://www.varzesh3.com/news/1830289/واکنش-رسمی-هوادار-به-خداحافظی-رضا-عنایتی"> <span class="news-type"></span>واکنش رسمی هوادار به خداحافظی رضا عنایتی</a></li>
                            <li class="text-type" data-origin="2" data-media="1" data-tag="" data-sport="1"><a title="ادعای خسارت علیه بوگاتی رونالدو؛ پولم را بدهند" href="https://www.varzesh3.com/news/1830288/ادعای-خسارت-علیه-بوگاتی-رونالدو-پولم-را-بدهند"> <span class="news-type"></span>ادعای خسارت علیه بوگاتی رونالدو؛ پولم را بدهند</a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="فازمتر: فروش فالوور تضمینی فقط با یک قرارداد" href="https://video.varzesh3.com/video/254261/فازمتر-فروش-فالوور-تضمینی-فقط-با-یک-قرارداد"> <span class="news-type"></span>فازمتر: فروش فالوور تضمینی فقط با یک قرارداد</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="مدیرعامل جدید باشگاه هوادار معرفی شد" href="https://www.varzesh3.com/news/1830287/مدیرعامل-جدید-باشگاه-هوادار-معرفی-شد"> <span class="news-type"></span>مدیرعامل جدید باشگاه هوادار معرفی شد</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="خداداد و سوپرایز جشن تولد 51 سالگی" href="https://www.varzesh3.com/news/1830285/خداداد-و-سوپرایز-جشن-تولد-51-سالگی"> <span class="news-type"></span>خداداد و سوپرایز جشن تولد 51 سالگی</a></li>
                            <li class="text-type" data-origin="2" data-media="1" data-tag="" data-sport="1"><a title="خداحافظی صلاح با مانه؛ دل‌مان برایت تنگ می‌شود" href="https://www.varzesh3.com/news/1830283/خداحافظی-صلاح-با-مانه-دل-مان-برایت-تنگ-می-شود"> <span class="news-type"></span>خداحافظی صلاح با مانه؛ دل‌مان برایت تنگ می‌شود</a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="خلاصه والیبال برزیل 1 - لهستان 3" href="https://video.varzesh3.com/video/254260/خلاصه-والیبال-برزیل-1-لهستان-3"> <span class="news-type"></span>خلاصه والیبال برزیل 1 - لهستان 3</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="نائیج‌‌پور، قلی‌زاده و بارانی حریف می‌طلبند!" href="https://www.varzesh3.com/news/1830284/نائیج-پور-قلی-زاده-و-بارانی-حریف-می-طلبند"> <span class="news-type"></span>نائیج‌‌پور، قلی‌زاده و بارانی حریف می‌طلبند!</a></li>
                            <li class="text-type" data-origin="2" data-media="1" data-tag="" data-sport="1"><a title="گاف اسکای‌نیوز در بدو ورود سادیو مانه(عکس)" href="https://www.varzesh3.com/news/1830282/گاف-اسکای-نیوز-در-بدو-ورود-سادیو-مانهعکس"> <span class="news-type"></span>گاف اسکای‌نیوز در بدو ورود سادیو مانه(عکس)</a></li>
                            <li class="text-type" data-origin="2" data-media="1" data-tag="" data-sport="1"><a title="خداحافظی بعدی در چلسی؛ پتر چک هم می‌رود؟" href="https://www.varzesh3.com/news/1830280/خداحافظی-بعدی-در-چلسی-پتر-چک-هم-می-رود"> <span class="news-type"></span>خداحافظی بعدی در چلسی؛ پتر چک هم می‌رود؟</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="3"><a title="لیگ ملت‌های والیبال؛ لهستان فاتح دوئل بزرگ" href="https://www.varzesh3.com/news/1830281/لیگ-ملت-های-والیبال-لهستان-فاتح-دوئل-بزرگ"> <span class="news-type"></span>لیگ ملت‌های والیبال؛ لهستان فاتح دوئل بزرگ</a></li>
                            <li class="text-type" data-origin="2" data-media="1" data-tag="" data-sport="1"><a title="اخراجی‌های یونایتد مشخص شد؛ لیست پنج‌نفره" href="https://www.varzesh3.com/news/1830277/اخراجی-های-یونایتد-مشخص-شد-لیست-پنج-نفره"> <span class="news-type"></span>اخراجی‌های یونایتد مشخص شد؛ لیست پنج‌نفره</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="سیاست تراکتور؛ بازیکن خارجی و ملی‌پوش امید!" href="https://www.varzesh3.com/news/1830279/سیاست-تراکتور-بازیکن-خارجی-و-ملی-پوش-امید"> <span class="news-type"></span>سیاست تراکتور؛ بازیکن خارجی و ملی‌پوش امید!</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="رضاوند:‌ بازیکن استقلالم، منتظر تصمیم باشگاه هستم" href="https://www.varzesh3.com/news/1830278/رضاوند-بازیکن-استقلالم-منتظر-تصمیم-باشگاه-هستم"> <span class="news-type"></span>رضاوند:‌ بازیکن استقلالم، منتظر تصمیم باشگاه هستم</a></li>
                            <li class="text-type" data-origin="2" data-media="1" data-tag="" data-sport="1"><a title="با جدایی بانوی پرقدرت؛ اقتدار حداکثری توخل در چلسی" href="https://www.varzesh3.com/news/1830272/با-جدایی-بانوی-پرقدرت-اقتدار-حداکثری-توخل-در-چلسی"> <span class="news-type"></span>با جدایی بانوی پرقدرت؛ اقتدار حداکثری توخل در چلسی</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="شریفات به‌زودی با آلومینیوم تمدید می‌کند" href="https://www.varzesh3.com/news/1830276/شریفات-به-زودی-با-آلومینیوم-تمدید-می-کند"> <span class="news-type"></span>شریفات به‌زودی با آلومینیوم تمدید می‌کند</a></li>
                            <li class="text-type" data-origin="2" data-media="1" data-tag="" data-sport="1"><a title="هافبک لیورپول درخواست جدایی داد" href="https://www.varzesh3.com/news/1830275/هافبک-لیورپول-درخواست-جدایی-داد"> <span class="news-type"></span>هافبک لیورپول درخواست جدایی داد</a></li>
                            <li class="text-type" data-origin="2" data-media="1" data-tag="" data-sport="1"><a title="کاوانی خودش را پیشنهاد داد؛ همبازی فالکائو می‌شوم" href="https://www.varzesh3.com/news/1830270/کاوانی-خودش-را-پیشنهاد-داد-همبازی-فالکائو-می-شوم"> <span class="news-type"></span>کاوانی خودش را پیشنهاد داد؛ همبازی فالکائو می‌شوم</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="وریا: ای‌کاش یک تماس ۳۰ ثانیه‌ای می‌گرفتند" href="https://www.varzesh3.com/news/1830273/وریا-ای-کاش-یک-تماس-۳۰-ثانیه-ای-می-گرفتند"> <span class="news-type"></span>وریا: ای‌کاش یک تماس ۳۰ ثانیه‌ای می‌گرفتند</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="کریم‌زاده: از پرسپولیس جا ماندیم ولی آجرلو جبران می‌کند!" href="https://www.varzesh3.com/news/1830271/کریم-زاده-از-پرسپولیس-جا-ماندیم-ولی-آجرلو-جبران-می-کند"> <span class="news-type"></span>کریم‌زاده: از پرسپولیس جا ماندیم ولی آجرلو جبران می‌کند!</a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="تنیس فوتبال یاران قلی زاده مقابل یاران غفوری" href="https://video.varzesh3.com/video/254254/تنیس-فوتبال-یاران-قلی-زاده-مقابل-یاران-غفوری"> <span class="news-type"></span>تنیس فوتبال یاران قلی زاده مقابل یاران غفوری</a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="*امیدوارم مانند کاپیتان های سابق استقلال جدا نشوم" href="https://video.varzesh3.com/video/254251/امیدوارم-مانند-کاپیتان-های-سابق-استقلال-جدا-نشوم"> <span class="news-type"></span>*امیدوارم مانند کاپیتان های سابق استقلال جدا نشوم</a></li>
                            <li class="text-type" data-origin="2" data-media="1" data-tag="" data-sport="1"><a title="شوک تابستان امسال؛ گرت بیل در چمپیونشیپ؟" href="https://www.varzesh3.com/news/1830267/شوک-تابستان-امسال-گرت-بیل-در-چمپیونشیپ"> <span class="news-type"></span>شوک تابستان امسال؛ گرت بیل در چمپیونشیپ؟</a></li>
                            <li class="text-type" data-origin="2" data-media="1" data-tag="" data-sport="1"><a title="اولیور کان: لواندوفسکی را در تمرینات می‌بینیم" href="https://www.varzesh3.com/news/1830269/اولیور-کان-لواندوفسکی-را-در-تمرینات-می-بینیم"> <span class="news-type"></span>اولیور کان: لواندوفسکی را در تمرینات می‌بینیم</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="قلی‌زاده: گروه ایران سخت‌ترین گروه جام است" href="https://www.varzesh3.com/news/1830268/قلی-زاده-گروه-ایران-سخت-ترین-گروه-جام-است"> <span class="news-type"></span>قلی‌زاده: گروه ایران سخت‌ترین گروه جام است</a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="قلی زاده: در جام جهانی باشم، قیچی می زنم!" href="https://video.varzesh3.com/video/254250/قلی-زاده-در-جام-جهانی-باشم-قیچی-می-زنم"> <span class="news-type"></span>قلی زاده: در جام جهانی باشم، قیچی می زنم!</a></li>
                            <li class="text-type" data-origin="2" data-media="1" data-tag="" data-sport="1"><a title="همه تاریخ‌های مهم برای فصل آینده لالیگا " href="https://www.varzesh3.com/news/1830265/همه-تاریخ-های-مهم-برای-فصل-آینده-لالیگا"> <span class="news-type"></span>همه تاریخ‌های مهم برای فصل آینده لالیگا </a></li>
                            <li class="text-type" data-origin="2" data-media="1" data-tag="" data-sport="1"><a title="حرف‌های جذاب ستاره جدید بایرن‌ در اولین نشست" href="https://www.varzesh3.com/news/1830262/حرف-های-جذاب-ستاره-جدید-بایرن-در-اولین-نشست"> <span class="news-type"></span>حرف‌های جذاب ستاره جدید بایرن‌ در اولین نشست</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="3"><a title="رونمایی از لیست ۱۶ نفره تیم ملی والیبال نوجوانان" href="https://www.varzesh3.com/news/1830266/رونمایی-از-لیست-۱۶-نفره-تیم-ملی-والیبال-نوجوانان"> <span class="news-type"></span>رونمایی از لیست ۱۶ نفره تیم ملی والیبال نوجوانان</a></li>
                            <li class="text-type" data-origin="2" data-media="1" data-tag="" data-sport="1"><a title="تنها حامی دمبله در بارسا؛ ژاوی هرناندز" href="https://www.varzesh3.com/news/1830260/تنها-حامی-دمبله-در-بارسا-ژاوی-هرناندز"> <span class="news-type"></span>تنها حامی دمبله در بارسا؛ ژاوی هرناندز</a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="مراسم معارفه سرمربی پرتغالی جدید استقلال" href="https://video.varzesh3.com/video/254249/مراسم-معارفه-سرمربی-پرتغالی-جدید-استقلال"> <span class="news-type"></span>مراسم معارفه سرمربی پرتغالی جدید استقلال</a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="آخرین وضعیت ورزشگاه نیمه تمام ثامن مشهد" href="https://video.varzesh3.com/video/254248/آخرین-وضعیت-ورزشگاه-نیمه-تمام-ثامن-مشهد"> <span class="news-type"></span>آخرین وضعیت ورزشگاه نیمه تمام ثامن مشهد</a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="اخبار نقل و انتقالات فوتبال جهان (1 تیرماه 1401)" href="https://video.varzesh3.com/video/254247/اخبار-نقل-و-انتقالات-فوتبال-جهان-1-تیرماه-1401"> <span class="news-type"></span>اخبار نقل و انتقالات فوتبال جهان (1 تیرماه 1401)</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="جملاتی که مرد پرتغالی را محبوب‌تر کرد!" href="https://www.varzesh3.com/news/1830261/جملاتی-که-مرد-پرتغالی-را-محبوب-تر-کرد"> <span class="news-type"></span>جملاتی که مرد پرتغالی را محبوب‌تر کرد!</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="منوچهری: لطفا به تصمیمات آجورلو احترام بگذارید" href="https://www.varzesh3.com/news/1830259/منوچهری-لطفا-به-تصمیمات-آجورلو-احترام-بگذارید"> <span class="news-type"></span>منوچهری: لطفا به تصمیمات آجورلو احترام بگذارید</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="اکبرپور: با ساپینتو قهرمانی را حفظ می‌کنیم" href="https://www.varzesh3.com/news/1830258/اکبرپور-با-ساپینتو-قهرمانی-را-حفظ-می-کنیم"> <span class="news-type"></span>اکبرپور: با ساپینتو قهرمانی را حفظ می‌کنیم</a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="کلیپ جالب خوشامدگویی بوندسلیگا به سادیو مانه" href="https://video.varzesh3.com/video/254246/کلیپ-جالب-خوشامدگویی-بوندسلیگا-به-سادیو-مانه"> <span class="news-type"></span>کلیپ جالب خوشامدگویی بوندسلیگا به سادیو مانه</a></li>
                            <li class="text-type" data-origin="2" data-media="1" data-tag="" data-sport="1"><a title="رسمی؛ قرارداد سرمربی موفق فیورنتینا تمدید شد" href="https://www.varzesh3.com/news/1830257/رسمی-قرارداد-سرمربی-موفق-فیورنتینا-تمدید-شد"> <span class="news-type"></span>رسمی؛ قرارداد سرمربی موفق فیورنتینا تمدید شد</a></li>
                            <li class="text-type" data-origin="2" data-media="1" data-tag="" data-sport="1"><a title="رئیس لالیگا: الخلیفی همه ما را احمق فرض کرده" href="https://www.varzesh3.com/news/1830255/رئیس-لالیگا-الخلیفی-همه-ما-را-احمق-فرض-کرده"> <span class="news-type"></span>رئیس لالیگا: الخلیفی همه ما را احمق فرض کرده</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="3"><a title="اسماعیل‌نژاد: امیدوارم فردا مردم را خوشحال کنیم" href="https://www.varzesh3.com/news/1830256/اسماعیل-نژاد-امیدوارم-فردا-مردم-را-خوشحال-کنیم"> <span class="news-type"></span>اسماعیل‌نژاد: امیدوارم فردا مردم را خوشحال کنیم</a></li>
                            <li class="text-type" data-origin="2" data-media="1" data-tag="" data-sport="1"><a title="لیورپول برای جذب ستاره اینتر هر کاری می‌کند" href="https://www.varzesh3.com/news/1830254/لیورپول-برای-جذب-ستاره-اینتر-هر-کاری-می-کند"> <span class="news-type"></span>لیورپول برای جذب ستاره اینتر هر کاری می‌کند</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="کاسیانو - پرسپولیس؛ این هفته مشخص می‌شود" href="https://www.varzesh3.com/news/1830243/کاسیانو-پرسپولیس-این-هفته-مشخص-می-شود"> <span class="news-type"></span>کاسیانو - پرسپولیس؛ این هفته مشخص می‌شود</a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="خلاصه والیبال آلمان 0 - ایتالیا 3" href="https://video.varzesh3.com/video/254245/خلاصه-والیبال-آلمان-0-ایتالیا-3"> <span class="news-type"></span>خلاصه والیبال آلمان 0 - ایتالیا 3</a></li>
                            <li class="text-type" data-origin="2" data-media="1" data-tag="" data-sport="1"><a title="سنگ بزرگ سیتی؛ ستاره پرتغالی از بارسا دور شد؟" href="https://www.varzesh3.com/news/1830200/سنگ-بزرگ-سیتی-ستاره-پرتغالی-از-بارسا-دور-شد"> <span class="news-type"></span>سنگ بزرگ سیتی؛ ستاره پرتغالی از بارسا دور شد؟</a></li>
                            <li class="text-type" data-origin="2" data-media="1" data-tag="" data-sport="1"><a title="بارسلونا زیر حرفش زد؛ ستاره هلندی می‌ماند؟" href="https://www.varzesh3.com/news/1830242/بارسلونا-زیر-حرفش-زد-ستاره-هلندی-می-ماند"> <span class="news-type"></span>بارسلونا زیر حرفش زد؛ ستاره هلندی می‌ماند؟</a></li>
                            <li class="text-type" data-origin="2" data-media="1" data-tag="" data-sport="1"><a title="باشگاه پرطرفدار فرانسوی برای نجات بارسا می‌آید" href="https://www.varzesh3.com/news/1830201/باشگاه-پرطرفدار-فرانسوی-برای-نجات-بارسا-می-آید"> <span class="news-type"></span>باشگاه پرطرفدار فرانسوی برای نجات بارسا می‌آید</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="وعده جذاب آجورلو؛ ساخت استادیوم اختصاصی استقلال" href="https://www.varzesh3.com/news/1830241/وعده-جذاب-آجورلو-ساخت-استادیوم-اختصاصی-استقلال"> <span class="news-type"></span>وعده جذاب آجورلو؛ ساخت استادیوم اختصاصی استقلال</a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="لحظه امضای قرارداد تامین کننده البسه باشگاه استقلال" href="https://video.varzesh3.com/video/254244/لحظه-امضای-قرارداد-تامین-کننده-البسه-باشگاه-استقلال"> <span class="news-type"></span>لحظه امضای قرارداد تامین کننده البسه باشگاه استقلال</a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="لحظه امضای قرارداد استادیوم اختصاصی استقلال" href="https://video.varzesh3.com/video/254243/لحظه-امضای-قرارداد-استادیوم-اختصاصی-استقلال"> <span class="news-type"></span>لحظه امضای قرارداد استادیوم اختصاصی استقلال</a></li>
                            <li class="text-type" data-origin="2" data-media="1" data-tag="" data-sport="1"><a title="هشدار طعنه‌آمیز اینتری‌ها به ستاره جدید؛ خیانت‌کار!" href="https://www.varzesh3.com/news/1830239/هشدار-طعنه-آمیز-اینتری-ها-به-ستاره-جدید-خیانت-کار"> <span class="news-type"></span>هشدار طعنه‌آمیز اینتری‌ها به ستاره جدید؛ خیانت‌کار!</a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="آجرلو: در حال تدارک برای ساخت استادیوم اختصاصی هستیم" href="https://video.varzesh3.com/video/254242/آجرلو-در-حال-تدارک-برای-ساخت-استادیوم-اختصاصی-هستیم"> <span class="news-type"></span>آجرلو: در حال تدارک برای ساخت استادیوم اختصاصی هستیم</a></li>
                            <li class="text-type" data-origin="2" data-media="1" data-tag="" data-sport="1"><a title="آقای لواندوفسکی، در اولین تمرین بایرن می‌بینمت" href="https://www.varzesh3.com/news/1830240/آقای-لواندوفسکی-در-اولین-تمرین-بایرن-می-بینمت"> <span class="news-type"></span>آقای لواندوفسکی، در اولین تمرین بایرن می‌بینمت</a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="ریکاردو ساپینتو: فقط برای قهرمانی خواهیم جنگید" href="https://video.varzesh3.com/video/254241/ریکاردو-ساپینتو-فقط-برای-قهرمانی-خواهیم-جنگید"> <span class="news-type"></span>ریکاردو ساپینتو: فقط برای قهرمانی خواهیم جنگید</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="یادداشت مهدی شیری برای هادی نوروزی (عکس)" href="https://www.varzesh3.com/news/1830237/یادداشت-مهدی-شیری-برای-هادی-نوروزی-عکس"> <span class="news-type"></span>یادداشت مهدی شیری برای هادی نوروزی (عکس)</a></li>
                            <li class="text-type" data-origin="2" data-media="1" data-tag="" data-sport="1"><a title="امیدوارم تیمم نصف کیفیت تیم کونته را ارائه دهد!" href="https://www.varzesh3.com/news/1830236/امیدوارم-تیمم-نصف-کیفیت-تیم-کونته-را-ارائه-دهد"> <span class="news-type"></span>امیدوارم تیمم نصف کیفیت تیم کونته را ارائه دهد!</a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="آجورلو: حق استقلال را از صداوسیما خواهم گرفت" href="https://video.varzesh3.com/video/254240/آجورلو-حق-استقلال-را-از-صداوسیما-خواهم-گرفت"> <span class="news-type"></span>آجورلو: حق استقلال را از صداوسیما خواهم گرفت</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="ساپینتو: می‌خواهم 4 قهرمانی با استقلال بیاورم" href="https://www.varzesh3.com/news/1830233/ساپینتو-می-خواهم-4-قهرمانی-با-استقلال-بیاورم"> <span class="news-type"></span>ساپینتو: می‌خواهم 4 قهرمانی با استقلال بیاورم</a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="آجورلو: شبکه استقلال به صورت‌آزمایشی شروع‌به‌کار خواهدکرد" href="https://video.varzesh3.com/video/254239/آجورلو-شبکه-استقلال-به-صورت-آزمایشی-شروع-به-کار-خواهدکرد"> <span class="news-type"></span>آجورلو: شبکه استقلال به صورت‌آزمایشی شروع‌به‌کار خواهدکرد</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="گل گهر یک سال دیگر با همین مثلث دروازه‌بانی" href="https://www.varzesh3.com/news/1830235/گل-گهر-یک-سال-دیگر-با-همین-مثلث-دروازه-بانی"> <span class="news-type"></span>گل گهر یک سال دیگر با همین مثلث دروازه‌بانی</a></li>
                            <li class="text-type" data-origin="2" data-media="1" data-tag="" data-sport="1"><a title="ضرر بارسلونا از جدایی قدرتمندترین بانوی فوتبال دنیا" href="https://www.varzesh3.com/news/1830234/ضرر-بارسلونا-از-جدایی-قدرتمندترین-بانوی-فوتبال-دنیا"> <span class="news-type"></span>ضرر بارسلونا از جدایی قدرتمندترین بانوی فوتبال دنیا</a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="اهدای شال باشگاه استقلال از سوی آجورلو به ساپینتو" href="https://video.varzesh3.com/video/254238/اهدای-شال-باشگاه-استقلال-از-سوی-آجورلو-به-ساپینتو"> <span class="news-type"></span>اهدای شال باشگاه استقلال از سوی آجورلو به ساپینتو</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="شال استقلال روی دست سرمربی پرتغالی (عکس)" href="https://www.varzesh3.com/news/1830232/شال-استقلال-روی-دست-سرمربی-پرتغالی-عکس"> <span class="news-type"></span>شال استقلال روی دست سرمربی پرتغالی (عکس)</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="شبکه تلویزیونی استقلال آغاز به کار کرد" href="https://www.varzesh3.com/news/1830231/شبکه-تلویزیونی-استقلال-آغاز-به-کار-کرد"> <span class="news-type"></span>شبکه تلویزیونی استقلال آغاز به کار کرد</a></li>
                            <li class="text-type" data-origin="2" data-media="1" data-tag="" data-sport="1"><a title="اعتراف کلوپ: یکی از بهترین‌های جهان از لیورپول رفت" href="https://www.varzesh3.com/news/1830230/اعتراف-کلوپ-یکی-از-بهترین-های-جهان-از-لیورپول-رفت"> <span class="news-type"></span>اعتراف کلوپ: یکی از بهترین‌های جهان از لیورپول رفت</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="تراکتور دوباره به دنبال جذب ملی‌پوش" href="https://www.varzesh3.com/news/1830229/تراکتور-دوباره-به-دنبال-جذب-ملی-پوش"> <span class="news-type"></span>تراکتور دوباره به دنبال جذب ملی‌پوش</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="تارتار آقای گل‌های لیگ یک را دوست دارد!" href="https://www.varzesh3.com/news/1830228/تارتار-آقای-گل-های-لیگ-یک-را-دوست-دارد"> <span class="news-type"></span>تارتار آقای گل‌های لیگ یک را دوست دارد!</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="آجورلو: ریکاردو گفت تشنه قهرمانی است" href="https://www.varzesh3.com/news/1830227/آجورلو-ریکاردو-گفت-تشنه-قهرمانی-است"> <span class="news-type"></span>آجورلو: ریکاردو گفت تشنه قهرمانی است</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="بازگشت میلاد محمدی به کمپ تیم‌های ملی" href="https://www.varzesh3.com/news/1830226/بازگشت-میلاد-محمدی-به-کمپ-تیم-های-ملی"> <span class="news-type"></span>بازگشت میلاد محمدی به کمپ تیم‌های ملی</a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="لحظه امضای قرارداد ساپینتو با باشگاه استقلال" href="https://video.varzesh3.com/video/254237/لحظه-امضای-قرارداد-ساپینتو-با-باشگاه-استقلال"> <span class="news-type"></span>لحظه امضای قرارداد ساپینتو با باشگاه استقلال</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="قرارداد ساپینتو با استقلال امضا شد" href="https://www.varzesh3.com/news/1830225/قرارداد-ساپینتو-با-استقلال-امضا-شد"> <span class="news-type"></span>قرارداد ساپینتو با استقلال امضا شد</a></li>
                            <li class="text-type" data-origin="2" data-media="1" data-tag="" data-sport="1"><a title="کواچیچ گفت به رئال برو؛ رونالدو غافلگیرم کرد" href="https://www.varzesh3.com/news/1830224/کواچیچ-گفت-به-رئال-برو-رونالدو-غافلگیرم-کرد"> <span class="news-type"></span>کواچیچ گفت به رئال برو؛ رونالدو غافلگیرم کرد</a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="پخش سرود ملی ایران در ابتدای نشست معارفه ساپینتو" href="https://video.varzesh3.com/video/254236/پخش-سرود-ملی-ایران-در-ابتدای-نشست-معارفه-ساپینتو"> <span class="news-type"></span>پخش سرود ملی ایران در ابتدای نشست معارفه ساپینتو</a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="ورود ساپینتو سرمربی باشگاه استقلال در نشست معارفه" href="https://video.varzesh3.com/video/254235/ورود-ساپینتو-سرمربی-باشگاه-استقلال-در-نشست-معارفه"> <span class="news-type"></span>ورود ساپینتو سرمربی باشگاه استقلال در نشست معارفه</a></li>
                            <li class="text-type" data-origin="2" data-media="1" data-tag="" data-sport="1"><a title="میلان مقصد یاغی فوتبال ایتالیاست یا اینتر؟" href="https://www.varzesh3.com/news/1830223/میلان-مقصد-یاغی-فوتبال-ایتالیاست-یا-اینتر"> <span class="news-type"></span>میلان مقصد یاغی فوتبال ایتالیاست یا اینتر؟</a></li>
                            <li class="text-type" data-origin="2" data-media="1" data-tag="" data-sport="1"><a title="پس از پیشنهاد رم؛ آقای آنچلوتی، باید صحبت کنیم" href="https://www.varzesh3.com/news/1830199/پس-از-پیشنهاد-رم-آقای-آنچلوتی-باید-صحبت-کنیم"> <span class="news-type"></span>پس از پیشنهاد رم؛ آقای آنچلوتی، باید صحبت کنیم</a></li>
                            <li class="text-type" data-origin="2" data-media="1" data-tag="" data-sport="1"><a title="ستاره رئال مادرید با بارسلونا تمام کرده بود " href="https://www.varzesh3.com/news/1830222/ستاره-رئال-مادرید-با-بارسلونا-تمام-کرده-بود"> <span class="news-type"></span>ستاره رئال مادرید با بارسلونا تمام کرده بود </a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="پاسخ بیژن طاهری به ادامه همکاری با استقلال" href="https://www.varzesh3.com/news/1830221/پاسخ-بیژن-طاهری-به-ادامه-همکاری-با-استقلال"> <span class="news-type"></span>پاسخ بیژن طاهری به ادامه همکاری با استقلال</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="مهدوی‌کیا: آمریکا تیم جوان و قدرتمندی دارد" href="https://www.varzesh3.com/news/1830220/مهدوی-کیا-آمریکا-تیم-جوان-و-قدرتمندی-دارد"> <span class="news-type"></span>مهدوی‌کیا: آمریکا تیم جوان و قدرتمندی دارد</a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="حضور برهانی در مراسم معارفه سرمربی جدید استقلال" href="https://video.varzesh3.com/video/254234/حضور-برهانی-در-مراسم-معارفه-سرمربی-جدید-استقلال"> <span class="news-type"></span>حضور برهانی در مراسم معارفه سرمربی جدید استقلال</a></li>
                            <li class="text-type" data-origin="2" data-media="1" data-tag="" data-sport="1"><a title="انتقال هیولای گلزنی آژاکس به دورتموند قطعی شد" href="https://www.varzesh3.com/news/1830218/انتقال-هیولای-گلزنی-آژاکس-به-دورتموند-قطعی-شد"> <span class="news-type"></span>انتقال هیولای گلزنی آژاکس به دورتموند قطعی شد</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="جشن تولد خداداد عزیزی با چند قطره اشک" href="https://www.varzesh3.com/news/1830217/جشن-تولد-خداداد-عزیزی-با-چند-قطره-اشک"> <span class="news-type"></span>جشن تولد خداداد عزیزی با چند قطره اشک</a></li>
                            <li class="text-type" data-origin="2" data-media="1" data-tag="" data-sport="1"><a title="سادیو مانه: هیچ تردیدی در مورد بایرن مونیخ نداشتم" href="https://www.varzesh3.com/news/1830219/سادیو-مانه-هیچ-تردیدی-در-مورد-بایرن-مونیخ-نداشتم"> <span class="news-type"></span>سادیو مانه: هیچ تردیدی در مورد بایرن مونیخ نداشتم</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="مدافع فصل پیش ذوب‌آهن شاگرد حسینی شد (عکس)" href="https://www.varzesh3.com/news/1830216/مدافع-فصل-پیش-ذوب-آهن-شاگرد-حسینی-شد-عکس"> <span class="news-type"></span>مدافع فصل پیش ذوب‌آهن شاگرد حسینی شد (عکس)</a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="مظلومی : سرمربی جدید مبارک هواداران باشد" href="https://video.varzesh3.com/video/254233/مظلومی-سرمربی-جدید-مبارک-هواداران-باشد"> <span class="news-type"></span>مظلومی : سرمربی جدید مبارک هواداران باشد</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="بیانیه پرسپولیس درباره مدرسه فوتبال جعلی پرسپولیس!" href="https://www.varzesh3.com/news/1830215/بیانیه-پرسپولیس-درباره-مدرسه-فوتبال-جعلی-پرسپولیس"> <span class="news-type"></span>بیانیه پرسپولیس درباره مدرسه فوتبال جعلی پرسپولیس!</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="متوسط سنی پرسپولیس در آستانه سی سالگی!" href="https://www.varzesh3.com/news/1830214/متوسط-سنی-پرسپولیس-در-آستانه-سی-سالگی"> <span class="news-type"></span>متوسط سنی پرسپولیس در آستانه سی سالگی!</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="سرمربی استقلال به پرتغال برمی‌گردد" href="https://www.varzesh3.com/news/1830213/سرمربی-استقلال-به-پرتغال-برمی-گردد"> <span class="news-type"></span>سرمربی استقلال به پرتغال برمی‌گردد</a></li>
                            <li class="text-type" data-origin="2" data-media="1" data-tag="" data-sport="1"><a title="رسمی؛ سادیو مانه به بایرن مونیخ پیوست" href="https://www.varzesh3.com/news/1830212/رسمی-سادیو-مانه-به-بایرن-مونیخ-پیوست"> <span class="news-type"></span>رسمی؛ سادیو مانه به بایرن مونیخ پیوست</a></li>
                            <li class="text-type" data-origin="2" data-media="1" data-tag="" data-sport="1"><a title="ورزشگاه یک میلیون نفری؛ تخیل یا واقعیت؟ (عکس)" href="https://www.varzesh3.com/news/1830208/ورزشگاه-یک-میلیون-نفری-تخیل-یا-واقعیت-عکس"> <span class="news-type"></span>ورزشگاه یک میلیون نفری؛ تخیل یا واقعیت؟ (عکس)</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="محسن مسلمان و شروعی دوباره در فوتبال ایران" href="https://www.varzesh3.com/news/1830211/محسن-مسلمان-و-شروعی-دوباره-در-فوتبال-ایران"> <span class="news-type"></span>محسن مسلمان و شروعی دوباره در فوتبال ایران</a></li>
                            <li class="text-type" data-origin="2" data-media="1" data-tag="" data-sport="1"><a title="الهلال فردا قهرمان لیگ عربستان می‌شود؟" href="https://www.varzesh3.com/news/1830210/الهلال-فردا-قهرمان-لیگ-عربستان-می-شود"> <span class="news-type"></span>الهلال فردا قهرمان لیگ عربستان می‌شود؟</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="3"><a title="اولین واکنش داورزنی به نتایج ناامیدکننده تیم‌ملی" href="https://www.varzesh3.com/news/1830209/اولین-واکنش-داورزنی-به-نتایج-ناامیدکننده-تیم-ملی"> <span class="news-type"></span>اولین واکنش داورزنی به نتایج ناامیدکننده تیم‌ملی</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="منشا و بازارگرمی به سبک همه آقای گل‌ها" href="https://www.varzesh3.com/news/1830207/منشا-و-بازارگرمی-به-سبک-همه-آقای-گل-ها"> <span class="news-type"></span>منشا و بازارگرمی به سبک همه آقای گل‌ها</a></li>
                            <li class="text-type" data-origin="2" data-media="1" data-tag="" data-sport="1"><a title="کی‌روش: به تیم ملی مصر برنمی‌گردم" href="https://www.varzesh3.com/news/1830206/کی-روش-به-تیم-ملی-مصر-برنمی-گردم"> <span class="news-type"></span>کی‌روش: به تیم ملی مصر برنمی‌گردم</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="تقدیر از مربی نوراللهی و قایدی (عکس)" href="https://www.varzesh3.com/news/1830205/تقدیر-از-مربی-نوراللهی-و-قایدی-عکس"> <span class="news-type"></span>تقدیر از مربی نوراللهی و قایدی (عکس)</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="مبهم‌ترین مقصد برای کدام ستاره فوتبال ایران است؟" href="https://www.varzesh3.com/news/1830204/مبهم-ترین-مقصد-برای-کدام-ستاره-فوتبال-ایران-است"> <span class="news-type"></span>مبهم‌ترین مقصد برای کدام ستاره فوتبال ایران است؟</a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="برد خاطر انگیز ایران مقابل مراکش در جام جهانی" href="https://video.varzesh3.com/video/254232/برد-خاطر-انگیز-ایران-مقابل-مراکش-در-جام-جهانی"> <span class="news-type"></span>برد خاطر انگیز ایران مقابل مراکش در جام جهانی</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="فریبا: دلیلی برای قهرمان نشدن استقلال وجود ندارد" href="https://www.varzesh3.com/news/1830203/فریبا-دلیلی-برای-قهرمان-نشدن-استقلال-وجود-ندارد"> <span class="news-type"></span>فریبا: دلیلی برای قهرمان نشدن استقلال وجود ندارد</a></li>
                            <li class="text-type" data-origin="2" data-media="1" data-tag="" data-sport="1"><a title="صفر تا صد انتقال مانه به بایرن از زبان صالح‌حمیدزیچ" href="https://www.varzesh3.com/news/1830197/صفر-تا-صد-انتقال-مانه-به-بایرن-از-زبان-صالح-حمیدزیچ"> <span class="news-type"></span>صفر تا صد انتقال مانه به بایرن از زبان صالح‌حمیدزیچ</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="پرسپولیس قرارداد با پدیده استقلال را تکذیب کرد" href="https://www.varzesh3.com/news/1830198/پرسپولیس-قرارداد-با-پدیده-استقلال-را-تکذیب-کرد"> <span class="news-type"></span>پرسپولیس قرارداد با پدیده استقلال را تکذیب کرد</a></li>
                            <li class="text-type" data-origin="2" data-media="1" data-tag="" data-sport="1"><a title="طعنه ناصر به رئال؛ 7 روز قهرمانی‌ را جشن گرفتند ولی..." href="https://www.varzesh3.com/news/1830202/طعنه-ناصر-به-رئال-7-روز-قهرمانی-را-جشن-گرفتند-ولی"> <span class="news-type"></span>طعنه ناصر به رئال؛ 7 روز قهرمانی‌ را جشن گرفتند ولی...</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="قلعه‌نویی و کنترل از راه دور گل‌گهر لیگ بیست و دو" href="https://www.varzesh3.com/news/1830196/قلعه-نویی-و-کنترل-از-راه-دور-گل-گهر-لیگ-بیست-و-دو"> <span class="news-type"></span>قلعه‌نویی و کنترل از راه دور گل‌گهر لیگ بیست و دو</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="لیست خریدهای خارجی‌ تراکتور دگرگون شد" href="https://www.varzesh3.com/news/1830194/لیست-خریدهای-خارجی-تراکتور-دگرگون-شد"> <span class="news-type"></span>لیست خریدهای خارجی‌ تراکتور دگرگون شد</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="اشکان دژاگه؛ چهره غیرقابل گذشت فصل نقل‌و‌انتقالات" href="https://www.varzesh3.com/news/1830192/اشکان-دژاگه-چهره-غیرقابل-گذشت-فصل-نقل-و-انتقالات"> <span class="news-type"></span>اشکان دژاگه؛ چهره غیرقابل گذشت فصل نقل‌و‌انتقالات</a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="مرور تمام گلهای آرسنال در فصل 22-2021" href="https://video.varzesh3.com/video/252375/مرور-تمام-گلهای-آرسنال-در-فصل-22-2021"> <span class="news-type"></span>مرور تمام گلهای آرسنال در فصل 22-2021</a></li>
                            <li class="text-type" data-origin="2" data-media="1" data-tag="" data-sport="1"><a title="وعده‌های پوچ لاپورتا؛ نه لواندوفسکی می‌آید، نه هیچکس" href="https://www.varzesh3.com/news/1830193/وعده-های-پوچ-لاپورتا-نه-لواندوفسکی-می-آید-نه-هیچکس"> <span class="news-type"></span>وعده‌های پوچ لاپورتا؛ نه لواندوفسکی می‌آید، نه هیچکس</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="این لژیونر به همه درخواست‌ها پاسخ منفی می‌دهد" href="https://www.varzesh3.com/news/1830191/این-لژیونر-به-همه-درخواست-ها-پاسخ-منفی-می-دهد"> <span class="news-type"></span>این لژیونر به همه درخواست‌ها پاسخ منفی می‌دهد</a></li>
                            <li class="text-type" data-origin="2" data-media="1" data-tag="" data-sport="1"><a title="لینِکِر: به من هم توهین‌های نژادپرستانه می‌کردند" href="https://www.varzesh3.com/news/1830195/لینِکِر-به-من-هم-توهین-های-نژادپرستانه-می-کردند"> <span class="news-type"></span>لینِکِر: به من هم توهین‌های نژادپرستانه می‌کردند</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="پرسپولیس برای سعید صادقی جا باز می‌کند!" href="https://www.varzesh3.com/news/1830190/پرسپولیس-برای-سعید-صادقی-جا-باز-می-کند"> <span class="news-type"></span>پرسپولیس برای سعید صادقی جا باز می‌کند!</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="بعد از سا‌پینتو نوبت به تیم زنان رسید" href="https://www.varzesh3.com/news/1830189/بعد-از-سا-پینتو-نوبت-به-تیم-زنان-رسید"> <span class="news-type"></span>بعد از سا‌پینتو نوبت به تیم زنان رسید</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="برومند: بیرانوند دوست خوب من است" href="https://www.varzesh3.com/news/1830188/برومند-بیرانوند-دوست-خوب-من-است"> <span class="news-type"></span>برومند: بیرانوند دوست خوب من است</a></li>
                            <li class="text-type" data-origin="3" data-media="1" data-tag="" data-sport="1"><a title="طارمی در اورتون؛ او جانشین ریچارلیسون می‌شود؟" href="https://www.varzesh3.com/news/1830186/طارمی-در-اورتون-او-جانشین-ریچارلیسون-می-شود"> <span class="news-type"></span>طارمی در اورتون؛ او جانشین ریچارلیسون می‌شود؟</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="مخالفت مس رفسنجان با جدایی مهدی حسینی" href="https://www.varzesh3.com/news/1830185/مخالفت-مس-رفسنجان-با-جدایی-مهدی-حسینی"> <span class="news-type"></span>مخالفت مس رفسنجان با جدایی مهدی حسینی</a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="برترین گلهای ضربه ایستگاهی تاریخ پاری سن ژرمن" href="https://video.varzesh3.com/video/254231/برترین-گلهای-ضربه-ایستگاهی-تاریخ-پاری-سن-ژرمن"> <span class="news-type"></span>برترین گلهای ضربه ایستگاهی تاریخ پاری سن ژرمن</a></li>
                            <li class="text-type" data-origin="2" data-media="1" data-tag="" data-sport="1"><a title="ده نام بزرگ و مبهم بازار نقل و انتقالات" href="https://www.varzesh3.com/news/1830187/ده-نام-بزرگ-و-مبهم-بازار-نقل-و-انتقالات"> <span class="news-type"></span>ده نام بزرگ و مبهم بازار نقل و انتقالات</a></li>
                            <li class="text-type" data-origin="2" data-media="1" data-tag="" data-sport="1"><a title="در صورت جدایی از PSG؛ نیمار به یووه می‌رود؟" href="https://www.varzesh3.com/news/1830184/در-صورت-جدایی-از-psg-نیمار-به-یووه-می-رود"> <span class="news-type"></span>در صورت جدایی از PSG؛ نیمار به یووه می‌رود؟</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="سردار آزمون چرا از اسکوچیچ حمایت می‌کند؟" href="https://www.varzesh3.com/news/1830183/سردار-آزمون-چرا-از-اسکوچیچ-حمایت-می-کند"> <span class="news-type"></span>سردار آزمون چرا از اسکوچیچ حمایت می‌کند؟</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="حمید مطهری به دنبال جذب دو هافبک پرسپولیس" href="https://www.varzesh3.com/news/1830182/حمید-مطهری-به-دنبال-جذب-دو-هافبک-پرسپولیس"> <span class="news-type"></span>حمید مطهری به دنبال جذب دو هافبک پرسپولیس</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="3"><a title="لیگ ملت‌ها؛ چالش سخت ایران برابر تیم بدون باخت" href="https://www.varzesh3.com/news/1830181/لیگ-ملت-ها-چالش-سخت-ایران-برابر-تیم-بدون-باخت"> <span class="news-type"></span>لیگ ملت‌ها؛ چالش سخت ایران برابر تیم بدون باخت</a></li>
                            <li class="text-type" data-origin="2" data-media="1" data-tag="" data-sport="1"><a title="جدایی قدرتمندترین زن دنیای فوتبال از چلسی" href="https://www.varzesh3.com/news/1830179/جدایی-قدرتمندترین-زن-دنیای-فوتبال-از-چلسی"> <span class="news-type"></span>جدایی قدرتمندترین زن دنیای فوتبال از چلسی</a></li>
                            <li class="text-type" data-origin="3" data-media="1" data-tag="" data-sport="1"><a title="قدوس در تمرینات مالمو چه می‌کند؟" href="https://www.varzesh3.com/news/1830180/قدوس-در-تمرینات-مالمو-چه-می-کند"> <span class="news-type"></span>قدوس در تمرینات مالمو چه می‌کند؟</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="شهره موسوی؛ سرنوشت عجیب صندلی نایب رییس زنان" href="https://www.varzesh3.com/news/1830178/شهره-موسوی-سرنوشت-عجیب-صندلی-نایب-رییس-زنان"> <span class="news-type"></span>شهره موسوی؛ سرنوشت عجیب صندلی نایب رییس زنان</a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="تمام گلهای این فصل چیرو ایموبیله در سری آ" href="https://video.varzesh3.com/video/254230/تمام-گلهای-این-فصل-چیرو-ایموبیله-در-سری-آ"> <span class="news-type"></span>تمام گلهای این فصل چیرو ایموبیله در سری آ</a></li>
                            <li class="text-type" data-origin="3" data-media="1" data-tag="" data-sport="1"><a title="په‌په: بازیکنی با هوش و استعداد طارمی کم است" href="https://www.varzesh3.com/news/1830175/په-په-بازیکنی-با-هوش-و-استعداد-طارمی-کم-است"> <span class="news-type"></span>په‌په: بازیکنی با هوش و استعداد طارمی کم است</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="ورود کاپیتان سابق پرسپولیس به عرصه مربیگری" href="https://www.varzesh3.com/news/1830174/ورود-کاپیتان-سابق-پرسپولیس-به-عرصه-مربیگری"> <span class="news-type"></span>ورود کاپیتان سابق پرسپولیس به عرصه مربیگری</a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="10 پاس گل برتر لیگ هلند در فصل 22-2021" href="https://video.varzesh3.com/video/253941/10-پاس-گل-برتر-لیگ-هلند-در-فصل-22-2021"> <span class="news-type"></span>10 پاس گل برتر لیگ هلند در فصل 22-2021</a></li>
                            <li class="text-type" data-origin="2" data-media="1" data-tag="" data-sport="1"><a title="رد پیشنهاد آرسنال برای رافینیا؛ لیدز کوتاه نمی‌آید" href="https://www.varzesh3.com/news/1830173/رد-پیشنهاد-آرسنال-برای-رافینیا-لیدز-کوتاه-نمی-آید"> <span class="news-type"></span>رد پیشنهاد آرسنال برای رافینیا؛ لیدز کوتاه نمی‌آید</a></li>
                            <li class="text-type" data-origin="2" data-media="1" data-tag="" data-sport="1"><a title="نگرانی جدی رونالدو؛ چرا بازیکن نمی‌خرید؟" href="https://www.varzesh3.com/news/1830170/نگرانی-جدی-رونالدو-چرا-بازیکن-نمی-خرید"> <span class="news-type"></span>نگرانی جدی رونالدو؛ چرا بازیکن نمی‌خرید؟</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="ساپینتو در استقلال؛ بازتابی شگفت‌انگیز در رسانه‌های پرتغالی" href="https://www.varzesh3.com/news/1830169/ساپینتو-در-استقلال-بازتابی-شگفت-انگیز-در-رسانه-های-پرتغالی"> <span class="news-type"></span>ساپینتو در استقلال؛ بازتابی شگفت‌انگیز در رسانه‌های پرتغالی</a></li>
                            <li class="text-type" data-origin="2" data-media="1" data-tag="" data-sport="1"><a title="سوارز: داروین نونیز را با من مقایسه نکنید" href="https://www.varzesh3.com/news/1830167/سوارز-داروین-نونیز-را-با-من-مقایسه-نکنید"> <span class="news-type"></span>سوارز: داروین نونیز را با من مقایسه نکنید</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="3"><a title="والیبالیست‌های جوانان در اسلوونی اردو می‌زنند" href="https://www.varzesh3.com/news/1830163/والیبالیست-های-جوانان-در-اسلوونی-اردو-می-زنند"> <span class="news-type"></span>والیبالیست‌های جوانان در اسلوونی اردو می‌زنند</a></li>
                            <li class="text-type" data-origin="3" data-media="1" data-tag="" data-sport="1"><a title="آزمون: اگر بگذارند رئیس فدراسیون سوارکاری می‌شوم " href="https://www.varzesh3.com/news/1830162/آزمون-اگر-بگذارند-رئیس-فدراسیون-سوارکاری-می-شوم"> <span class="news-type"></span>آزمون: اگر بگذارند رئیس فدراسیون سوارکاری می‌شوم </a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="دو استادیوم به هفته‌های ابتدایی نمی‌رسند! " href="https://www.varzesh3.com/news/1830161/دو-استادیوم-به-هفته-های-ابتدایی-نمی-رسند"> <span class="news-type"></span>دو استادیوم به هفته‌های ابتدایی نمی‌رسند! </a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="3"><a title="تیم ملی در دادگاه جنجالی؛ پیشنهاد انصراف (عکس)" href="https://www.varzesh3.com/news/1830160/تیم-ملی-در-دادگاه-جنجالی-پیشنهاد-انصراف-عکس"> <span class="news-type"></span>تیم ملی در دادگاه جنجالی؛ پیشنهاد انصراف (عکس)</a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="صحبتهای عطایی و بازیکنان پس از شکست مقابل بلغارستان" href="https://video.varzesh3.com/video/254222/صحبتهای-عطایی-و-بازیکنان-پس-از-شکست-مقابل-بلغارستان"> <span class="news-type"></span>صحبتهای عطایی و بازیکنان پس از شکست مقابل بلغارستان</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="بدنساز تیم ملی جوانان معرفی شد " href="https://www.varzesh3.com/news/1830159/بدنساز-تیم-ملی-جوانان-معرفی-شد"> <span class="news-type"></span>بدنساز تیم ملی جوانان معرفی شد </a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="3"><a title="نمی‌توانید بگویید شانسی ایران را بردیم" href="https://www.varzesh3.com/news/1830158/نمی-توانید-بگویید-شانسی-ایران-را-بردیم"> <span class="news-type"></span>نمی‌توانید بگویید شانسی ایران را بردیم</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="هفته آخر لیگ 2؛ قهرمانی شاهین و صعود ون پارس " href="https://www.varzesh3.com/news/1830157/هفته-آخر-لیگ-2-قهرمانی-شاهین-و-صعود-ون-پارس"> <span class="news-type"></span>هفته آخر لیگ 2؛ قهرمانی شاهین و صعود ون پارس </a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="سیاست ذوب‌آهن در پنجره تابستانی لیگ 22" href="https://www.varzesh3.com/news/1830156/سیاست-ذوب-آهن-در-پنجره-تابستانی-لیگ-22"> <span class="news-type"></span>سیاست ذوب‌آهن در پنجره تابستانی لیگ 22</a></li>
                            <li class="text-type" data-origin="2" data-media="1" data-tag="" data-sport="1"><a title="ادعای بارسا: قیمت بالای دی‌یونگ تقصیر لالیگاست" href="https://www.varzesh3.com/news/1830155/ادعای-بارسا-قیمت-بالای-دی-یونگ-تقصیر-لالیگاست"> <span class="news-type"></span>ادعای بارسا: قیمت بالای دی‌یونگ تقصیر لالیگاست</a></li>
                            <li class="text-type" data-origin="2" data-media="1" data-tag="" data-sport="1"><a title="تصمیم نهایی یونایتد؛ حفظ مگوایر بدون بازوبند" href="https://www.varzesh3.com/news/1830154/تصمیم-نهایی-یونایتد-حفظ-مگوایر-بدون-بازوبند"> <span class="news-type"></span>تصمیم نهایی یونایتد؛ حفظ مگوایر بدون بازوبند</a></li>
                            <li class="text-type" data-origin="2" data-media="1" data-tag="" data-sport="1"><a title="آمریکا بازی با ایران را شبیه سازی می‌کند " href="https://www.varzesh3.com/news/1830148/آمریکا-بازی-با-ایران-را-شبیه-سازی-می-کند"> <span class="news-type"></span>آمریکا بازی با ایران را شبیه سازی می‌کند </a></li>
                            <li class="text-type" data-origin="2" data-media="1" data-tag="" data-sport="1"><a title="خواکین: هالند می‌خواست به بتیس بیاید اما نتوانست!" href="https://www.varzesh3.com/news/1830150/خواکین-هالند-می-خواست-به-بتیس-بیاید-اما-نتوانست"> <span class="news-type"></span>خواکین: هالند می‌خواست به بتیس بیاید اما نتوانست!</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="2"><a title="درخشش فوتسال عراق با ناظم الشریعه" href="https://www.varzesh3.com/news/1830144/درخشش-فوتسال-عراق-با-ناظم-الشریعه"> <span class="news-type"></span>درخشش فوتسال عراق با ناظم الشریعه</a></li>
                            <li class="video-type" data-origin="0" data-media="2" data-tag="" data-sport="0"><a title="انتقاد نوری از بالا رفتن رقم قرارداد سعید صادقی و مربیان" href="https://video.varzesh3.com/video/254229/انتقاد-نوری-از-بالا-رفتن-رقم-قرارداد-سعید-صادقی-و-مربیان"> <span class="news-type"></span>انتقاد نوری از بالا رفتن رقم قرارداد سعید صادقی و مربیان</a></li>
                            <li class="text-type" data-origin="1" data-media="1" data-tag="" data-sport="1"><a title="خداحافظی واتس‌اپی حسین‌خانی با مس! (عکس)" href="https://www.varzesh3.com/news/1830146/خداحافظی-واتس-اپی-حسین-خانی-با-مس-عکس"> <span class="news-type"></span>خداحافظی واتس‌اپی حسین‌خانی با مس! (عکس)</a></li>
                            <li class="text-type" data-origin="3" data-media="1" data-tag="" data-sport="3"><a title="کلید غلبه بر ایران از نگاه سرمربی بلغارستان" href="https://www.varzesh3.com/news/1830141/کلید-غلبه-بر-ایران-از-نگاه-سرمربی-بلغارستان"> <span class="news-type"></span>کلید غلبه بر ایران از نگاه سرمربی بلغارستان</a></li>
                </ul>
            </div>
        </div>
    </div>
</div>

            </div>
        </div>
        



        <div class="widget-holder">
            <div class="widget league schedual football" id="83">
                            

<div class="widget-header">
    <h2>لیگ های خارجی</h2>
    <div class="select-options">
        <select id="stage">
                    <option value="901881" selected="selected" data-api="https://football-api.varzesh3.com/v1.0/widgets/83/league/901881">لیگ برتر انگلیس </option>
                    <option value="901878" data-api="https://football-api.varzesh3.com/v1.0/widgets/83/league/901878">سری آ ایتالیا </option>
                    <option value="901880" data-api="https://football-api.varzesh3.com/v1.0/widgets/83/league/901880">لالیگا اسپانیا </option>
                    <option value="901877" data-api="https://football-api.varzesh3.com/v1.0/widgets/83/league/901877">لیگ یک فرانسه </option>
                    <option value="901879" data-api="https://football-api.varzesh3.com/v1.0/widgets/83/league/901879">بوندسلیگا آلمان </option>
        </select>
        <select id="round">
                    <option value="1">هفته 1</option>
                    <option value="2">هفته 2</option>
                    <option value="3">هفته 3</option>
                    <option value="4">هفته 4</option>
                    <option value="5">هفته 5</option>
                    <option value="6">هفته 6</option>
                    <option value="7">هفته 7</option>
                    <option value="8">هفته 8</option>
                    <option value="9">هفته 9</option>
                    <option value="10">هفته 10</option>
                    <option value="11">هفته 11</option>
                    <option value="12">هفته 12</option>
                    <option value="13">هفته 13</option>
                    <option value="14">هفته 14</option>
                    <option value="15">هفته 15</option>
                    <option value="16">هفته 16</option>
                    <option value="17">هفته 17</option>
                    <option value="18">هفته 18</option>
                    <option value="19">هفته 19</option>
                    <option value="20">هفته 20</option>
                    <option value="21">هفته 21</option>
                    <option value="22">هفته 22</option>
                    <option value="23">هفته 23</option>
                    <option value="24">هفته 24</option>
                    <option value="25">هفته 25</option>
                    <option value="26">هفته 26</option>
                    <option value="27">هفته 27</option>
                    <option value="28">هفته 28</option>
                    <option value="29">هفته 29</option>
                    <option value="30">هفته 30</option>
                    <option value="31">هفته 31</option>
                    <option value="32">هفته 32</option>
                    <option value="33">هفته 33</option>
                    <option value="34">هفته 34</option>
                    <option value="35">هفته 35</option>
                    <option value="36">هفته 36</option>
                    <option value="37">هفته 37</option>
                    <option value="38" selected="selected">هفته 38</option>
        </select>
    </div>
</div>
<div class="widget-body">
    <div class="scrollable-box" style="max-height:auto">
        <div class="scroll-list-content">
             <div class="widget-subtitle" style="background-color:#4285f4"><h3>لیگ برتر انگلیس</h3></div>
            <div class="widget-schedual">
                        <div class="date-seprator"><h4>یکشنبه 1 خرداد</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/107968/آرسنال-اورتون"> <img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                    
                                </div>
                                <div class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><a href="/football/team/87/آرسنال">آرسنال</a></div>
                                    <div class="fixture-result-match-goals"><span class="host">5</span><span> - </span><span class="guest">1</span></div>
                                    <div class="fixture-result-match-guest"><a href="/football/team/93/اورتون">اورتون</a></div>
                                </div>
                                <div class="fixture-result-match-time">
                                    <a target="_blank" href="https://video.varzesh3.com/video/252314/"> <img src="https://static.varzesh3.com/img/icons/video-link.svg" /></a>
                                    <span class="match-clock"></span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/107969/برنتفورد-لیدز"> <img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                    
                                </div>
                                <div class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><a href="/football/team/900810/برنتفورد">برنتفورد</a></div>
                                    <div class="fixture-result-match-goals"><span class="host">1</span><span> - </span><span class="guest">2</span></div>
                                    <div class="fixture-result-match-guest"><a href="/football/team/621/لیدز">لیدز</a></div>
                                </div>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock"></span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/107970/برایتون-وستهام"> <img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                    
                                </div>
                                <div class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><a href="/football/team/413/برایتون">برایتون</a></div>
                                    <div class="fixture-result-match-goals"><span class="host">3</span><span> - </span><span class="guest">1</span></div>
                                    <div class="fixture-result-match-guest"><a href="/football/team/96/وستهام">وستهام</a></div>
                                </div>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock"></span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/107971/برنلی-نیوکسل"> <img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                    
                                </div>
                                <div class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><a href="/football/team/89/برنلی">برنلی</a></div>
                                    <div class="fixture-result-match-goals"><span class="host">1</span><span> - </span><span class="guest">2</span></div>
                                    <div class="fixture-result-match-guest"><a href="/football/team/274/نیوکسل">نیوکسل</a></div>
                                </div>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock"></span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/107972/چلسی-واتفورد"> <img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                    
                                </div>
                                <div class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><a href="/football/team/81/چلسی">چلسی</a></div>
                                    <div class="fixture-result-match-goals"><span class="host">2</span><span> - </span><span class="guest">1</span></div>
                                    <div class="fixture-result-match-guest"><a href="/football/team/900834/واتفورد">واتفورد</a></div>
                                </div>
                                <div class="fixture-result-match-time">
                                    <a target="_blank" href="https://video.varzesh3.com/video/252315/"> <img src="https://static.varzesh3.com/img/icons/video-link.svg" /></a>
                                    <span class="match-clock"></span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/107973/کریستال-پالاس-منچستریونایتد"> <img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                    
                                </div>
                                <div class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><a href="/football/team/900872/کریستال-پالاس">کریستال پالاس</a></div>
                                    <div class="fixture-result-match-goals"><span class="host">1</span><span> - </span><span class="guest">0</span></div>
                                    <div class="fixture-result-match-guest"><a href="/football/team/82/منچستریونایتد">منچستریونایتد</a></div>
                                </div>
                                <div class="fixture-result-match-time">
                                    <a target="_blank" href="https://video.varzesh3.com/video/252317/"> <img src="https://static.varzesh3.com/img/icons/video-link.svg" /></a>
                                    <span class="match-clock"></span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/107974/لسترسیتی-ساوتهمپتون"> <img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                    
                                </div>
                                <div class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><a href="/football/team/332/لسترسیتی">لسترسیتی</a></div>
                                    <div class="fixture-result-match-goals"><span class="host">4</span><span> - </span><span class="guest">1</span></div>
                                    <div class="fixture-result-match-guest"><a href="/football/team/900683/ساوتهمپتون">ساوتهمپتون</a></div>
                                </div>
                                <div class="fixture-result-match-time">
                                    
                                    <span class="match-clock"></span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/107975/لیورپول-ولورهمپتون"> <img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                    
                                </div>
                                <div class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><a href="/football/team/83/لیورپول">لیورپول</a></div>
                                    <div class="fixture-result-match-goals"><span class="host">3</span><span> - </span><span class="guest">1</span></div>
                                    <div class="fixture-result-match-guest"><a href="/football/team/92/ولورهمپتون">ولورهمپتون</a></div>
                                </div>
                                <div class="fixture-result-match-time">
                                    <a target="_blank" href="https://video.varzesh3.com/video/252311/"> <img src="https://static.varzesh3.com/img/icons/video-link.svg" /></a>
                                    <span class="match-clock"></span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/107976/منچسترسیتی-استون-ویلا"> <img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                    
                                </div>
                                <div class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><a href="/football/team/84/منچسترسیتی">منچسترسیتی</a></div>
                                    <div class="fixture-result-match-goals"><span class="host">3</span><span> - </span><span class="guest">2</span></div>
                                    <div class="fixture-result-match-guest"><a href="/football/team/85/استون-ویلا">استون ویلا</a></div>
                                </div>
                                <div class="fixture-result-match-time">
                                    <a target="_blank" href="https://video.varzesh3.com/video/252312/"> <img src="https://static.varzesh3.com/img/icons/video-link.svg" /></a>
                                    <span class="match-clock"></span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                            <div class="fixture-result-match odd">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/107977/نوریچ-تاتنهام"> <img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                    
                                </div>
                                <div class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><a href="/football/team/508/نوریچ">نوریچ</a></div>
                                    <div class="fixture-result-match-goals"><span class="host">0</span><span> - </span><span class="guest">5</span></div>
                                    <div class="fixture-result-match-guest"><a href="/football/team/86/تاتنهام">تاتنهام</a></div>
                                </div>
                                <div class="fixture-result-match-time">
                                    <a target="_blank" href="https://video.varzesh3.com/video/252316/"> <img src="https://static.varzesh3.com/img/icons/video-link.svg" /></a>
                                    <span class="match-clock"></span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
            </div>
        </div>
    </div>
    
</div>
<div class="widget-footer"> <a href="/football/league/900564/لیگ-برتر-انگلیس-2021-2022" >مشاهده جدول کامل لیگ برتر انگلیس</a></div>
            </div>
        </div>
        

        

<div class="adbox" data-id="115">
            <div class="native-holder">
                <div id="pos-article-display-3545"></div>
            </div>
</div>


        <div class="widget-holder">
            <div class="widget league schedual football" id="84">
                            

<div class="widget-header">
    <h2>جدول لیگ های خارجی</h2>
    <div class="select-options">
        <select id="stage">
                    <option value="901881" selected="selected" data-api="https://football-api.varzesh3.com/v1.0/widgets/84/league/901881">لیگ برتر انگلیس </option>
                    <option value="901880" data-api="https://football-api.varzesh3.com/v1.0/widgets/84/league/901880">لالیگا اسپانیا </option>
                    <option value="901879" data-api="https://football-api.varzesh3.com/v1.0/widgets/84/league/901879">بوندسلیگا آلمان </option>
                    <option value="901878" data-api="https://football-api.varzesh3.com/v1.0/widgets/84/league/901878">سری آ ایتالیا </option>
                    <option value="901877" data-api="https://football-api.varzesh3.com/v1.0/widgets/84/league/901877">لیگ یک فرانسه </option>
                    <option value="901883" data-api="https://football-api.varzesh3.com/v1.0/widgets/84/league/901883">لیگ برتر روسیه </option>
                    <option value="901885" data-api="https://football-api.varzesh3.com/v1.0/widgets/84/league/901885">ژوپیر لیگ بلژیک </option>
                    <option value="901886" data-api="https://football-api.varzesh3.com/v1.0/widgets/84/league/901886">پریمیر لیگ پرتغال </option>
                    <option value="901876" data-api="https://football-api.varzesh3.com/v1.0/widgets/84/league/901876">اردیویسه هلند </option>
                    <option value="901884" data-api="https://football-api.varzesh3.com/v1.0/widgets/84/league/901884">سوپرلیگ ترکیه </option>
                    <option value="901882" data-api="https://football-api.varzesh3.com/v1.0/widgets/84/league/901882">لیگ ستارگان قطر </option>
                    <option value="901915" data-api="https://football-api.varzesh3.com/v1.0/widgets/84/league/901915">لیگ برتر امارات </option>
                    <option value="902015" data-api="https://football-api.varzesh3.com/v1.0/widgets/84/league/902015">کی لیگ کره جنوبی </option>
                    <option value="902014" data-api="https://football-api.varzesh3.com/v1.0/widgets/84/league/902014">جی لیگ ژاپن </option>
                    <option value="902070" data-api="https://football-api.varzesh3.com/v1.0/widgets/84/league/902070">سوپرلیگ آرژانتین </option>
                    <option value="902078" data-api="https://football-api.varzesh3.com/v1.0/widgets/84/league/902078">سری آ برزیل </option>
        </select>
        
    </div>
</div>
<div class="widget-body">
    
    <div class="widget-table">
        <div class="widget-subtitle" style="background-color:#4285f4"><h3>جدول لیگ برتر انگلیس</h3></div>
        <div class="table-holder">
            <table class=" league-standing widget-standing">
                <thead>
                    <tr>
                        <th scope="col">رتبه</th>
                        <th scope="col">تيم</th>
                        <th scope="col">بازی</th>
                        <th scope="col">امتياز</th>
                    </tr>
                </thead>
                <tbody>
                            <tr>
                                <td scope="row">1</td>
                                <td><a href="/football/team/84/منچسترسیتی"> منچسترسیتی</a></td>
                                <td>38</td>
                                <td>93</td>
                            </tr>
                            <tr>
                                <td scope="row">2</td>
                                <td><a href="/football/team/83/لیورپول"> لیورپول</a></td>
                                <td>38</td>
                                <td>92</td>
                            </tr>
                            <tr>
                                <td scope="row">3</td>
                                <td><a href="/football/team/81/چلسی"> چلسی</a></td>
                                <td>38</td>
                                <td>74</td>
                            </tr>
                            <tr>
                                <td scope="row">4</td>
                                <td><a href="/football/team/86/تاتنهام"> تاتنهام</a></td>
                                <td>38</td>
                                <td>71</td>
                            </tr>
                            <tr>
                                <td scope="row">5</td>
                                <td><a href="/football/team/87/آرسنال"> آرسنال</a></td>
                                <td>38</td>
                                <td>69</td>
                            </tr>
                            <tr>
                                <td scope="row">6</td>
                                <td><a href="/football/team/82/منچستریونایتد"> منچستریونایتد</a></td>
                                <td>38</td>
                                <td>58</td>
                            </tr>
                            <tr>
                                <td scope="row">7</td>
                                <td><a href="/football/team/96/وستهام"> وستهام</a></td>
                                <td>38</td>
                                <td>56</td>
                            </tr>
                            <tr>
                                <td scope="row">8</td>
                                <td><a href="/football/team/332/لسترسیتی"> لسترسیتی</a></td>
                                <td>38</td>
                                <td>52</td>
                            </tr>
                            <tr>
                                <td scope="row">9</td>
                                <td><a href="/football/team/413/برایتون"> برایتون</a></td>
                                <td>38</td>
                                <td>51</td>
                            </tr>
                            <tr>
                                <td scope="row">10</td>
                                <td><a href="/football/team/92/ولورهمپتون"> ولورهمپتون</a></td>
                                <td>38</td>
                                <td>51</td>
                            </tr>
                            <tr>
                                <td scope="row">11</td>
                                <td><a href="/football/team/274/نیوکسل"> نیوکسل</a></td>
                                <td>38</td>
                                <td>49</td>
                            </tr>
                            <tr>
                                <td scope="row">12</td>
                                <td><a href="/football/team/900872/کریستال-پالاس"> کریستال پالاس</a></td>
                                <td>38</td>
                                <td>48</td>
                            </tr>
                            <tr>
                                <td scope="row">13</td>
                                <td><a href="/football/team/900810/برنتفورد"> برنتفورد</a></td>
                                <td>38</td>
                                <td>46</td>
                            </tr>
                            <tr>
                                <td scope="row">14</td>
                                <td><a href="/football/team/85/استون-ویلا"> استون ویلا</a></td>
                                <td>38</td>
                                <td>45</td>
                            </tr>
                            <tr>
                                <td scope="row">15</td>
                                <td><a href="/football/team/900683/ساوتهمپتون"> ساوتهمپتون</a></td>
                                <td>38</td>
                                <td>40</td>
                            </tr>
                            <tr>
                                <td scope="row">16</td>
                                <td><a href="/football/team/93/اورتون"> اورتون</a></td>
                                <td>38</td>
                                <td>39</td>
                            </tr>
                            <tr>
                                <td scope="row">17</td>
                                <td><a href="/football/team/621/لیدز"> لیدز</a></td>
                                <td>38</td>
                                <td>38</td>
                            </tr>
                            <tr>
                                <td scope="row">18</td>
                                <td><a href="/football/team/89/برنلی"> برنلی</a></td>
                                <td>38</td>
                                <td>35</td>
                            </tr>
                            <tr>
                                <td scope="row">19</td>
                                <td><a href="/football/team/900834/واتفورد"> واتفورد</a></td>
                                <td>38</td>
                                <td>23</td>
                            </tr>
                            <tr>
                                <td scope="row">20</td>
                                <td><a href="/football/team/508/نوریچ"> نوریچ</a></td>
                                <td>38</td>
                                <td>22</td>
                            </tr>
                </tbody>
            </table>
        </div>
    </div>
</div>
<div class="widget-footer"> <a href="/football/league/900564/لیگ-برتر-انگلیس-2021-2022" >مشاهده جدول کامل لیگ برتر انگلیس</a></div>
            </div>
        </div>
        

        

<div class="adbox" data-id="162">
            <div class="native-holder">
                <div id="pos-article-display-10718"></div>
            </div>
</div>


        <div class="widget-holder">
            <div class="widget league schedual football" id="85">
                            

<div class="widget-header">
    <h2>مقدماتی جام‌جهانی اروپا</h2>
    <div class="select-options">
        <select id="stage">
                    <option value="901802" data-api="https://football-api.varzesh3.com/v1.0/widgets/85/league/901802">گروه A </option>
                    <option value="901803" data-api="https://football-api.varzesh3.com/v1.0/widgets/85/league/901803">گروه B </option>
                    <option value="901804" data-api="https://football-api.varzesh3.com/v1.0/widgets/85/league/901804">گروه C </option>
                    <option value="901805" data-api="https://football-api.varzesh3.com/v1.0/widgets/85/league/901805">گروه D </option>
                    <option value="901806" data-api="https://football-api.varzesh3.com/v1.0/widgets/85/league/901806">گروه E </option>
                    <option value="901807" data-api="https://football-api.varzesh3.com/v1.0/widgets/85/league/901807">گروه F </option>
                    <option value="901808" data-api="https://football-api.varzesh3.com/v1.0/widgets/85/league/901808">گروه G </option>
                    <option value="901809" data-api="https://football-api.varzesh3.com/v1.0/widgets/85/league/901809">گروه H </option>
                    <option value="901810" data-api="https://football-api.varzesh3.com/v1.0/widgets/85/league/901810">گروه I </option>
                    <option value="901811" data-api="https://football-api.varzesh3.com/v1.0/widgets/85/league/901811">گروه J </option>
                    <option value="901974" selected="selected" data-api="https://football-api.varzesh3.com/v1.0/widgets/85/league/901974">گروه پلی آف A </option>
                    <option value="901975" data-api="https://football-api.varzesh3.com/v1.0/widgets/85/league/901975">گروه پلی آف B </option>
                    <option value="901976" data-api="https://football-api.varzesh3.com/v1.0/widgets/85/league/901976">گروه پلی آف C </option>
        </select>
        
    </div>
</div>
<div class="widget-body">
    <div class="scrollable-box" style="max-height:300px">
        <div class="scroll-list-content">
             <div class="widget-subtitle" style="background-color:#33ab54"><h3>گروه پلی آف A</h3></div>
            <div class="widget-schedual">
                        <div class="date-seprator"><h4>جمعه 5 فروردين</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/102830/ولز-اتریش"> <img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                    
                                </div>
                                <div class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><a href="/football/team/447/ولز">ولز</a></div>
                                    <div class="fixture-result-match-goals"><span class="host">2</span><span> - </span><span class="guest">1</span></div>
                                    <div class="fixture-result-match-guest"><span>اتریش</span></div>
                                </div>
                                <div class="fixture-result-match-time">
                                    <a target="_blank" href="https://video.varzesh3.com/video/248792/"> <img src="https://static.varzesh3.com/img/icons/video-link.svg" /></a>
                                    <span class="match-clock"></span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                        <div class="date-seprator"><h4>چهارشنبه 11 خرداد</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/102831/اسکاتلند-اوکراین"> <img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                    
                                </div>
                                <div class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>اسکاتلند</span></div>
                                    <div class="fixture-result-match-goals"><span class="host">1</span><span> - </span><span class="guest">3</span></div>
                                    <div class="fixture-result-match-guest"><span>اوکراین</span></div>
                                </div>
                                <div class="fixture-result-match-time">
                                    <a target="_blank" href="https://video.varzesh3.com/video/253061/"> <img src="https://static.varzesh3.com/img/icons/video-link.svg" /></a>
                                    <span class="match-clock"></span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
                        <div class="date-seprator"><h4>یکشنبه 15 خرداد</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/173099/ولز-اوکراین"> <img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                    
                                </div>
                                <div class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><a href="/football/team/447/ولز">ولز</a></div>
                                    <div class="fixture-result-match-goals"><span class="host">1</span><span> - </span><span class="guest">0</span></div>
                                    <div class="fixture-result-match-guest"><span>اوکراین</span></div>
                                </div>
                                <div class="fixture-result-match-time">
                                    <a target="_blank" href="https://video.varzesh3.com/video/253275/"> <img src="https://static.varzesh3.com/img/icons/video-link.svg" /></a>
                                    <span class="match-clock"></span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
            </div>
        </div>
    </div>
    
</div>
<div class="widget-footer"> <a href="/football/league/900542/مقدماتی-جام-جهانی-اروپا-2022" >مشاهده جدول کامل مقدماتی جام جهانی اروپا</a></div>
            </div>
        </div>
        <div class="widget-holder">
            <div class="widget league schedual football" id="105">
                            

<div class="widget-header">
    <h2>قهرمانی زیر 23 سال آسیا</h2>
    <div class="select-options">
        <select id="stage">
                    <option value="902051" data-api="https://football-api.varzesh3.com/v1.0/widgets/105/league/902051">گروه A </option>
                    <option value="902052" data-api="https://football-api.varzesh3.com/v1.0/widgets/105/league/902052">گروه B </option>
                    <option value="902053" data-api="https://football-api.varzesh3.com/v1.0/widgets/105/league/902053">گروه C </option>
                    <option value="902054" data-api="https://football-api.varzesh3.com/v1.0/widgets/105/league/902054">گروه D </option>
                    <option value="902072" data-api="https://football-api.varzesh3.com/v1.0/widgets/105/league/902072">یک چهارم نهایی </option>
                    <option value="902073" data-api="https://football-api.varzesh3.com/v1.0/widgets/105/league/902073">نیمه نهایی </option>
                    <option value="902076" data-api="https://football-api.varzesh3.com/v1.0/widgets/105/league/902076">رده‌بندی </option>
                    <option value="902075" selected="selected" data-api="https://football-api.varzesh3.com/v1.0/widgets/105/league/902075">فینال </option>
        </select>
        
    </div>
</div>
<div class="widget-body">
    <div class="scrollable-box" style="max-height:auto">
        <div class="scroll-list-content">
             <div class="widget-subtitle" style="background-color:#f1c40f"><h3>فینال</h3></div>
            <div class="widget-schedual">
                        <div class="date-seprator"><h4>یکشنبه 29 خرداد</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/173613/امید-ازبکستان-امید-عربستان"> <img src="https://static.varzesh3.com/img/icons/info-icon.svg" /></a>
                                    
                                </div>
                                <div class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>امید ازبکستان</span></div>
                                    <div class="fixture-result-match-goals"><span class="host">0</span><span> - </span><span class="guest">2</span></div>
                                    <div class="fixture-result-match-guest"><span>امید عربستان</span></div>
                                </div>
                                <div class="fixture-result-match-time">
                                    <a target="_blank" href="https://video.varzesh3.com/video/254108/"> <img src="https://static.varzesh3.com/img/icons/video-link.svg" /></a>
                                    <span class="match-clock"></span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
            </div>
        </div>
    </div>
    
</div>

            </div>
        </div>

            </div>
        </div>
        <div class="left-side-ad-col">
            <div class="side-banner-zone tb-holder">
                        

<div class="adbox" data-id="183">
            <a  style="display:none;" class="adlink vrz-lazy" target="_blank" href="https://biz.varzesh3.com/events/click/183">
                <img class="adimage" id="img-183" src="https://static.varzeshe3.com/img/blank.png" data-origin="https://biz-cdn.varzesh3.com/banners/2022/04/17/817dd8a4-3c12-48e3-a397-2fbecc4d76ef.gif" width="160" />
            </a>
</div>
                        

<div class="adbox" data-id="284">
            <a  style="display:none;" class="adlink vrz-lazy" target="_blank" href="https://biz.varzesh3.com/events/click/284">
                <img class="adimage" id="img-284" src="https://static.varzeshe3.com/img/blank.png" data-origin="https://biz-cdn.varzesh3.com/banners/2022/06/14/58a87046-8a94-43e4-84f7-84fe3c0f1bb7.gif" width="160" />
            </a>
</div>
                        

<div class="adbox" data-id="285">
            <a  style="display:none;" class="adlink vrz-lazy" target="_blank" href="https://biz.varzesh3.com/events/click/285">
                <img class="adimage" id="img-285" src="https://static.varzeshe3.com/img/blank.png" data-origin="https://biz-cdn.varzesh3.com/banners/2022/05/16/99acbffc-5f65-460b-a226-1ae437907050.gif" width="160" />
            </a>
</div>
                        

<div class="adbox" data-id="182">
            <a  style="display:none;" class="adlink vrz-lazy" target="_blank" href="https://biz.varzesh3.com/events/click/182">
                <img class="adimage" id="img-182" src="https://static.varzeshe3.com/img/blank.png" data-origin="https://biz-cdn.varzesh3.com/banners/2022/02/16/43ed7d0d-e13c-4013-ab47-e3aebf5a0ede.gif" width="160" />
            </a>
</div>
                        

<div class="adbox" data-id="261">
            <a  style="display:none;" class="adlink vrz-lazy" target="_blank" href="https://biz.varzesh3.com/events/click/261">
                <img class="adimage" id="img-261" src="https://static.varzeshe3.com/img/blank.png" data-origin="https://biz-cdn.varzesh3.com/banners/2022/06/16/4a8834bb-0714-4525-921d-04ed11e41c92.gif" width="160" />
            </a>
</div>
                        

<div class="adbox" data-id="333">
            <a  style="display:none;" class="adlink vrz-lazy" target="_blank" href="https://biz.varzesh3.com/events/click/333">
                <img class="adimage" id="img-333" src="https://static.varzeshe3.com/img/blank.png" data-origin="https://biz-cdn.varzesh3.com/banners/2022/06/23/74014f2e-cb22-4d32-94a0-4ef9fec4722a.gif" width="160" />
            </a>
</div>
                        

<div class="adbox" data-id="294">
            <a  style="display:none;" class="adlink vrz-lazy" target="_blank" href="https://biz.varzesh3.com/events/click/294">
                <img class="adimage" id="img-294" src="https://static.varzeshe3.com/img/blank.png" data-origin="https://biz-cdn.varzesh3.com/banners/2022/04/24/32dc32e2-cbf1-4e6f-aebf-9c3b50009493.gif" width="160" />
            </a>
</div>
                        

<div class="adbox" data-id="315">
            <a  style="display:none;" class="adlink vrz-lazy" target="_blank" href="https://biz.varzesh3.com/events/click/315">
                <img class="adimage" id="img-315" src="https://static.varzeshe3.com/img/blank.png" data-origin="https://biz-cdn.varzesh3.com/banners/2022/05/14/47e32495-376f-46ea-a1fb-270d150ba6ad.jpg" width="160" />
            </a>
</div>
            </div>
        </div>
    </div>
</div>

        </main>
    </section>
    
<footer>
    <div class="allfooter">
        <div class="container">
            <div class="allfooter-menus">
                <div class="row">
                            <div class="col-6 col-md-2">
                                <ul class="footermenu">
                                    <li>
                                        <span>
                                            <img alt="سرویس ها" width="20" height="20" src="https://match-cdn.varzesh3.com/footer-menu/2022/03/27/B/uqsoneco.svg?w=20" />
                                            راهنما
                                        </span>
                                    </li>
                                            <li><a  rel="noopener noreferrer" href="https://www.varzesh3.com/contact">ارتباط با ما</a></li>
                                            <li><a  rel="noopener noreferrer" href="https://www.varzesh3.com/advertisement">تبلیغات</a></li>
                                            <li><a  rel="noopener noreferrer" href="https://www.varzesh3.com/careers">فرصت های شغلی</a></li>
                                            <li><a  rel="noopener noreferrer" href="https://www.varzesh3.com/policy">قوانین و مقررات</a></li>
                                            <li><a  rel="noopener noreferrer" href="https://www.varzesh3.com/about">درباره ما</a></li>
                                </ul>
                            </div>
                            <div class="col-6 col-md-2">
                                <ul class="footermenu">
                                    <li>
                                        <span>
                                            <img alt="سرویس ها" width="20" height="20" src="https://match-cdn.varzesh3.com/footer-menu/2022/03/27/B/3q33ppav.svg?w=20" />
                                            سرویس ها
                                        </span>
                                    </li>
                                            <li><a  rel="noopener noreferrer" href="https://www.varzesh3.com/news">اخبار ورزشی</a></li>
                                            <li><a  rel="noopener noreferrer" href="https://www.varzesh3.com/news/live">اخبار زنده</a></li>
                                            <li><a  rel="noopener noreferrer" href="https://www.varzesh3.com/leagues">جدول لیگ ها</a></li>
                                            <li><a  rel="noopener noreferrer" href="https://video.varzesh3.com/">ویدئو</a></li>
                                            <li><a  rel="noopener noreferrer" href="https://www.varzesh3.com/newspaper">روزنامه</a></li>
                                            <li><a  rel="noopener noreferrer" href="https://www.varzesh3.com/livescore">نتایج زنده</a></li>
                                            <li><a  rel="noopener noreferrer" href="https://www.anten.ir/">آنتن</a></li>
                                            <li><a  rel="noopener noreferrer" href="https://pishbini.varzesh3.com/">پیش بینی</a></li>
                                            <li><a  rel="noopener noreferrer" href="https://lenz.varzesh3.com/">لنز</a></li>
                                </ul>
                            </div>
                            <div class="col-6 col-md-2">
                                <ul class="footermenu">
                                    <li>
                                        <span>
                                            <img alt="سرویس ها" width="20" height="20" src="https://match-cdn.varzesh3.com/footer-menu/2022/03/27/B/4q4ntaac.svg?w=20" />
                                            تیم های داخلی
                                        </span>
                                    </li>
                                            <li><a  rel="noopener noreferrer" href="https://www.varzesh3.com/football/team/4/%D8%A7%D8%B3%D8%AA%D9%82%D9%84%D8%A7%D9%84">استقلال</a></li>
                                            <li><a  rel="noopener noreferrer" href="https://www.varzesh3.com/football/team/6/%D9%BE%D8%B1%D8%B3%D9%BE%D9%88%D9%84%DB%8C%D8%B3">پرسپولیس</a></li>
                                            <li><a  rel="noopener noreferrer" href="https://www.varzesh3.com/football/team/18/%D8%AA%D8%B1%D8%A7%DA%A9%D8%AA%D9%88%D8%B1">تراکتور</a></li>
                                            <li><a  rel="noopener noreferrer" href="https://www.varzesh3.com/football/team/1/%D8%B0%D9%88%D8%A8-%D8%A7%D9%93%D9%87%D9%86">ذوب آهن</a></li>
                                            <li><a  rel="noopener noreferrer" href="https://www.varzesh3.com/football/team/10/%D8%B3%D9%BE%D8%A7%D9%87%D8%A7%D9%86">سپاهان</a></li>
                                            <li><a  rel="noopener noreferrer" href="https://www.varzesh3.com/football/team/21/%D8%B5%D9%86%D8%B9%D8%AA-%D9%86%D9%81%D8%AA-%D8%A7%D9%93%D8%A8%D8%A7%D8%AF%D8%A7%D9%86">صنعت نفت آبادان</a></li>
                                            <li><a  rel="noopener noreferrer" href="https://www.varzesh3.com/football/team/2/%D9%81%D8%AC%D8%B1-%D8%B3%D9%BE%D8%A7%D8%B3%DB%8C">فجر سپاسی</a></li>
                                            <li><a  rel="noopener noreferrer" href="https://www.varzesh3.com/football/team/9/%D9%81%D9%88%D9%84%D8%A7%D8%AF">فولاد</a></li>
                                            <li><a  rel="noopener noreferrer" href="https://www.varzesh3.com/football/team/37/%D9%86%D8%B3%D8%A7%D8%AC%DB%8C-%D9%85%D8%A7%D8%B2%D9%86%D8%AF%D8%B1%D8%A7%D9%86">نساجی مازندران</a></li>
                                </ul>
                            </div>
                            <div class="col-6 col-md-2">
                                <ul class="footermenu">
                                    <li>
                                        <span>
                                            <img alt="سرویس ها" width="20" height="20" src="https://match-cdn.varzesh3.com/footer-menu/2022/03/27/B/nupvsdov.svg?w=20" />
                                            تیم های خارجی
                                        </span>
                                    </li>
                                            <li><a  rel="noopener noreferrer" href="https://www.varzesh3.com/football/team/68/%D8%A7%D9%93%D8%AB-%D9%85%DB%8C%D9%84%D8%A7%D9%86">آث میلان</a></li>
                                            <li><a  rel="noopener noreferrer" href="https://www.varzesh3.com/football/team/63/%D8%A7%DB%8C%D9%86%D8%AA%D8%B1">اینتر میلان</a></li>
                                            <li><a  rel="noopener noreferrer" href="https://www.varzesh3.com/football/team/101/%D8%A8%D8%A7%D8%B1%D8%B3%D9%84%D9%88%D9%86%D8%A7">بارسلونا</a></li>
                                            <li><a  rel="noopener noreferrer" href="https://www.varzesh3.com/football/team/145/%D9%BE%D8%A7%D8%B1%DB%8C-%D8%B3%D9%86-%DA%98%D8%B1%D9%85%D9%86">پاری سن ژرمن</a></li>
                                            <li><a  rel="noopener noreferrer" href="https://www.varzesh3.com/football/team/81/%DA%86%D9%84%D8%B3%DB%8C">چلسی</a></li>
                                            <li><a  rel="noopener noreferrer" href="https://www.varzesh3.com/football/team/102/%D8%B1%D9%8A%D9%94%D8%A7%D9%84-%D9%85%D8%A7%D8%AF%D8%B1%DB%8C%D8%AF">رئال مادرید</a></li>
                                            <li><a  rel="noopener noreferrer" href="https://www.varzesh3.com/football/team/83/%D9%84%DB%8C%D9%88%D8%B1%D9%BE%D9%88%D9%84">لیورپول</a></li>
                                            <li><a  rel="noopener noreferrer" href="https://www.varzesh3.com/football/team/82/%D9%85%D9%86%DA%86%D8%B3%D8%AA%D8%B1%DB%8C%D9%88%D9%86%D8%A7%DB%8C%D8%AA%D8%AF">منچستریونایتد</a></li>
                                            <li><a  rel="noopener noreferrer" href="https://www.varzesh3.com/football/team/62/%DB%8C%D9%88%D9%88%D9%86%D8%AA%D9%88%D8%B3">یوونتوس</a></li>
                                </ul>
                            </div>
                            <div class="col-6 col-md-2">
                                <ul class="footermenu">
                                    <li>
                                        <span>
                                            <img alt="سرویس ها" width="20" height="20" src="https://match-cdn.varzesh3.com/footer-menu/2022/03/27/B/0wsjiwoa.svg?w=20" />
                                            رقابت ها
                                        </span>
                                    </li>
                                            <li><a  rel="noopener noreferrer" href="https://www.varzesh3.com/football/league/900578/%D9%84%DB%8C%DA%AF-%D8%A8%D8%B1%D8%AA%D8%B1-%D8%A7%DB%8C%D8%B1%D8%A7%D9%86-1400-1401">جدول لیگ برتر ایران</a></li>
                                            <li><a  rel="noopener noreferrer" href="https://www.varzesh3.com/football/playoffs/900591/%D8%AC%D8%A7%D9%85-%D8%AD%D8%B0%D9%81%DB%8C-%D8%A7%DB%8C%D8%B1%D8%A7%D9%86-1400-1401">نمودار جام حذفی ایران</a></li>
                                            <li><a  rel="noopener noreferrer" href="https://www.varzesh3.com/football/league/900584/%D9%84%DB%8C%DA%AF-%D9%82%D9%87%D8%B1%D9%85%D8%A7%D9%86%D8%A7%D9%86-%D8%A7%D8%B1%D9%88%D9%BE%D8%A7-2021-2022">لیگ قهرمان اروپا</a></li>
                                            <li><a  rel="noopener noreferrer" href="https://www.varzesh3.com/football/league/900604/%D9%84%DB%8C%DA%AF-%D9%82%D9%87%D8%B1%D9%85%D8%A7%D9%86%D8%A7%D9%86-%D8%A7%D9%93%D8%B3%DB%8C%D8%A7-2022">لیگ قهرمان آسیا</a></li>
                                            <li><a  rel="noopener noreferrer" href="https://www.varzesh3.com/football/league/900585/%D9%84%DB%8C%DA%AF-%D8%A7%D8%B1%D9%88%D9%BE%D8%A7-2021-2022">لیگ اروپا</a></li>
                                            <li><a  rel="noopener noreferrer" href="https://www.varzesh3.com/football/league/900564/%D9%84%DB%8C%DA%AF-%D8%A8%D8%B1%D8%AA%D8%B1-%D8%A7%D9%86%DA%AF%D9%84%DB%8C%D8%B3-2021-2022">جدول لیگ برتر انگلیس</a></li>
                                            <li><a  rel="noopener noreferrer" href="https://www.varzesh3.com/football/league/900563/%D9%84%D8%A7%D9%84%DB%8C%DA%AF%D8%A7-%D8%A7%D8%B3%D9%BE%D8%A7%D9%86%DB%8C%D8%A7-2021-2022">جدول لالیگا اسپانیا</a></li>
                                            <li><a  rel="noopener noreferrer" href="https://www.varzesh3.com/football/league/900562/%D8%A8%D9%88%D9%86%D8%AF%D8%B3%D9%84%DB%8C%DA%AF%D8%A7-%D8%A7%D9%93%D9%84%D9%85%D8%A7%D9%86-2021-2022">جدول بوندسلیگا آلمان</a></li>
                                            <li><a  rel="noopener noreferrer" href="https://www.varzesh3.com/football/league/900561/%D8%B3%D8%B1%DB%8C-%D8%A7%D9%93-%D8%A7%DB%8C%D8%AA%D8%A7%D9%84%DB%8C%D8%A7-2021-2022">جدول سری آ ایتالیا</a></li>
                                </ul>
                            </div>
                            <div class="col-6 col-md-2">
                                <ul class="footermenu">
                                    <li>
                                        <span>
                                            <img alt="سرویس ها" width="20" height="20" src="https://match-cdn.varzesh3.com/footer-menu/2022/03/27/B/3szclmgh.svg?w=20" />
                                            سایر
                                        </span>
                                    </li>
                                            <li><a  rel="noopener noreferrer" href="https://www.varzesh3.com/football/fifa-ranking">رنکینگ فیفا</a></li>
                                            <li><a  rel="noopener noreferrer" href="https://www.varzesh3.com/football/transfers/euro/%D9%86%D9%82%D9%84-%D9%88-%D8%A7%D9%86%D8%AA%D9%82%D8%A7%D9%84%D8%A7%D8%AA-%D8%A7%D8%B1%D9%88%D9%BE%D8%A7">نقل و انتقالات اروپا</a></li>
                                            <li><a  rel="noopener noreferrer" href="https://www.varzesh3.com/football/transfers/iran/%D9%86%D9%82%D9%84-%D9%88-%D8%A7%D9%86%D8%AA%D9%82%D8%A7%D9%84%D8%A7%D8%AA-%D9%84%DB%8C%DA%AF-%D8%A8%D8%B1%D8%AA%D8%B1">نقل و انتقالات لیگ برتر ایران</a></li>
                                            <li><a  rel="noopener noreferrer" href="https://www.varzesh3.com/futsal/league/900568/%D9%84%DB%8C%DA%AF-%D8%A8%D8%B1%D8%AA%D8%B1-%D9%81%D9%88%D8%AA%D8%B3%D8%A7%D9%84-1400">جدول لیگ برتر فوتسال</a></li>
                                            <li><a  rel="noopener noreferrer" href="https://www.varzesh3.com/volleyball/league/900566/%D9%84%DB%8C%DA%AF-%D8%A8%D8%B1%D8%AA%D8%B1-%D9%88%D8%A7%D9%84%DB%8C%D8%A8%D8%A7%D9%84-1400">جدول لیگ برتر والیبال</a></li>
                                            <li><a  rel="noopener noreferrer" href="https://www.varzesh3.com/basketball/group/901996/%D9%85%D8%B1%D8%AD%D9%84%D9%87-%D8%AF%D9%88%D9%85-%D9%85%D9%82%D8%AF%D9%85%D8%A7%D8%AA%DB%8C-%DA%AF%D8%B1%D9%88%D9%87-c-%D9%84%DB%8C%DA%AF-%D8%A8%D8%B1%D8%AA%D8%B1-%D8%A8%D8%B3%DA%A9%D8%AA%D8%A8%D8%A7%D9%84-1400">جدول لیگ برتر بسکتبال</a></li>
                                            <li><a  rel="noopener noreferrer" href="https://www.varzesh3.com/football/team/122/%D8%A8%D8%A7%DB%8C%D8%B1%D9%84%D9%88%D8%B1%DA%A9%D9%88%D8%B2%D9%86">بایرلورکوزن</a></li>
                                            <li><a  rel="noopener noreferrer" href="https://www.varzesh3.com/football/team/403/%D9%BE%D9%88%D8%B1%D8%AA%D9%88">پورتو</a></li>
                                            <li><a  rel="noopener noreferrer" href="https://www.varzesh3.com/football/team/162/%D9%81%D8%A7%DB%8C%D9%86%D9%88%D8%B1%D8%AF">فاینورد</a></li>
                                </ul>
                            </div>
                </div>
            </div>
            <div class="allfooter-copy">
                <div class="footerlogo"><span class="footer-logo-holder"><img alt="ورزش سه" width="20" height="20" src="https://static.varzesh3.com/img/shared/footer/logo.svg?w=20" /></span><span>ورزش سه</span></div>
                <div class="copyright">تمام حقوق مادی و معنوی این سایت متعلق به ورزش سه می باشد. شما می توانید از سایت ورزش سه در صورت پذیرش موافقت نامه کاربری استفاده نمایید.</div>
                <div class="socials">
                    <a target="_blank" rel="noopener noreferrer" href="https://facebook.com/varzesh3"> <img alt="فیس بوک" width="8" height="15" src="https://static.varzesh3.com/img/shared/footer/social/facebook.svg?w=8" /></a>
                    <a target="_blank" rel="noopener noreferrer" href="https://twitter.com/varzesh3"><img alt="توییتر" width="15" height="15" src="https://static.varzesh3.com/img/shared/footer/social/twitter.svg?w=15" /> </a>
                    <a target="_blank" rel="noopener noreferrer" href="https://www.instagram.com/varzesh3/"><img alt="اینستاگرام" width="15" height="15" src="https://static.varzesh3.com/img/shared/footer/social/instagram.svg?w=15" /></a>
                    <a target="_blank" rel="noopener noreferrer" href="https://t.me/varzesh3"><img alt="تلگرام" width="15" height="15" src="https://static.varzesh3.com/img/shared/footer/social/telegram.svg?w=15" /> </a>
                    <a target="_blank" rel="noopener noreferrer" href="https://www.varzesh3.com/rss/list"><img alt="خبرخوان" width="15" height="15" src="https://static.varzesh3.com/img/shared/footer/social/rss.svg?w=15" /></a>
                </div>
            </div>
        </div>
    </div>
</footer>

    

<div class="searchbox" data-search-url="https://search-api.varzesh3.com/v1.0/query?q=">
    <form id="vrz-search-form" method="GET" role="search" autocomplete="off" action="/search">
        <div class="input-holder">
            <input id="main-search" class="search" type="search" name="q" placeholder="جستجوی اخبار، تیم‌ها، بازیکنان، ویدیوهای ورزشی …" />
            <span class="close-search">
                <img src="https://static.varzesh3.com/img/icons/close-icon.svg" />
            </span>
        </div>
    </form>
</div>

<div class="search-ajax-result">
    <div id="search-result-tags tagbox ">
        <div class="search-content-type-title">
            برچسب ها
        </div>
        <div class="result-box tags-res tags"></div>
    </div>
    <div id="search-result-news">
        <div class="search-content-type-title">
            اخبار
        </div>
        <div class="result-box  news-res row"></div>
    </div>
    <div id="search-result-videos">
        <div class="search-content-type-title">
            ویدیوها
        </div>
        <div class="result-box  videos-res row"></div>
    </div>
    <div id="search-result-lenz">
        <div class="search-content-type-title">
            تصاویر
        </div>
        <div class="result-box  lenz-res row"></div>
    </div>
    <div class="see-all">
        مشاهده همه نتایج
    </div>
</div>
    <div class="dark-shadow"></div>
    <a id="gotop"></a>
    <div id="alertModal" class="modal fade alerts-show" tabindex="-1" role="dialog">
        <div class="modal-dialog modal-dialog-centered" role="document">
            <div class="modal-content">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                </button>
                <div class="modal-body"></div>
            </div>
        </div>
    </div>
    <script>
        window.appSettings = {
            imageServer: "https://static.varzesh3.com/",
            ssoClientId:"0D996589651C4235B7D40837E8C1DBC2F60410B2C9304298B568",
            ssoUrl:"https://sso.varzesh3.com",
            newsSocket: "https://ksocket.varzesh3.com/news",
            livescoreSocket: "https://ksocket.varzesh3.com/live",
            adsViewUrl: "https://biz.varzesh3.com/events/view",
            adsViewSamplePercentage: 10,
            profileUrl : "https://sso.varzesh3.com/profile",
        };
    </script>
    <script src="https://static.varzesh3.com/js/global.vendor.js?v=1.5.1"></script>
    <script src="https://static.varzesh3.com/js/sharedLayout.js?v=1.5.1"></script>
<script src="https://static.varzesh3.com/js/home.js?v=1.5.1"></script>
<script type="text/javascript">
    (function(){
    var now = new Date();
    var head = document.getElementsByTagName('head')[0];
    var script = document.createElement('script');
    script.async = true;
    var script_address = 'https://cdn.yektanet.com/js/varzesh3.com/article.v1.js';
    script.src = script_address + '?v=' + now.getFullYear().toString() + '0' + now.getMonth() + '0' + now.getDate() + '0' + now.getHours();
    head.appendChild(script);
    })();
</script><script type="text/javascript">
	now = new Date();
	var head = document.getElementsByTagName('head')[0];
	var script = document.createElement('script');
	script.async = true;
	script.type = 'text/javascript';
	var script_address = 'https://cdn.yektanet.com/template/bnrs/yn_bnr.min.js';
	script.src = script_address + '?v=' + now.getFullYear().toString() + '0' + now.getMonth() + '0' + now.getDate() + '0' + now.getHours();
	head.appendChild(script);
</script><script type="text/javascript">
                var head = document.getElementsByTagName("head")[0];
                var script = document.createElement("script");
                script.type = "text/javascript";
                script.async=1;
                script.src = "https://s1.mediaad.org/serve/varzesh3.com/loader.js" ;
                head.appendChild(script);
            </script>
    <script src="https://static.varzesh3.com/js/vrzLazy.js?v=1.5.1"></script>

</body>
</html>
    '''
    )