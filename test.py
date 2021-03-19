from bs4 import BeautifulSoup
soup = '''
<html class="js localstorage sessionstorage csspositionsticky cssanimations backgroundsize" lang="en">
 <head>
  <style>
   body {transition: opacity ease-in 0.2s; } 
body[unresolved] {opacity: 0; display: block; overflow: hidden; position: relative; }
  </style>
  <script async="" src="https://tags.tiqcdn.com/utag/barclaysuk/barclays-public/prod/utag.js" type="text/javascript">
  </script>
  <script>
   function getCookie(name) {
            var value = "; " + document.cookie;
            var parts = value.split("; " + name + "=");
            if (parts.length == 2) return parts.pop().split(";").shift();
        }

        var items = 'Personal,Mortgages,MortgageCalculator,CostCalculator'.split(',');
        var pageDepth = items.length;
        var ccpCookie = getCookie('CCP');
        var ccpCookieValues = {cat2: 'off', cat3: 'off', cat4: 'off'};
        var newReturning = 'undefined' !== typeof getCookie('CCP_OTM') ? "returning" : "new";

        if ('undefined' !== typeof ccpCookie) {
            var decodedCcpCookieValues = JSON.parse(decodeURIComponent(getCookie('CCP')));
            if ('undefined' !== typeof decodedCcpCookieValues.publicuser) {
                ccpCookieValues = decodedCcpCookieValues.publicuser
            }
        }

        var digitalData = {
            user_optin_performance: ccpCookieValues.cat2,
            user_optin_functional: ccpCookieValues.cat3,
            user_optin_targeting: ccpCookieValues.cat4,
            user_newReturning: newReturning,
            page_platform: 'couk',
            page_id: "",
            page_template_id: "\/apps\/componentlibrary\/templates\/tier_3_article",
            page_name: items.join(':'),
            page_title: 'Mortgage cost calculator | How much will my mortgage cost? | Barclays',
            page_cmsPageName: 'cost\u002Dcalculator',
            page_cmsPath: '\/content\/barclaysuk\/en\/personal\/mortgages\/mortgage\u002Dcalculator\/cost\u002Dcalculator',
            page_level1: items[0],
            page_level2: pageDepth > 1 ? items[1] : '',
            page_level3: pageDepth > 2 ? items[2] : '',
            page_level4: pageDepth > 3 ? items[3] : '',
            page_breadcrumb: items.join('>'),
            page_breadCrumbs: items,
            page_url_protocol: document.location.protocol,
            page_url_host: document.location.hostname,
            page_url_path: document.location.pathname,
            page_url_querystring: document.location.search,
            page_url_hash: document.location.hash,
            page_destinationURL: document.location,
            page_referring_url: document.referrer,
            page_search_term: "",
            page_search_type: "",
            device_build_id: "",
            device_name: window.navigator.userAgent,
            device_os: window.navigator.platform,
            device_os_version: window.navigator.userAgent,
            device_type: "",
            event_alt: "",
            event_applicationid: "",
            event_applicationtype: "",
            event_campaign: "",
            event_cssSelector: "",
            event_deeplink_start: "",
            event_deeplink_success: "",
            event_destination: "",
            event_domPath: "",
            event_error_code: "",
            event_error_form_fields: "",
            event_label: "",
            event_section: "",
            event_timestamp_unix: Date.now() / 1000 | 0,
            event_timestamp_utc: new Date().toISOString(),
            event_type: "screenload",
            event_value: "",
            page_accessibility: "",
            page_channel_id: "",
            page_impressions: "",
            page_url_content: "",
            page_version: "",
            user_accessibility: "",
            user_accounts_held: "",
            user_accounts_held_total: "",
            user_accounts_held_3p: "",
            user_accounts_held_3p_total: "",
            user_brassId: "",
            user_browsing_as: "",
            user_customer_segment: "",
            user_eligible_products: "",
            user_hashed_id: "",
            user_hashed_id_business: "",
            user_login_method: "",
            user_login_route: "",
            user_login_segment: "",
            user_login_success: "",
            user_registered: ""
        };
  </script>
  <meta charset="utf-8"/>
  <meta content="ie=edge" http-equiv="x-ua-compatible"/>
  <title>
   Mortgage cost calculator | How much will my mortgage cost? | Barclays - Cost results
  </title>
  <meta content="Mortgage cost calculator | How much will my mortgage cost? | Barclays" property="og:title"/>
  <meta content="Mortgage cost calculator | How much will my mortgage cost? | Barclays" name="twitter:title"/>
  <meta content="Start calculating the cost of your mortgage. See examples of costs for different mortgage types, payment terms and interest rates." name="description"/>
  <meta content="Start calculating the cost of your mortgage. See examples of costs for different mortgage types, payment terms and interest rates." property="og:description"/>
  <meta content="Start calculating the cost of your mortgage. See examples of costs for different mortgage types, payment terms and interest rates." name="twitter:description"/>
  <meta content="article" property="og:type"/>
  <meta content="summary" name="twitter:card"/>
  <meta content="en_GB" property="og:locale"/>
  <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
  <meta content="index,follow" name="robots"/>
  <link href="https://www.barclays.co.uk/mortgages/mortgage-calculator/cost-calculator/" rel="canonical"/>
  <meta content="https://www.barclays.co.uk/mortgages/mortgage-calculator/cost-calculator/" property="og:url"/>
  <meta content="https://www.barclays.co.uk/mortgages/mortgage-calculator/cost-calculator/" name="twitter:url"/>
  <link href="/content/dam/icons/favicons/barclays/favicon.ico" rel="shortcut icon" type="image/x-icon"/>
  <link href="/content/dam/icons/favicons/barclays/apple-touch-icon-180x180.png" rel="apple-touch-icon" sizes="180x180"/>
  <link href="/content/dam/icons/favicons/barclays/apple-touch-icon-167x167.png" rel="apple-touch-icon" sizes="167x167"/>
  <link href="/content/dam/icons/favicons/barclays/apple-touch-icon-152x152.png" rel="apple-touch-icon" sizes="152x152"/>
  <link href="/content/dam/icons/favicons/barclays/apple-touch-icon-120x120.png" rel="apple-touch-icon" sizes="120x120"/>
  <link as="font" crossorigin="" href="/etc/designs/assetsBundle/clientlib/resources/fonts/expert-sans-b14.woff2" rel="preload" type="font/woff2"/>
  <link as="font" crossorigin="" href="/etc/designs/assetsBundle/clientlib/resources/fonts/expert-sans-regular.woff2" rel="preload" type="font/woff2"/>
  <link as="font" crossorigin="" href="/etc/designs/assetsBundle/clientlib/resources/fonts/expert-sans-light.woff2" rel="preload" type="font/woff2"/>
  <link crossorigin="" href="//smetrics.barclays.co.uk" rel="preconnect"/>
  <script src="/etc/designs/componentlibrary/commonlibs/js/libs/modernizr.min.js">
  </script>
  <script type="text/javascript">
   (function() {
                window.ContextHub = window.ContextHub || {};

                /* setting paths */
                ContextHub.Paths = ContextHub.Paths || {};
                ContextHub.Paths.CONTEXTHUB_PATH = "/etc/cloudsettings/default/contexthub";
                ContextHub.Paths.RESOURCE_PATH = "\/content\/barclaysuk\/en\/personal\/mortgages\/mortgage\u002Dcalculator\/cost\u002Dcalculator\/_jcr_content\/contexthub";
                ContextHub.Paths.SEGMENTATION_PATH = "\/etc\/segmentation\/contexthub";
                ContextHub.Paths.CQ_CONTEXT_PATH = "";

                /* setting initial constants */
                ContextHub.Constants = ContextHub.Constants || {};
                ContextHub.Constants.ANONYMOUS_HOME = "/home/users/m/mT4Y971Fb3AWuvKRF-X6";
                ContextHub.Constants.MODE = "no-ui";
            }());
  </script>
  <script src="/etc/cloudsettings/default/contexthub.kernel.js" type="text/javascript">
  </script>
  <!-- TEST : theme.barclays -->
  <link href="/etc/designs/bdl1.7.4/clientlib.css" rel="stylesheet" type="text/css"/>
  <link href="/etc/designs/componentlibrary/componentlibraryBundle/clientlib.css" rel="stylesheet" type="text/css"/>
  <link href="/etc/designs/componentlibrary/clientlib.css" rel="stylesheet" type="text/css"/>
  <link href="/etc/designs/componentlibrary/commonlibs.css" rel="stylesheet" type="text/css"/>
  <link href="/etc/designs/bdl-next/clientlib.css" rel="stylesheet" type="text/css"/>
  <link href="/etc/designs/componentlibrary/theme.barclays/clientlib.css" rel="stylesheet" type="text/css"/>
  <link href="/etc/designs/componentlibrary/coverFinder/clientlib.css" rel="stylesheet" type="text/css"/>
  <!-- this is the page sub header libs -->
  <script src="/etc/designs/componentlibrary/jquery/clientlib.js" type="text/javascript">
  </script>
  <script>
   window.$CQ = jQuery;
  </script>
  <script src="/etc/designs/componentlibrary/commonlibs/js/libs/cookiepolicy.js">
  </script>
  <meta content="685D4DAE5295BC9C156623C34F17A6A6" name="msvalidate.01"/>
  <meta content="FyxsTQlL50FynDQWDnxthDes72UsbBAdfgWuSVpbfNo" name="google-site-verification"/>
  <script>
   bazadebezolkohpepadr="1879093531"
  </script>
  <script defer="" src="https://www.barclays.co.uk/akam/11/7000b060" type="text/javascript">
  </script>
  <style id="__tealiumGDPRecStyle" type="text/css">
   .barclays-gdpr__consent-pane .a-link{color:#0076b6;font-family:Barclays Expert Sans,Expert Sans Light,expertsans-light,Verdana,sans-serif;font-size:16px;font-weight:400;line-height:1.5;margin:0 0 -2px;text-decoration:none;border-bottom:2px solid #0076b6;transition:color .3s cubic-bezier(.25,.46,.45,.94),border-color .3s cubic-bezier(.25,.46,.45,.94)}.barclays-gdpr__consent-pane .a-link:visited{color:#00395d;border-color:#00395d}.barclays-gdpr__consent-pane .a-link:hover{color:#00395d;text-decoration:none;border-color:#00395d}.barclays-gdpr__consent-pane .a-link:active{color:#0076b6}.barclays-gdpr__consent-pane .a-link:focus{color:#00395d;background-color:#f2fbfe;outline:none;box-shadow:0 0 0 2px #f2fbfe,0 0 0 4px #0076b6}.barclays-gdpr__consent-pane .a-link--size-large{font-size:24px}.barclays-gdpr__consent-pane .a-link--size-medium{font-size:20px}.barclays-gdpr__consent-pane .a-link--size-small{font-size:14px}.barclays-gdpr__consent-pane .a-link--size-small,.barclays-gdpr__consent-pane .a-text{font-family:Barclays Expert Sans,Expert Sans Light,expertsans-light,Verdana,sans-serif}.barclays-gdpr__consent-pane .a-text{color:#333;font-size:16px;font-weight:400;line-height:1.5;margin:0}.barclays-gdpr__consent-pane .a-text--weight-light{font-weight:300}.barclays-gdpr__consent-pane .a-text--weight-semibold{font-weight:400}.barclays-gdpr__consent-pane .a-text--weight-bold{font-weight:700}.barclays-gdpr__consent-pane .a-text--style-italic{font-style:italic}.barclays-gdpr__consent-pane .a-text--color-white{color:#fff}.barclays-gdpr__consent-pane .a-text--color-red{color:#e00000}.barclays-gdpr__consent-pane .a-text--color-green{color:#008312}.barclays-gdpr__consent-pane .a-text--color-grey{color:#666}.barclays-gdpr__consent-pane .a-text--color-black{color:#000}.barclays-gdpr__consent-pane .a-text--color-dark-blue{color:#00395d}.barclays-gdpr__consent-pane .a-text--size-large{font-size:30px}.barclays-gdpr__consent-pane .a-text--size-large .a-text__suffix,.barclays-gdpr__consent-pane .a-text--size-medium{font-size:20px}.barclays-gdpr__consent-pane .a-text--size-medium .a-text__suffix{font-size:16px}.barclays-gdpr__consent-pane .a-text--size-small{font-family:Barclays Expert Sans,Expert Sans Light,expertsans-light,Verdana,sans-serif;font-size:14px}.barclays-gdpr__consent-pane .a-text--size-small .a-text__suffix{font-size:14px}.barclays-gdpr__consent-pane .a-text--size-extra-small{font-family:Barclays Expert Sans,Expert Sans Light,expertsans-light,Verdana,sans-serif;font-size:12px}.barclays-gdpr__consent-pane .a-text--size-extra-small .a-text__suffix{font-size:12px}.barclays-gdpr__consent-pane .a-text--with-margin{margin-bottom:16px}@media (min-width:641px){.barclays-gdpr__consent-pane .a-text--with-margin{margin-bottom:24px}}.barclays-gdpr__consent-pane .a-text--align-left{text-align:left}.barclays-gdpr__consent-pane .a-text--align-center{text-align:center}.barclays-gdpr__consent-pane .a-text--align-right{text-align:right}.barclays-gdpr__consent-pane .m-button{color:#0076b6;font-family:Barclays Expert Sans,Expert Sans Light,expertsans-light,Verdana,sans-serif;font-size:1rem;font-weight:400;line-height:1.5;box-sizing:border-box;display:inline-flex;align-items:center;justify-content:center;min-width:140px;padding:11px 20px;margin:0;text-align:center;text-decoration:none;word-break:break-word;cursor:pointer;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;background-color:#fff;border:1px solid #0076b6;border-radius:999px;transition:none .15s ease-out;transition-property:color,background-color,border,outline,box-shadow}.barclays-gdpr__consent-pane .m-button:visited{color:#0076b6;background-color:#fff}.barclays-gdpr__consent-pane .m-button:hover{color:#0076b6;text-decoration:none;background-color:#f2fbfe}.barclays-gdpr__consent-pane .m-button:active{color:#00395d;border-color:#00395d}.barclays-gdpr__consent-pane .m-button--has-focus,.barclays-gdpr__consent-pane .m-button:focus,.barclays-gdpr__consent-pane .m-button:focus-within{color:#0076b6;background-color:#f2fbfe;border-color:#0076b6;outline:none;box-shadow:inset 0 0 0 1px #0076b6}.barclays-gdpr__consent-pane .m-button::-moz-focus-inner{border:0}.barclays-gdpr__consent-pane .m-button.m-button--is-disabled,.barclays-gdpr__consent-pane .m-button.m-button--is-disabled:hover,.barclays-gdpr__consent-pane .m-button.m-button--is-disabled:visited,.barclays-gdpr__consent-pane .m-button[aria-disabled=true],.barclays-gdpr__consent-pane .m-button[disabled]{color:#666;cursor:not-allowed;background-color:#f7f7f7;border-color:#8c8c8c}.barclays-gdpr__consent-pane .m-button__media{position:relative;box-sizing:border-box;display:inline-block;width:16px;height:16px;font-size:16px;line-height:16px;transition:transform .3s ease-out}.barclays-gdpr__consent-pane .m-button__media--medium{width:20px;height:20px;font-size:20px;line-height:1}.barclays-gdpr__consent-pane .m-button__media--large{width:48px;height:48px;font-size:48px}.barclays-gdpr__consent-pane .m-button__media--bordered{padding:8px;font-size:0;border:2px solid #0076b6;border-radius:50%}.barclays-gdpr__consent-pane .m-button__media--medium.m-button__media--bordered{font-size:4px}.barclays-gdpr__consent-pane .m-button__media--large.m-button__media--bordered{font-size:32px}.barclays-gdpr__consent-pane .m-button__media--rotate-90{transform:rotate(90deg)}.barclays-gdpr__consent-pane .m-button__media--rotate-180{transform:rotate(180deg)}.barclays-gdpr__consent-pane .m-button__media--rotate-270{transform:rotate(270deg)}.barclays-gdpr__consent-pane .m-button__icon{display:block;width:100%;height:100%;fill:currentColor}.barclays-gdpr__consent-pane .m-button__badge{position:absolute;top:0;right:0;font-size:16px;transform:translate(40%,-15%)}.barclays-gdpr__consent-pane .m-button--small{padding:5px 24px 4px;font-size:.875rem}.barclays-gdpr__consent-pane .m-button--primary{color:#fff;background-color:#0076b6;border:1px solid transparent}.barclays-gdpr__consent-pane .m-button--primary:visited{color:#fff;background-color:#0076b6}.barclays-gdpr__consent-pane .m-button--primary:hover{color:#fff;background-color:#005e91}.barclays-gdpr__consent-pane .m-button--primary:active{color:#fff;background-color:#00395d}.barclays-gdpr__consent-pane .m-button--primary.m-button--has-focus,.barclays-gdpr__consent-pane .m-button--primary:focus,.barclays-gdpr__consent-pane .m-button--primary:focus-within{color:#0076b6;background-color:#f2fbfe;border-color:#0076b6;outline:none;box-shadow:inset 0 0 0 1px #0076b6}.barclays-gdpr__consent-pane .m-button--primary.m-button--is-disabled,.barclays-gdpr__consent-pane .m-button--primary.m-button--is-disabled:hover,.barclays-gdpr__consent-pane .m-button--primary.m-button--is-disabled:visited,.barclays-gdpr__consent-pane .m-button--primary[aria-disabled=true],.barclays-gdpr__consent-pane .m-button--primary[disabled]{color:#666;cursor:not-allowed;background-color:#f7f7f7;border-color:#8c8c8c}.barclays-gdpr__consent-pane .m-button--outline{color:#fff;background-color:transparent;border:1px solid #fff}.barclays-gdpr__consent-pane .m-button--outline:visited{color:#fff}.barclays-gdpr__consent-pane .m-button--outline:hover{color:#ccc;background-color:transparent;border-color:#ccc}.barclays-gdpr__consent-pane .m-button--outline:active{border-color:#ccc}.barclays-gdpr__consent-pane .m-button--outline--has-focus,.barclays-gdpr__consent-pane .m-button--outline:focus,.barclays-gdpr__consent-pane .m-button--outline:focus-within{color:#000;background-color:transparent;border-color:#000;outline:none;box-shadow:0 0 0 1px #000}.barclays-gdpr__consent-pane .m-button--outline.m-button--is-disabled,.barclays-gdpr__consent-pane .m-button--outline.m-button--is-disabled:hover,.barclays-gdpr__consent-pane .m-button--outline.m-button--is-disabled:visited,.barclays-gdpr__consent-pane .m-button--outline[aria-disabled=true],.barclays-gdpr__consent-pane .m-button--outline[disabled]{color:#666;cursor:not-allowed;background-color:transparent;border-color:#666;opacity:.5}.barclays-gdpr__consent-pane .m-button--text{min-width:auto;padding:0;margin:0 0 -2px;color:#0076b6;background-color:transparent;border:0;border-radius:0;transition:color .3s cubic-bezier(.25,.46,.45,.94),border-color .3s cubic-bezier(.25,.46,.45,.94)}.barclays-gdpr__consent-pane .m-button--text .m-button__text{border-bottom:2px solid #0076b6}.barclays-gdpr__consent-pane .m-button--text:visited{color:#00395d}.barclays-gdpr__consent-pane .m-button--text:visited .m-button__text{border-color:#00395d}.barclays-gdpr__consent-pane .m-button--text:hover{color:#00395d;text-decoration:none;background-color:transparent}.barclays-gdpr__consent-pane .m-button--text:hover .m-button__text{border-color:#00395d}.barclays-gdpr__consent-pane .m-button--text:active{color:#0076b6}.barclays-gdpr__consent-pane .m-button--text--has-focus,.barclays-gdpr__consent-pane .m-button--text:focus,.barclays-gdpr__consent-pane .m-button--text:focus-within{color:#00395d;background-color:#f2fbfe;outline:none;box-shadow:0 0 0 2px #f2fbfe,0 0 0 4px #0076b6}.barclays-gdpr__consent-pane .m-button--text.m-button--is-disabled,.barclays-gdpr__consent-pane .m-button--text.m-button--is-disabled:focus,.barclays-gdpr__consent-pane .m-button--text.m-button--is-disabled:hover,.barclays-gdpr__consent-pane .m-button--text[aria-disabled=true],.barclays-gdpr__consent-pane .m-button--text[disabled]{color:#666;text-decoration:none;cursor:not-allowed;background-color:transparent;box-shadow:none}.barclays-gdpr__consent-pane .m-button--text.m-button--is-disabled .m-button__text,.barclays-gdpr__consent-pane .m-button--text.m-button--is-disabled:focus .m-button__text,.barclays-gdpr__consent-pane .m-button--text.m-button--is-disabled:hover .m-button__text,.barclays-gdpr__consent-pane .m-button--text[aria-disabled=true] .m-button__text,.barclays-gdpr__consent-pane .m-button--text[disabled] .m-button__text{border-color:#666}.barclays-gdpr__consent-pane .m-button--icon-only{min-width:auto;line-height:1;border-radius:8px}.barclays-gdpr__consent-pane .m-button--icon-left .m-button__text{order:1;margin-left:6px}.barclays-gdpr__consent-pane .m-button--icon-right .m-button__text{order:-1;margin-right:6px}.barclays-gdpr__consent-pane .m-button--icon-bottom,.barclays-gdpr__consent-pane .m-button--icon-top{flex-direction:column}.barclays-gdpr__consent-pane .m-button--icon-top .m-button__text{order:1;margin-top:6px}.barclays-gdpr__consent-pane .m-button--icon-bottom .m-button__text{order:-1;margin-bottom:6px}.barclays-gdpr__consent-pane .m-button--full-width{width:100%}@media (max-width:480px){.barclays-gdpr__consent-pane .m-button--full-width-until-sm{width:100%}}@media (max-width:640px){.barclays-gdpr__consent-pane .m-button--full-width-until-md{width:100%}}.barclays-gdpr__consent-pane .m-button--ghost{min-width:auto;color:#fff;background-color:transparent;border-color:transparent}.barclays-gdpr__consent-pane .m-button--ghost:visited{color:#fff}.barclays-gdpr__consent-pane .m-button--ghost:focus,.barclays-gdpr__consent-pane .m-button--ghost:hover{color:#fff;background-color:transparent}.barclays-gdpr__consent-pane .m-button--ghost:focus{border-color:#fff;box-shadow:inset 0 0 0 1px #fff}.barclays-gdpr__consent-pane .m-button--text.m-button--ghost{min-width:auto}.barclays-gdpr__consent-pane .m-button--ghost .m-button__text,.barclays-gdpr__consent-pane .m-button--ghost:hover .m-button__text{border:none}.barclays-gdpr__consent-pane .m-button--text.m-button--ghost:focus{outline:2px solid #fff;outline-offset:2px;box-shadow:none}.barclays-gdpr__consent-pane .m-button--round{width:44px;min-width:auto;height:44px;padding:8px;border-radius:50%}@media (max-width:640px){.barclays-gdpr__consent-pane .m-button--small-md-down{padding:5px 24px 4px;font-size:.875rem}}.barclays-gdpr__consent-pane .m-button__input{position:absolute;z-index:-1;opacity:0}.barclays-gdpr__consent-pane .m-cookie-prompt{box-sizing:border-box;display:flex;padding:0;flex-wrap:wrap;margin:0 -4px}@media (min-width:481px){.barclays-gdpr__consent-pane .m-cookie-prompt{margin:0 -8px}}@media (min-width:641px){.barclays-gdpr__consent-pane .m-cookie-prompt{margin:0 -12px}}.barclays-gdpr__consent-pane .m-cookie-prompt__content{color:#333;font-family:Barclays Expert Sans,Expert Sans Light,expertsans-light,Verdana,sans-serif;font-size:14px;font-weight:400;line-height:1.5;box-sizing:border-box;flex-basis:auto;width:100%;min-width:0;padding:0 4px;margin-bottom:8px;color:#000}@media (min-width:481px){.barclays-gdpr__consent-pane .m-cookie-prompt__content{padding:0 8px}}@media (min-width:641px){.barclays-gdpr__consent-pane .m-cookie-prompt__content{padding:0 12px;margin-bottom:24px}}@media (min-width:961px){.barclays-gdpr__consent-pane .m-cookie-prompt__content{flex:1 1 0%}}.barclays-gdpr__consent-pane .m-cookie-prompt__head{padding-bottom:16px}.barclays-gdpr__consent-pane .m-cookie-prompt__heading{color:#00395d;font-family:Barclays Expert Sans,Expert Sans Light,expertsans-light,Verdana,sans-serif;font-size:26px;font-weight:400;line-height:1.333;margin:0}@media (min-width:641px){.barclays-gdpr__consent-pane .m-cookie-prompt__heading{font-size:30px}}.barclays-gdpr__consent-pane .m-cookie-prompt__body{flex-grow:1}.barclays-gdpr__consent-pane .m-cookie-prompt__menu{box-sizing:border-box;flex-basis:auto;width:100%;min-width:0;padding:0 4px;margin-bottom:8px}@media (min-width:481px){.barclays-gdpr__consent-pane .m-cookie-prompt__menu{padding:0 8px;margin-bottom:16px}}@media (min-width:641px){.barclays-gdpr__consent-pane .m-cookie-prompt__menu{padding:0 12px;margin-bottom:24px}}@media (min-width:961px){.barclays-gdpr__consent-pane .m-cookie-prompt__menu{padding:0 12px;width:auto;display:flex;align-items:flex-end}}.barclays-gdpr__consent-pane .m-cookie-prompt__buttons{box-sizing:border-box;display:flex;padding:0;margin:0 -4px}@media (min-width:481px){.barclays-gdpr__consent-pane .m-cookie-prompt__buttons{margin:0 -8px}}@media (min-width:641px){.barclays-gdpr__consent-pane .m-cookie-prompt__buttons{margin:0 -12px}}@media (min-width:961px){.barclays-gdpr__consent-pane .m-cookie-prompt__buttons{flex-direction:column}}.barclays-gdpr__consent-pane .m-cookie-prompt__button{box-sizing:border-box;flex-basis:auto;width:100%;min-width:0;padding:0 4px}@media (min-width:481px){.barclays-gdpr__consent-pane .m-cookie-prompt__button{padding:0 8px}}@media (min-width:641px){.barclays-gdpr__consent-pane .m-cookie-prompt__button{padding:0 12px}}@media (min-width:961px){.barclays-gdpr__consent-pane .m-cookie-prompt__button:not(:last-child){margin-bottom:16px}}.barclays-gdpr__consent-pane .o-sticky-footer{color:#333;font-family:Barclays Expert Sans,Expert Sans Light,expertsans-light,Verdana,sans-serif;font-size:16px;font-weight:400;line-height:1.5;position:fixed;right:0;bottom:0;left:0;z-index:9998;background-color:#fff;transition-duration:.4s;transform:translateZ(0)}.barclays-gdpr__consent-pane .o-sticky-footer--shadow{box-shadow:0 -2px 7px 0 hsla(0,0%,54.9%,.5)}.barclays-gdpr__consent-pane .o-sticky-footer--secondary{background-color:#f2fbfe}.barclays-gdpr__consent-pane .o-sticky-footer--is-hidden{transform:translate3d(0,100%,0)}.barclays-gdpr__consent-pane .o-sticky-footer__content{max-width:1600px;max-height:60vh;padding:8px 16px 0;margin:0 auto;overflow-y:auto}@media (min-width:641px){.barclays-gdpr__consent-pane .o-sticky-footer__content{padding:24px 24px 0}}.barclays-gdpr__consent-pane .m-button__text{word-break:keep-all}
  </style>
  <script id="__tealiumGDPRecScript" type="text/javascript">
   try{"use strict";(function(){var scope=document.getElementById('__tealiumGDPRecModal');if(scope){var preferencesButton=scope.querySelector('.barclays-gdpr__preferences-button');var acceptAllButton=scope.querySelector('.barclays-gdpr__accept-all-button');var close_1=function(){var _a;scope.style.display='none';(_a=scope.parentElement)===null||_a===void 0?void 0:_a.removeChild(scope);};var onPreferencesClick=function(){close_1();window.utag.gdpr.showConsentPreferences();};preferencesButton===null||preferencesButton===void 0?void 0:preferencesButton.addEventListener('click',onPreferencesClick);var onAcceptAllClick=function(){close_1();window.utag.gdpr.setConsentValue(1);};acceptAllButton===null||acceptAllButton===void 0?void 0:acceptAllButton.addEventListener('click',onAcceptAllClick);}})();} catch(e){utag.DB(e)}
  </script>
  <script async="" charset="utf-8" id="tiqapp" src="//tags.tiqcdn.com/utag/tiqapp/utag.v.js?a=barclaysuk/barclays-public/202010231014&amp;cb=1603730954465" type="text/javascript">
  </script>
 </head>
 <body class="skiplinks-hidden segment-visible desktop" data-runmode-publish="true" data-template="/apps/componentlibrary/templates/tier_3_article">
  <div id="__tealiumGDPRecModal">
   <div class="barclays-gdpr__consent-pane">
    <div aria-labelledby="barclays-gdpr__consent-pane-title" class="o-sticky-footer o-sticky-footer--intrusive o-sticky-footer--shadow" role="banner">
     <div class="o-sticky-footer__content">
      <div class="m-cookie-prompt">
       <div class="m-cookie-prompt__content">
        <div class="m-cookie-prompt__head">
         <h2 class="m-cookie-prompt__heading" id="barclays-gdpr__consent-pane-title">
          Cookies
         </h2>
        </div>
        <div class="m-cookie-prompt__body">
         <p class="a-text">
          We would like to collect data from your device while you use this website. We do this using cookies. You can find out more in our
          <a class="a-link" href="/important-information/cookies-policy/" target="_blank">
           cookie policy
          </a>
          . 
Collecting this data helps us provide the best experience for you, keeps your account secure, helps us provide social media features and allows us to personalise advert and service message content. 
Please select 'Accept all' to consent to us collecting your data in this way. To see other data collection options, select 'Preferences'.
         </p>
        </div>
       </div>
       <div class="m-cookie-prompt__menu">
        <div class="m-cookie-prompt__buttons">
         <div class="m-cookie-prompt__button">
          <button class="barclays-gdpr__preferences-button m-button m-button--full-width">
           <span class="m-button__text">
            Preferences
           </span>
          </button>
         </div>
         <div class="m-cookie-prompt__button">
          <button class="barclays-gdpr__accept-all-button m-button m-button--full-width m-button--primary">
           <span class="m-button__text">
            Accept All
           </span>
          </button>
         </div>
        </div>
       </div>
      </div>
     </div>
    </div>
   </div>
  </div>
  <div class="section">
   <div class="new">
   </div>
  </div>
  <div class="iparys_inherited">
   <div class="custom_tags_head_sitewide iparsys parsys">
   </div>
  </div>
  <div class="section">
   <div class="new">
   </div>
  </div>
  <div class="iparys_inherited">
   <div class="navigation iparsys parsys">
    <div class="reference parbase section">
     <div>
      <div class="skiplinks mod-skiplinks">
       <div class="skiplinks-container">
        <span id="skiplinks-label">
         Skip to:
        </span>
        <ul>
         <li>
          <a accesskey="1" aria-labelledby="skiplinks-label home-link" href="/" id="home-link">
           Home
          </a>
         </li>
         <li>
          <a accesskey="s" aria-labelledby="skiplinks-label content-link" href="#skip-nav" id="content-link">
           Content
          </a>
         </li>
         <li>
          <a accesskey="4" aria-labelledby="skiplinks-label footer-link" href="#skip-main" id="footer-link">
           Footer navigation
          </a>
         </li>
        </ul>
       </div>
      </div>
      <header class="global-header js-globalheader desktop" data-interaction="mouse" style="height: 162px;">
       <div class="segment segment-transition" data-component-type="Header">
        <nav aria-label="Product type navigation" class="segment-wrapper" data-component-type="Link" role="navigation">
         <ul class="segment-body">
          <li class="active">
           <a class="segment-item active" href="/" target="_self">
            Personal
           </a>
          </li>
          <li>
           <a class="segment-item" href="/premier-banking" target="_self">
            Premier
           </a>
          </li>
          <li>
           <a class="segment-item" href="/business-banking" target="_self">
            Business
           </a>
          </li>
          <li>
           <a class="segment-item" href="/wealth-management" target="_self">
            Wealth Management
           </a>
          </li>
          <li>
           <a class="segment-item" href="https://www.barclayscorporate.com/" target="_self">
            Corporate
           </a>
          </li>
         </ul>
        </nav>
       </div>
       <div class="header-main" data-component-type="Header">
        <div class="header-container">
         <div class="logo-section">
          <div class="logo" data-component-type="Link:Logo">
           <a aria-label="Barclays Home" href="/">
            <span class="icon icon-barclays-eagle logo-eagle">
            </span>
            <span class="icon icon-barclays-wordmark logo-title">
            </span>
           </a>
          </div>
         </div>
         <div>
          <div class="search-bar" data-contexthub="false" data-main-search-path="/content/barclaysuk/en/help/results.search.json" data-quick-search-path="/content/barclaysuk/en/help/results.quick-search.json?q={query}&amp;origin={origin}&amp;_charset_=UTF-8&amp;facets={facets}" data-top-search-path="/content/barclaysuk/en/help/results/_jcr_content/search_bar.topanswers.json" id="search-bar" style="display: none;">
           <form action="/help/results/" class="mod-form" data-component-type="SiteSearch" method="get">
            <div data-widget="accessible-autocomplete">
             <!-- Keep label for accessibility on screen readers -->
             <label class="access" for="search-input">
              How can we help?
             </label>
             <div class="search-input-wrapper">
              <input aria-activedescendant="" aria-autocomplete="both" aria-controls="quicksearch-body" autocomplete="off" class="autocomplete-search-field mod-input search-input-nav" id="search-input" name="q" placeholder="How can we help?" type="text"/>
             </div>
             <a aria-describedby="ariaClearField" class="search-clear" href="#" id="clear-search-input" role="button">
              Clear search field
             </a>
             <button class="btn-search btn btn-primary btn-sm" type="submit">
              Search
             </button>
             <button class="search-close xsmall">
              Cancel
              <span class="access">
               Search
              </span>
             </button>
             <input name="_charset_" type="hidden" value="utf-8"/>
             <input name="offset" type="hidden" value="0"/>
             <input name="origin" type="hidden" value="help.barclays.co.uk"/>
             <div aria-hidden="true" class="headersearch" id="quicksearch-body">
              <div class="headersearch-container">
               <div class="headersearch-body">
                <div class="headersearch-results">
                 <div class="headersearch-heading">
                  Unsure what to search for? Other customers found these links helpful.
                 </div>
                 <div class="quick-search--results" id="primary-results-nav">
                 </div>
                 <div class="quick-search--results" id="secondary-results-nav">
                 </div>
                </div>
               </div>
              </div>
             </div>
             <div aria-hidden="true" class="headersearch" id="commonquestions-body">
              <div class="headersearch-container">
               <div class="headersearch-body" data-display-common-questions="true">
                <div class="headersearch-heading">
                 Unsure what to search for? Other customers found these links helpful.
                </div>
                <div class="headersearch-results">
                 <ul class="autocomplete-list" id="common-questions-list" role="listbox">
                  <li aria-selected="false" class="headersearch-item" role="option">
                   <a class="common-questions--list-entry" data-list-index="1" href="https://www.barclays.co.uk/help/international/payments/making-and-receiving-international-payments/what-iban-swiftcode.html" role="link" tabindex="-1">
                    What are IBANs and SWIFT codes?
                   </a>
                  </li>
                  <li aria-selected="false" class="headersearch-item" role="option">
                   <a class="common-questions--list-entry" data-list-index="2" href="https://www.barclays.co.uk/help/payments/payment-information/unrecognised-transaction.html" role="link" tabindex="-1">
                    I don’t know what this transaction is
                   </a>
                  </li>
                  <li aria-selected="false" class="headersearch-item" role="option">
                   <a class="common-questions--list-entry" data-list-index="3" href="https://www.barclays.co.uk/help/customer-services/branch-opening-hours.html" role="link" tabindex="-1">
                    What’s the address, the opening hours and phone number of my Barclays branch?
                   </a>
                  </li>
                  <li aria-selected="false" class="is-last-mobile headersearch-item" role="option">
                   <a class="common-questions--list-entry" data-list-index="4" href="https://www.barclays.co.uk/help/accounts/account-services/find-sort-code.html" role="link" tabindex="-1">
                    How do I find my sort code and account number?
                   </a>
                  </li>
                  <li aria-selected="false" class="is-desktop-only headersearch-item" role="option">
                   <a class="common-questions--list-entry" data-list-index="5" href="https://www.barclays.co.uk/help/accounts/statements-balances/cheque-clearing.html" role="link" tabindex="-1">
                    What is the cheque clearing cycle and how long does it take?
                   </a>
                  </li>
                 </ul>
                </div>
               </div>
              </div>
             </div>
             <div aria-live="assertive" class="sr-only">
             </div>
            </div>
           </form>
          </div>
         </div>
         <div class="utilities" data-component-type="Header:Utilities">
          <a class="login btn btn-primary btn-sm" href="https://bank.barclays.co.uk/olb/authlogin/loginAppContainer.do">
           Log In
          </a>
          <ul>
           <li>
            <a class="btn-none" href="https://bank.barclays.co.uk/olb/registration/registerAppContainer.do" target="_self">
             Register
            </a>
           </li>
           <li class="contact">
            <a href="/contact-us" target="_self">
             <span>
              Contact us
             </span>
            </a>
           </li>
           <li class="branch-finder">
            <a href="/branch-finder" target="_self">
             <span>
              Find a branch
             </span>
            </a>
           </li>
           <li class="search">
            <a aria-haspopup="true" href="#search">
             <span>
              Search
             </span>
            </a>
           </li>
           <li class="hamburger">
            <a aria-expanded="false" aria-label="Navigation Menu" href="#menu">
             <span>
              Menu
             </span>
            </a>
           </li>
          </ul>
         </div>
        </div>
       </div>
       <div class="header-nav">
        <div class="header-container" data-component-type="Header">
         <nav aria-label="Main navigation" class="main-nav" data-menustate="closed" role="navigation" style="visibility: visible;">
          <ul>
           <li aria-haspopup="true" data-component-type="MenuItemLevel1">
            <a aria-expanded="false" href="#">
             Bank
            </a>
            <div aria-hidden="true" class="nav-l2">
             <ul class="nav-col-four">
              <li aria-haspopup="true" data-component-type="MenuItemLevel2">
               <a aria-expanded="false" data-nav-link="#" href="#" role="heading">
                Bank accounts
               </a>
               <div aria-hidden="true" class="nav-l3">
                <ul>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/current-accounts/" target="_self" title="Current accounts">
                   Current accounts
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/current-accounts/bank-account/" target="_self" title="Barclays Bank Account">
                   Barclays Bank Account
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/premier-banking/current-accounts/" target="_self" title="Premier Current Accounts">
                   Premier Current Accounts
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/business-banking/accounts/" target="_self" title="Business current accounts">
                   Business current accounts
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/current-accounts/switch-bank-account/" target="_self" title="Switching bank account to Barclays">
                   Switching bank account to Barclays
                  </a>
                 </li>
                </ul>
               </div>
              </li>
              <li aria-haspopup="true" data-component-type="MenuItemLevel2">
               <a aria-expanded="false" data-nav-link="#" href="#" role="heading">
                Reward and offers
               </a>
               <div aria-hidden="true" class="nav-l3">
                <ul>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/current-accounts/blue-rewards/" target="_self" title="Barclays Blue Rewards">
                   Barclays Blue Rewards
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/current-accounts/cashback/" target="_self" title="Cashback">
                   Cashback
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/current-accounts/customise-my-account/" target="_self" title="Customise my account">
                   Customise my account
                  </a>
                 </li>
                </ul>
               </div>
              </li>
              <li aria-haspopup="true" data-component-type="MenuItemLevel2">
               <a aria-expanded="false" data-nav-link="#" href="#" role="heading">
                Account services
               </a>
               <div aria-hidden="true" class="nav-l3">
                <ul>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/ways-to-bank/banking-from-home/" target="_self" title="Bank from home">
                   Bank from home
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/ways-to-bank/online-banking/" target="_self" title="Explore Online Banking">
                   Explore Online Banking
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/ways-to-bank/mobile-banking-app/" target="_self" title="The Barclays app">
                   The Barclays app
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/ways-to-bank/barclays-launchpad/" target="_self" title="Barclays Launchpad">
                   Barclays Launchpad
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/ways-to-bank/cloud-it/" target="_self" title="Paperless documents">
                   Paperless documents
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="https://bank.barclays.co.uk/olb/registration/registerAppContainer.do" target="_self" title="Register for Online Banking">
                   Register for Online Banking
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/travel/" target="_self" title="Travelling abroad">
                   Travelling abroad
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/important-information/control-your-data/" target="_self" title="Control your data">
                   Control your data
                  </a>
                 </li>
                </ul>
               </div>
              </li>
              <li aria-haspopup="true" data-component-type="MenuItemLevel2">
               <a aria-expanded="false" data-nav-link="#" href="#" role="heading">
                Payment services
               </a>
               <div aria-hidden="true" class="nav-l3">
                <ul>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/current-accounts/bank-account/payment-methods/" target="_self" title="Explore all payment services">
                   Explore all payment services
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/current-accounts/debit-cards/" target="_self" title="Debit cards">
                   Debit cards
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/current-accounts/debit-cards/card-management/" target="_self" title="Card management">
                   Card management
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/ways-to-bank/international-payments/" target="_self" title="International payments">
                   International payments
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="https://www.pingit.com/" target="_self" title="Pingit">
                   Pingit
                  </a>
                 </li>
                </ul>
               </div>
              </li>
             </ul>
            </div>
           </li>
           <li aria-haspopup="true" data-component-type="MenuItemLevel1">
            <a aria-expanded="false" href="#">
             Borrow
            </a>
            <div aria-hidden="true" class="nav-l2">
             <ul class="nav-col-four">
              <li aria-haspopup="true" data-component-type="MenuItemLevel2">
               <a aria-expanded="false" data-nav-link="#" href="#" role="heading">
                Loans and overdraft
               </a>
               <div aria-hidden="true" class="nav-l3">
                <ul>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/loans/" target="_self" title="All loans products">
                   All loans products
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/loans/personal/" target="_self" title="Personal loan">
                   Personal loan
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/loans/car-loans/" target="_self" title="Car loan">
                   Car loan
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/loans/debt-consolidation-loans/" target="_self" title="Debt consolidation loans">
                   Debt consolidation loans
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/loans/home-improvement-loan/" target="_self" title="Home improvement loan">
                   Home improvement loan
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/loans/top-up-loan/" target="_self" title="Top-up loan">
                   Top-up loan
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/current-accounts/bank-account/overdrafts/" target="_self" title="Barclays Overdraft">
                   Barclays Overdraft
                  </a>
                 </li>
                </ul>
               </div>
              </li>
              <li aria-haspopup="true" data-component-type="MenuItemLevel2">
               <a aria-expanded="false" data-nav-link="#" href="#" role="heading">
                Credit cards
               </a>
               <div aria-hidden="true" class="nav-l3">
                <ul>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/credit-cards/" target="_self" title="Compare credit cards">
                   Compare credit cards
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/credit-cards/check-your-eligibility/" target="_self" title="Check your eligibility">
                   Check your eligibility
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/credit-cards/balance-transfer-credit-cards/" target="_self" title="Balance transfer credit cards">
                   Balance transfer credit cards
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/credit-cards/purchase-credit-cards/" target="_self" title="Purchase offer credit cards">
                   Purchase offer credit cards
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/credit-cards/credit-building-credit-cards/" target="_self" title="Credit building credit cards">
                   Credit building credit cards
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/credit-cards/reward-cards/" target="_self" title="Reward credit cards">
                   Reward credit cards
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="https://bcol.barclaycard.co.uk/ecom/as2/initialLogon.do?x=49&amp;y=35?TC=QXBCA23302" target="_self" title="Log in to Barclaycard">
                   Log in to Barclaycard
                  </a>
                 </li>
                </ul>
               </div>
              </li>
              <li aria-haspopup="true" data-component-type="MenuItemLevel2">
               <a aria-expanded="false" data-nav-link="#" href="#" role="heading">
                Tips
               </a>
               <div aria-hidden="true" class="nav-l3">
                <ul>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/loans/ways-to-borrow/" target="_self" title="Ways to borrow">
                   Ways to borrow
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/credit-cards/what-is-a-credit-rating/" target="_self" title="What is a credit rating?">
                   What is a credit rating?
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/money-management/money-worries/" target="_self" title="Money worries">
                   Money worries
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/loans/what-does-apr-mean/" target="_self" title="What does APR mean?">
                   What does APR mean?
                  </a>
                 </li>
                </ul>
               </div>
              </li>
              <li aria-haspopup="true" data-component-type="MenuItemLevel2">
               <a aria-expanded="false" data-nav-link="#" href="#" role="heading">
                Tools
               </a>
               <div aria-hidden="true" class="nav-l3">
                <ul>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/loans/calculator/" target="_self" title="Personal loan calculator">
                   Personal loan calculator
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/loans/budget-planner/" target="_self" title="Budget planner">
                   Budget planner
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/current-accounts/credit-manager/" target="_self" title="Credit Manager">
                   Credit Manager
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/loans/debt-estimator/" target="_self" title="Debt estimator">
                   Debt estimator
                  </a>
                 </li>
                </ul>
               </div>
              </li>
             </ul>
            </div>
           </li>
           <li aria-haspopup="true" data-component-type="MenuItemLevel1">
            <a aria-expanded="false" href="#">
             Credit cards
            </a>
            <div aria-hidden="true" class="nav-l2">
             <ul class="nav-col-four">
              <li aria-haspopup="true" data-component-type="MenuItemLevel2">
               <a aria-expanded="false" data-nav-link="#" href="#" role="heading">
                Apply for a credit card
               </a>
               <div aria-hidden="true" class="nav-l3">
                <ul>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/credit-cards/" target="_self" title="Compare our cards">
                   Compare our cards
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/credit-cards/balance-transfer-credit-cards/" target="_self" title="Balance transfer credit cards">
                   Balance transfer credit cards
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/credit-cards/purchase-credit-cards/" target="_self" title="Purchase offer credit cards">
                   Purchase offer credit cards
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/credit-cards/credit-building-credit-cards/" target="_self" title="Credit building credit cards">
                   Credit building credit cards
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/credit-cards/reward-cards/" target="_self" title="Rewards credit cards">
                   Rewards credit cards
                  </a>
                 </li>
                </ul>
               </div>
              </li>
              <li aria-haspopup="true" data-component-type="MenuItemLevel2">
               <a aria-expanded="false" data-nav-link="#" href="#" role="heading">
                Manage my Barclaycard
               </a>
               <div aria-hidden="true" class="nav-l3">
                <ul>
                 <li data-component-type="MenuItemLevel3">
                  <a href="https://bcol.barclaycard.co.uk/ecom/as2/initialLogon.do?x=49&amp;y=35?TC=QXBCA23302" target="_blank" title="Log in to Barclaycard">
                   Log in to Barclaycard
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="https://www.barclaycard.co.uk/personal/customer/barclaycard-app" target="_blank" title="Barclaycard app">
                   Barclaycard app
                  </a>
                 </li>
                </ul>
               </div>
              </li>
              <li aria-haspopup="true" data-component-type="MenuItemLevel2">
               <a aria-expanded="false" data-nav-link="#" href="#" role="heading">
                Tools
               </a>
               <div aria-hidden="true" class="nav-l3">
                <ul>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/credit-cards/check-your-eligibility/" target="_self" title="Check your eligibility">
                   Check your eligibility
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/credit-cards/jargon-buster/" target="_self" title="Jargon Buster">
                   Jargon Buster
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/credit-cards/what-is-a-credit-rating/" target="_self" title="What is a credit rating?">
                   What is a credit rating?
                  </a>
                 </li>
                </ul>
               </div>
              </li>
              <li aria-haspopup="true" data-component-type="MenuItemLevel2">
               <a aria-expanded="false" data-nav-link="#" href="#" role="heading">
                Help &amp; Support
               </a>
               <div aria-hidden="true" class="nav-l3">
                <ul>
                 <li data-component-type="MenuItemLevel3">
                  <a href="https://www.barclays.co.uk/help/products/cards/barclaycard/?_charset_=UTF-8&amp;offset=0&amp;facets=group-credit-cards&amp;origin=help.barclays.co.uk&amp;q=false" target="_self" title="FAQs">
                   FAQs
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/help/contact-us/barclaycard/" target="_self" title="Contact us">
                   Contact us
                  </a>
                 </li>
                </ul>
               </div>
              </li>
             </ul>
            </div>
           </li>
           <li aria-haspopup="true" data-component-type="MenuItemLevel1">
            <a aria-expanded="false" href="#">
             Save and invest
            </a>
            <div aria-hidden="true" class="nav-l2">
             <ul class="nav-col-four">
              <li aria-haspopup="true" data-component-type="MenuItemLevel2">
               <a aria-expanded="false" data-nav-link="#" href="#" role="heading">
                Cash ISAs
               </a>
               <div aria-hidden="true" class="nav-l3">
                <ul>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/savings/isas/" target="_self" title="Compare ISA accounts">
                   Compare ISA accounts
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/savings/isas/instant-cash-isa/" target="_self" title="Instant Cash ISA">
                   Instant Cash ISA
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/savings/isas/guide-to-isas/" target="_self" title="Guide to ISAs">
                   Guide to ISAs
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/savings/isas/flexible-cash-isa/" target="_self" title="Flexible Cash ISA – 2 Year">
                   Flexible Cash ISA – 2 Year
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/premier-banking/two-year-flexible-cash-isa/" target="_self" title="Premier Flexible Cash ISA – 2 Year">
                   Premier Flexible Cash ISA – 2 Year
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/savings/isas/help-to-buy-isa/" target="_self" title="Managing your Help to Buy: ISA">
                   Managing your Help to Buy: ISA
                  </a>
                 </li>
                </ul>
               </div>
              </li>
              <li aria-haspopup="true" data-component-type="MenuItemLevel2">
               <a aria-expanded="false" data-nav-link="#" href="#" role="heading">
                Savings
               </a>
               <div aria-hidden="true" class="nav-l3">
                <ul>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/savings/instant-access/" target="_self" title="Compare Savings accounts">
                   Compare Savings accounts
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/premier-banking/premier-savings-investments/" target="_self" title="Premier Savings and Investments">
                   Premier Savings and Investments
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/savings/instant-access/everyday-saver/" target="_self" title="Everyday Saver">
                   Everyday Saver
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/savings/instant-access/blue-reward-saver/" target="_self" title="Blue Rewards Saver">
                   Blue Rewards Saver
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/savings/instant-access/childrens-instant-saver/" target="_self" title="Children’s Instant Saver">
                   Children’s Instant Saver
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/savings/instant-access/childrens-regular-saver/" target="_self" title="Children's Regular Saver">
                   Children's Regular Saver
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/savings/interest-rates/" target="_self" title="All interest rates">
                   All interest rates
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/savings/quick-guide-to-saving/" target="_self" title="Guide to Savings">
                   Guide to Savings
                  </a>
                 </li>
                </ul>
               </div>
              </li>
              <li aria-haspopup="true" data-component-type="MenuItemLevel2">
               <a aria-expanded="false" data-nav-link="#" href="#" role="heading">
                Bonds
               </a>
               <div aria-hidden="true" class="nav-l3">
                <ul>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/savings/bonds/" target="_self" title="Compare Bonds accounts">
                   Compare Bonds accounts
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/savings/bonds/1-year-fixed-rate-savings-bond/" target="_self" title="Fixed-rate Bond">
                   Fixed-rate Bond
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/savings/bonds/2-year-flexible-bond/" target="_self" title="Flexible Bond – 2 Year">
                   Flexible Bond – 2 Year
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/premier-banking/flexible-bond/" target="_self" title="Premier Flexible Bond – 2 Year">
                   Premier Flexible Bond – 2 Year
                  </a>
                 </li>
                </ul>
               </div>
              </li>
              <li aria-haspopup="true" data-component-type="MenuItemLevel2">
               <a aria-expanded="false" data-nav-link="#" href="#" role="heading">
                Investments
               </a>
               <div aria-hidden="true" class="nav-l3">
                <ul>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/investments/" target="_self" title="All investment options">
                   All investment options
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/smart-investor/" target="_self" title="Smart Investor">
                   Smart Investor
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/investments/plan-and-invest/" target="_self" title="Plan &amp; Invest">
                   Plan &amp; Invest
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/smart-investor/accounts/investment-isa/" target="_self" title="Investment ISA">
                   Investment ISA
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/smart-investor/accounts/investment-account/" target="_self" title="Investment Account">
                   Investment Account
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/smart-investor/accounts/sipp-pension/" target="_self" title="Self-Invested Personal Pension (SIPP)">
                   Self-Invested Personal Pension (SIPP)
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/smart-investor/ready-made-investments/" target="_self" title="Ready-made Investments">
                   Ready-made Investments
                  </a>
                 </li>
                </ul>
               </div>
              </li>
             </ul>
            </div>
           </li>
           <li aria-haspopup="true" data-component-type="MenuItemLevel1">
            <a aria-expanded="false" href="#">
             Mortgage
            </a>
            <div aria-hidden="true" class="nav-l2">
             <ul class="nav-col-four">
              <li aria-haspopup="true" data-component-type="MenuItemLevel2">
               <a aria-expanded="false" data-nav-link="#" href="#" role="heading">
                Your mortgage needs
               </a>
               <div aria-hidden="true" class="nav-l3">
                <ul>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/mortgages/" target="_self" title="All mortgage services">
                   All mortgage services
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/mortgages/first-time-buyers/" target="_self" title="Buying your first home">
                   Buying your first home
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/mortgages/remortgage/" target="_self" title="Remortgaging with us">
                   Remortgaging with us
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/mortgages/moving-home/" target="_self" title="Moving to a new home">
                   Moving to a new home
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/mortgages/buy-to-let/" target="_self" title="Buying to let">
                   Buying to let
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/mortgages/existing-customer-centre/" target="_self" title="Managing your mortgage">
                   Managing your mortgage
                  </a>
                 </li>
                </ul>
               </div>
              </li>
              <li aria-haspopup="true" data-component-type="MenuItemLevel2">
               <a aria-expanded="false" data-nav-link="#" href="#" role="heading">
                Mortgages by type
               </a>
               <div aria-hidden="true" class="nav-l3">
                <ul>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/mortgages/options/" target="_self" title="All mortgage types">
                   All mortgage types
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/mortgages/fixed-rate-mortgage/" target="_self" title="Fixed-rate mortgages">
                   Fixed-rate mortgages
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/mortgages/tracker-mortgages/" target="_self" title="Tracker mortgages">
                   Tracker mortgages
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/mortgages/offset-mortgage/" target="_self" title="Offset mortgages">
                   Offset mortgages
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/mortgages/buy-to-let/mortgage/" target="_self" title="Buy-to-let mortgages">
                   Buy-to-let mortgages
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/mortgages/family-springboard-mortgage/" target="_self" title="Family Springboard Mortgage">
                   Family Springboard Mortgage
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/mortgages/green-home-mortgage/" target="_self" title="Green Home Mortgage">
                   Green Home Mortgage
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/mortgages/interest-only-mortgage/" target="_self" title="Interest-only mortgages">
                   Interest-only mortgages
                  </a>
                 </li>
                </ul>
               </div>
              </li>
              <li aria-haspopup="true" data-component-type="MenuItemLevel2">
               <a aria-expanded="false" data-nav-link="#" href="#" role="heading">
                Calculators and applications
               </a>
               <div aria-hidden="true" class="nav-l3">
                <ul>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/mortgages/mortgage-calculator/" target="_self" title="All mortgage calculators">
                   All mortgage calculators
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/mortgages/agreement-in-principle/" target="_self" title="Get Agreement in Principle">
                   Get Agreement in Principle
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/mortgages/applications-login/" target="_self" title="Resume Agreement in Principle">
                   Resume Agreement in Principle
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/ways-to-bank/track-it/" target="_self" title="Track an application">
                   Track an application
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/mortgages/mortgage-calculator/interest-rate-calculator/" target="_self" title="Interest rate calculator">
                   Interest rate calculator
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/mortgages/base-rate-information/" target="_self" title="About the mortgage base rate">
                   About the mortgage base rate
                  </a>
                 </li>
                </ul>
               </div>
              </li>
              <li aria-haspopup="true" data-component-type="MenuItemLevel2">
               <a aria-expanded="false" data-nav-link="#" href="#" role="heading">
                Mortgage help
               </a>
               <div aria-hidden="true" class="nav-l3">
                <ul>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/mortgages/guides/" target="_self" title="Mortgage guides and advice">
                   Mortgage guides and advice
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/mortgages/switching-mortgage-deals/" target="_self" title="Switch to a new rate">
                   Switch to a new rate
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/mortgages/existing-customer-centre/additional-borrowing/" target="_self" title="Borrow more on your mortgage">
                   Borrow more on your mortgage
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/mortgages/existing-customer-centre/overpayment-underpayment-explained/" target="_self" title="Making overpayments">
                   Making overpayments
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/mortgages/help-to-buy/" target="_self" title="Help to Buy schemes">
                   Help to Buy schemes
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/mortgages/shared-ownership-mortgages/" target="_self" title="Shared ownership">
                   Shared ownership
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/coronavirus/mortgages/help/" target="_self" title="Worried about mortgage payments?">
                   Worried about mortgage payments?
                  </a>
                 </li>
                </ul>
               </div>
              </li>
             </ul>
            </div>
           </li>
           <li aria-haspopup="true" data-component-type="MenuItemLevel1">
            <a aria-expanded="false" href="#">
             Insure
            </a>
            <div aria-hidden="true" class="nav-l2">
             <ul class="nav-col-four">
              <li aria-haspopup="true" data-component-type="MenuItemLevel2">
               <a aria-expanded="false" data-nav-link="#" href="#" role="heading">
                Home insurance
               </a>
               <div aria-hidden="true" class="nav-l3">
                <ul>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/insurance/home-insurance/" target="_self" title="Barclays Home Insurance">
                   Barclays Home Insurance
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/insurance/home-insurance/landlord-insurance/" target="_self" title="Barclays Landlord Insurance">
                   Barclays Landlord Insurance
                  </a>
                 </li>
                </ul>
               </div>
              </li>
              <li aria-haspopup="true" data-component-type="MenuItemLevel2">
               <a aria-expanded="false" data-nav-link="#" href="#" role="heading">
                Life insurance
               </a>
               <div aria-hidden="true" class="nav-l3">
                <ul>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/insurance/life-insurance/" target="_self" title="All life insurance">
                   All life insurance
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/insurance/life-insurance/barclays-simple-life-insurance/" target="_self" title="Barclays Simple Life Insurance">
                   Barclays Simple Life Insurance
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/insurance/life-insurance/barclays-life-insurance-for-mortgage-holders/" target="_self" title="Life insurance for mortgage protection">
                   Life insurance for mortgage protection
                  </a>
                 </li>
                </ul>
               </div>
              </li>
              <li aria-haspopup="true" data-component-type="MenuItemLevel2">
               <a aria-expanded="false" data-nav-link="#" href="#" role="heading">
                Travel insurance
               </a>
               <div aria-hidden="true" class="nav-l3">
                <ul>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/insurance/travel-insurance/" target="_self" title="All travel insurance">
                   All travel insurance
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/insurance/travel-insurance/travel-pack/" target="_self" title="Travel with breakdown cover">
                   Travel with breakdown cover
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/insurance/travel-insurance/travel-plus-pack/" target="_self" title="Travel with breakdown cover and airport lounges">
                   Travel with breakdown cover and airport lounges
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/travel/" target="_self" title="Travel services">
                   Travel services
                  </a>
                 </li>
                </ul>
               </div>
              </li>
              <li aria-haspopup="true" data-component-type="MenuItemLevel2">
               <a aria-expanded="false" data-nav-link="#" href="#" role="heading">
                Tech insurance
               </a>
               <div aria-hidden="true" class="nav-l3">
                <ul>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/insurance/gadget-and-mobile-phone-insurance/" target="_self" title="All tech insurance">
                   All tech insurance
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/insurance/gadget-and-mobile-phone-insurance/tech-pack/tech-pack/" target="_self" title="Tech Pack">
                   Tech Pack
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/insurance/gadget-and-mobile-phone-insurance/tech-pack-lite/tech-pack-lite/" target="_self" title="Tech Pack Lite">
                   Tech Pack Lite
                  </a>
                 </li>
                </ul>
               </div>
              </li>
             </ul>
            </div>
           </li>
           <li aria-haspopup="true" class="" data-component-type="MenuItemLevel1">
            <a aria-expanded="false" href="#">
             Service and support
            </a>
            <div aria-hidden="true" class="nav-l2">
             <ul class="nav-col-four">
              <li aria-haspopup="true" data-component-type="MenuItemLevel2">
               <a aria-expanded="false" data-nav-link="#" href="#" role="heading">
                Help and support
               </a>
               <div aria-hidden="true" class="nav-l3">
                <ul>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/help/" target="_self" title="Help">
                   Help
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/current-accounts/dormant-lost-accounts/" target="_self" title="Dormant and lost accounts">
                   Dormant and lost accounts
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/security/fraud/" target="_self" title="Fraud prevention">
                   Fraud prevention
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/branch-finder/" target="_self" title="Branch Finder">
                   Branch Finder
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/contact-us/" target="_self" title="Contact us">
                   Contact us
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="https://status.barclays/" target="_self" title="Service status">
                   Service status
                  </a>
                 </li>
                </ul>
               </div>
              </li>
              <li aria-haspopup="true" data-component-type="MenuItemLevel2">
               <a aria-expanded="false" data-nav-link="#" href="#" role="heading">
                Account services
               </a>
               <div aria-hidden="true" class="nav-l3">
                <ul>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/ways-to-bank/banking-from-home/" target="_self" title="Bank from home">
                   Bank from home
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/ways-to-bank/online-banking/" target="_self" title="Explore Online Banking">
                   Explore Online Banking
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/ways-to-bank/mobile-banking-app/" target="_self" title="The Barclays app">
                   The Barclays app
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="https://www.pingit.com/" target="_self" title="Barclays Pingit">
                   Barclays Pingit
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/digital-confidence/eagles/" target="_self" title="Digital Eagles">
                   Digital Eagles
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="https://labs.uk.barclays/" target="_self" title="Eagle Labs">
                   Eagle Labs
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/important-information/control-your-data/" target="_self" title="Control your data">
                   Control your data
                  </a>
                 </li>
                </ul>
               </div>
              </li>
              <li aria-haspopup="true" data-component-type="MenuItemLevel2">
               <a aria-expanded="false" data-nav-link="#" href="#" role="heading">
                Tools and guides
               </a>
               <div aria-hidden="true" class="nav-l3">
                <ul>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/money-management/" target="_self" title="Money management">
                   Money management
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/money-mentors/" target="_self" title="Money Mentors">
                   Money Mentors
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/travel/foreign-currency-exchange/" target="_self" title="Foreign currency">
                   Foreign currency
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/help/international/payments/making-and-receiving-international-payments/generate-iban/" target="_self" title="How can I generate an IBAN?">
                   How can I generate an IBAN?
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/digital-confidence/" target="_self" title="Digital confidence">
                   Digital confidence
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/journal/" target="_self" title="Barclays Journal">
                   Barclays Journal
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/brexit/" target="_self" title="Brexit and your banking">
                   Brexit and your banking
                  </a>
                 </li>
                </ul>
               </div>
              </li>
              <li aria-haspopup="true" data-component-type="MenuItemLevel2">
               <a aria-expanded="false" data-nav-link="#" href="#" role="heading">
                Support
               </a>
               <div aria-hidden="true" class="nav-l3">
                <ul>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/accessibility/" target="_self" title="Accessibility &amp; disability support">
                   Accessibility &amp; disability support
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/money-management/money-worries/" target="_self" title="Money worries">
                   Money worries
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/mental-health/" target="_self" title="Mental health support">
                   Mental health support
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/power-of-attorney/" target="_self" title="Third-party access to bank accounts">
                   Third-party access to bank accounts
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/what-to-do-when-someone-dies/" target="_self" title="What to do when someone dies">
                   What to do when someone dies
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/coronavirus/" target="_self" title="Coronavirus support">
                   Coronavirus support
                  </a>
                 </li>
                </ul>
               </div>
              </li>
             </ul>
            </div>
           </li>
           <li aria-haspopup="true" class="" data-component-type="MenuItemLevel1">
            <a aria-expanded="false" href="#">
             Fraud and privacy
            </a>
            <div aria-hidden="true" class="nav-l2">
             <ul class="nav-col-four">
              <li aria-haspopup="true" data-component-type="MenuItemLevel2">
               <a aria-expanded="false" data-nav-link="#" href="#" role="heading">
                Get in touch now
               </a>
               <div aria-hidden="true" class="nav-l3">
                <ul>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/digisafe/reporting-fraud/" target="_self" title="How to report fraud">
                   How to report fraud
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/digisafe/phone-number-checker/" target="_self" title="Phone number checker">
                   Phone number checker
                  </a>
                 </li>
                </ul>
               </div>
              </li>
              <li aria-haspopup="true" data-component-type="MenuItemLevel2">
               <a aria-expanded="false" data-nav-link="#" href="#" role="heading">
                Protect yourself
               </a>
               <div aria-hidden="true" class="nav-l3">
                <ul>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/digisafe/" target="_self" title="Fraud and protection">
                   Fraud and protection
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/digisafe/financial-fraud/" target="_self" title="Protect your money">
                   Protect your money
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/digisafe/types-of-scams/" target="_self" title="Protect your personal data">
                   Protect your personal data
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/digisafe/fraud-prevention-tips/" target="_self" title="Take control of your personal data">
                   Take control of your personal data
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/digisafe/protecting-you-against-fraud/" target="_self" title="Protecting your account">
                   Protecting your account
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/digisafe/digitally-safe-quiz/" target="_self" title="Digitally safe quiz">
                   Digitally safe quiz
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/coronavirus/scams/" target="_self" title="Coronavirus scams">
                   Coronavirus scams
                  </a>
                 </li>
                </ul>
               </div>
              </li>
              <li aria-haspopup="true" data-component-type="MenuItemLevel2">
               <a aria-expanded="false" data-nav-link="#" href="#" role="heading">
                Your privacy
               </a>
               <div aria-hidden="true" class="nav-l3">
                <ul>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/important-information/control-your-data/" target="_self" title="Control your privacy and data">
                   Control your privacy and data
                  </a>
                 </li>
                </ul>
               </div>
              </li>
              <li aria-haspopup="true" data-component-type="MenuItemLevel2">
               <div aria-hidden="true" class="nav-l3">
               </div>
              </li>
             </ul>
            </div>
           </li>
           <li aria-haspopup="true" class="" data-component-type="MenuItemLevel1">
            <a aria-expanded="false" href="#">
             Moments
            </a>
            <div aria-hidden="true" class="nav-l2">
             <ul class="nav-col-four">
              <li aria-haspopup="true" data-component-type="MenuItemLevel2">
               <a aria-expanded="false" data-nav-link="#" href="#" role="heading">
                Studying and graduation
               </a>
               <div aria-hidden="true" class="nav-l3">
                <ul>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/going-to-university/" target="_self" title="Going to uni">
                   Going to uni
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/moments/your-child-and-university/" target="_self" title="Your child and university">
                   Your child and university
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/journal/life-after-graduation/" target="_self" title="Life after graduation">
                   Life after graduation
                  </a>
                 </li>
                </ul>
               </div>
              </li>
              <li aria-haspopup="true" data-component-type="MenuItemLevel2">
               <a aria-expanded="false" data-nav-link="#" href="#" role="heading">
                Support for life
               </a>
               <div aria-hidden="true" class="nav-l3">
                <ul>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/financial-health-budgeting/" target="_self" title="Financial health and budgeting">
                   Financial health and budgeting
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/moments/buying-a-car/" target="_self" title="Buying a car">
                   Buying a car
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/moments/steps-to-buying-your-first-home/" target="_self" title="Steps to buying your first home">
                   Steps to buying your first home
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/digital-confidence/" target="_self" title="Getting digital skills">
                   Getting digital skills
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/travel/" target="_self" title="Travel">
                   Travel
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/moments/move-or-improve/" target="_self" title="Move or improve?">
                   Move or improve?
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/moments/separation/" target="_self" title="Relationship breakdown">
                   Relationship breakdown
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/moments/living-with-illness-disability/" target="_self" title="Living with illness or disability">
                   Living with illness or disability
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/moments/helping-younger-generations/" target="_self" title="Helping younger generations">
                   Helping younger generations
                  </a>
                 </li>
                </ul>
               </div>
              </li>
              <li aria-haspopup="true" data-component-type="MenuItemLevel2">
               <a aria-expanded="false" data-nav-link="#" href="#" role="heading">
                Your future
               </a>
               <div aria-hidden="true" class="nav-l3">
                <ul>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/first-job/" target="_self" title="Your first job">
                   Your first job
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/starting-a-family/" target="_self" title="Starting a family">
                   Starting a family
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/moments/new-to-the-uk/" target="_self" title="Moving to the UK">
                   Moving to the UK
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/moments/getting-married/" target="_self" title="Getting married">
                   Getting married
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/moments/preparing-for-later-life/" target="_self" title="Later life">
                   Later life
                  </a>
                 </li>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/moments/armed-forces-when-you-have-served/" target="_self" title="Armed Forces veterans">
                   Armed Forces veterans
                  </a>
                 </li>
                </ul>
               </div>
              </li>
              <li aria-haspopup="true" data-component-type="MenuItemLevel2">
               <a aria-expanded="false" data-nav-link="#" href="#" role="heading">
                More life moments
               </a>
               <div aria-hidden="true" class="nav-l3">
                <ul>
                 <li data-component-type="MenuItemLevel3">
                  <a href="/moments/" target="_self" title="Explore all moments">
                   Explore all moments
                  </a>
                 </li>
                </ul>
               </div>
              </li>
             </ul>
            </div>
           </li>
          </ul>
          <div id="menu-screen">
          </div>
         </nav>
        </div>
       </div>
      </header>
     </div>
    </div>
   </div>
  </div>
  <div class="section">
   <div class="new">
   </div>
  </div>
  <div class="iparys_inherited">
   <div class="cookies iparsys parsys">
    <div class="tealiumIQ parbase section">
     <script type="text/javascript">
      (function(a,b,c,d) {
            a='https://tags.tiqcdn.com/utag/barclaysuk/barclays-public/prod/utag.js';
            b=document;
            c='script';
            d=b.createElement(c);
            d.src=a;
            d.type='text/java'+c;
            d.async=true;
            a=b.getElementsByTagName(c)[0];
            a.parentNode.insertBefore(d,a);
        })();
     </script>
    </div>
   </div>
  </div>
  <div class="section">
   <div class="new">
   </div>
  </div>
  <div class="iparys_inherited">
   <div class="upgrade-browser iparsys parsys">
    <div class="upgrade-browser parbase section">
     <!-- [if lt IE 9]>

        <div class="aem-upgrade-browser" role="alert" data-component-type="UpgradeBrowser">
            <div class="aem-upgrade-browser__content">
                <div class='aem-upgrade-browser__media'><svg class='aem-upgrade-browser__icon' xmlns='http://www.w3.org/2000/svg' viewBox='0 0 19 19' id='accept' width='100%' height='100%'><path d='M9.5,19C4.3,19,0,14.7,0,9.5S4.3,0,9.5,0S19,4.3,19,9.5C19,14.7,14.7,19,9.5,19z M9.5,1C4.8,1,1,4.8,1,9.5S4.8,18,9.5,18 S18,14.2,18,9.5C18,4.8,14.2,1,9.5,1z'></path><path d='M10.2,14.5H8.8v-7l1.4-0.3V14.5z'></path><circle cx='9.5' cy='5.3' r='0.8'></circle></svg></div>
                <div class="aem-upgrade-browser__body">
                    <h3 class='aem-upgrade-browser__heading'>Please upgrade your browser</h3>
                    <div class="aem-upgrade-browser__message">
                        <p>To have the best experience using our site, please upgrade to one of the latest browsers.</p>

                    </div>
                </div>
            </div>
        </div>

        <![endif] -->
    </div>
   </div>
  </div>
  <main class="main" id="main-content" role="main">
   <!-- Placeholder <a> tag to ensure main content receives focus with skip link -->
   <div class="skipwrapper">
    <a id="skip-nav" name="skip-nav">
     -
    </a>
   </div>
   <section data-component-type="Hero">
    <div class="jumbo jumbo-noimage jumbo-cyan5">
     <div>
      <div class="jumbo-breadcrumb">
       <div class="jumbo-breadcrumb-body">
        <ul class="breadcrumb" data-component-type="Breadcrumb" typeof="BreadcrumbList" vocab="http://schema.org/">
         <li property="itemListElement" typeof="ListItem">
          <a href="/mortgages/" property="item" typeof="WebPage">
           <span property="name">
            Mortgages
           </span>
          </a>
         </li>
         <li property="itemListElement" typeof="ListItem">
          <a href="/mortgages/mortgage-calculator/" property="item" typeof="WebPage">
           <span property="name">
            Mortgage calculators
           </span>
          </a>
         </li>
        </ul>
       </div>
      </div>
     </div>
     <div class="jumbo-body">
      <div class="container-fluid">
       <div class="row">
        <div class="col-md-8 col-md-offset-1 col-lg-8 col-lg-offset-1">
         <div class="jumbo-content aperture-left">
          <h1 class="h2 jumbo-title">
           Mortgage cost calculator
          </h1>
          <p aria-level="2" class="h2 jumbo-tagline" role="heading">
           How much would a mortgage cost?
          </p>
         </div>
         <div class="jumbo-content">
          <div class="aem-rte">
           <p>
            See examples of costs for different mortgage types and interest rates.
            <br/>
           </p>
          </div>
         </div>
        </div>
       </div>
      </div>
     </div>
    </div>
   </section>
   <div>
    <div class="container-fluid">
     <div class="row">
      <div class="col-xs-12">
      </div>
     </div>
    </div>
   </div>
   <div>
    <section class="wrapper">
     <div class="container-fluid">
      <div class="row">
       <div class="col-xs-12">
        <div data-component-type="MortgageCalculator" data-json-path="/content/dam/barclays-uk/json-files/mortgage-calculator-cost-borrow-2020.json" id="mortgage-calculator-component">
         <noscript>
          Please enable JavaScript to use the Mortgage calculator
         </noscript>
         <div class="mCalc">
          <div class="mCalc-module mCalc-DataError">
           <h2>
            Mortgage Calculator
           </h2>
           <div class="mCalc-Page-Alert">
           </div>
          </div>
          <div class="mCalc-module mCalc-Cost" style="display: none;">
           <div class="row">
            <div class="col-md-8 col-md-offset-2 wrapper-heading">
             <h2>
              What will my mortgage cost?
             </h2>
             <p>
              See examples of costs for different mortgage types, payment terms and interest rates.
             </p>
            </div>
           </div>
           <form class="mCalc-Cost-Form mod-form" data-sitecat="Cost:Form:Calculate">
            <div class="row">
             <div class="col-sm-8 col-sm-offset-2 col-md-6 col-md-offset-3 col-lg-4 col-lg-offset-4">
              <div class="mCalc-Page-Alert" style="display: none;">
              </div>
             </div>
            </div>
            <div class="row mCalc-Component">
             <div class="col-sm-8 col-sm-offset-2 col-md-6 col-md-offset-3 col-lg-4 col-lg-offset-4">
              <fieldset>
               <div class="field-row message-region">
                <div class="mCalc-Cost-Reason" data-sitecat="Cost:Form:Reason" data-tooltip="Are you buying a property, moving your mortgage to us from another lender or would you like to borrow against a property that currently has no mortgage?">
                 <label class="label" for="mCalc-Reason-gckn">
                  Reason for mortgage
                 </label>
                 <a class="mCalc-Tooltip icon-tooltip icon-small" data-hasqtip="0" href="#" oldtitle="Are you buying a property, moving your mortgage to us from another lender or would you like to borrow against a property that currently has no mortgage?" title="">
                 </a>
                 <div class="input-wrapper">
                  <div class="select-field">
                   <select class="large" id="mCalc-Reason-gckn" name="mCalc-Reason-gckn">
                    <option class="option-default" disabled="" selected="" value="">
                     Please select
                    </option>
                    <option value="FTBP">
                     Buy a first home
                    </option>
                    <option value="HP">
                     Move to a new home
                    </option>
                    <option value="BAH">
                     Buy a second home
                    </option>
                    <option value="RML">
                     Remortgage from another lender
                    </option>
                    <option value="ER">
                     Mortgage an owned property
                    </option>
                   </select>
                   <span>
                   </span>
                  </div>
                 </div>
                </div>
               </div>
              </fieldset>
             </div>
            </div>
            <div class="row mCalc-Component">
             <div class="col-sm-8 col-sm-offset-2 col-md-6 col-md-offset-3 col-lg-4 col-lg-offset-4">
              <fieldset>
               <div class="field-row message-region">
                <div class="mCalc-Cost-PropertyValue" data-sitecat="Cost:Form:PropertyValue" data-tooltip="The purchase price of a new home or the market value of your current home if you're remortgaging.">
                 <label class="label" for="mCalc-PropertyValue-vwrq">
                  Estimated property value
                 </label>
                 <a class="mCalc-Tooltip icon-tooltip icon-small" data-hasqtip="1" href="#" oldtitle="The purchase price of a new home or the market value of your current home if you're remortgaging." title="">
                 </a>
                 <div class="input-wrapper">
                  <span class="input-prefix">
                   £
                  </span>
                  <input id="mCalc-PropertyValue-vwrq" maxlength="12" type="tel" value=""/>
                 </div>
                </div>
               </div>
              </fieldset>
             </div>
            </div>
            <div class="row mCalc-Component">
             <div class="col-sm-8 col-sm-offset-2 col-md-6 col-md-offset-3 col-lg-4 col-lg-offset-4">
              <fieldset>
               <div class="field-row message-region">
                <div class="mCalc-Cost-RepaymentType" data-sitecat="Cost:Form:RepaymentType" data-tooltip="Repayment means you pay back part of the amount you borrowed and the interest we charge each month, so your balance reduces with each payment. Interest-only means you pay only the interest each month without repaying what you’ve borrowed. You need to make plans to pay off the amount borrowed by the end of the mortgage. Part and part is a combination of the 2 types.">
                 <label class="label" for="mCalc-RepaymentType-ksup">
                  Payment type
                 </label>
                 <a class="mCalc-Tooltip icon-tooltip icon-small" data-hasqtip="2" href="#" oldtitle="Repayment means you pay back part of the amount you borrowed and the interest we charge each month, so your balance reduces with each payment. Interest-only means you pay only the interest each month without repaying what you’ve borrowed. You need to make plans to pay off the amount borrowed by the end of the mortgage. Part and part is a combination of the 2 types." title="">
                 </a>
                 <div class="input-wrapper">
                  <div class="select-field">
                   <select class="large" id="mCalc-RepaymentType-ksup" name="mCalc-RepaymentType-ksup">
                    <option selected="" value="repayment">
                     Repayment
                    </option>
                    <option value="interest">
                     Interest only
                    </option>
                    <option value="part">
                     Part and part
                    </option>
                   </select>
                   <span>
                   </span>
                  </div>
                 </div>
                </div>
               </div>
              </fieldset>
             </div>
            </div>
            <div class="row mCalc-Component" style="display: none;">
             <div class="col-sm-8 col-sm-offset-2 col-md-6 col-md-offset-3 col-lg-4 col-lg-offset-4">
              <fieldset>
               <div class="field-row message-region">
                <div class="mCalc-Cost-RepaymentPlan" data-sitecat="Cost:Form:RepaymentPlan">
                 <label class="label" for="mCalc-RepaymentPlan-es5n">
                  What plans do you have in place to repay the interest-only balance?
                 </label>
                 <div class="input-wrapper">
                  <div class="select-field">
                   <select class="large" id="mCalc-RepaymentPlan-es5n" name="mCalc-RepaymentPlan-es5n">
                    <option class="option-default" disabled="" selected="" value="">
                     Please select
                    </option>
                    <option value="endowment">
                     Endowment Policy
                    </option>
                    <option value="isa">
                     Stocks and Shares ISA
                    </option>
                    <option value="trust">
                     Professionally managed trust
                    </option>
                    <option value="sell">
                     Selling the mortgaged property
                    </option>
                   </select>
                   <span>
                   </span>
                  </div>
                 </div>
                </div>
               </div>
              </fieldset>
             </div>
            </div>
            <div class="row mCalc-Component" style="display: none;">
             <div class="col-sm-8 col-sm-offset-2 col-md-6 col-md-offset-3 col-lg-4 col-lg-offset-4">
              <fieldset>
               <div class="field-row message-region">
                <div class="mCalc-Cost-Interest" data-sitecat="Cost:Form:Interest" data-tooltip="The amount in your mortgage on which you repay the interest we charge without reducing your mortgage balance.">
                 <label class="label" for="mCalc-Interest-t6u8">
                  Interest-only balance
                 </label>
                 <a class="mCalc-Tooltip icon-tooltip icon-small" data-hasqtip="4" href="#" oldtitle="The amount in your mortgage on which you repay the interest we charge without reducing your mortgage balance." title="">
                 </a>
                 <div class="input-wrapper">
                  <span class="input-prefix">
                   £
                  </span>
                  <input id="mCalc-Interest-t6u8" maxlength="12" type="tel" value=""/>
                 </div>
                </div>
               </div>
              </fieldset>
             </div>
            </div>
            <div class="row mCalc-Component" style="display: none;">
             <div class="col-sm-8 col-sm-offset-2 col-md-6 col-md-offset-3 col-lg-4 col-lg-offset-4">
              <fieldset>
               <div class="field-row message-region">
                <div class="mCalc-Cost-Repayment" data-sitecat="Cost:Form:Repayment" data-tooltip="The amount in your mortgage on which you repay the part of the amount you borrowed and the interest we charge.">
                 <label class="label" for="mCalc-Repayment-ffra">
                  Repayment balance
                 </label>
                 <a class="mCalc-Tooltip icon-tooltip icon-small" data-hasqtip="5" href="#" oldtitle="The amount in your mortgage on which you repay the part of the amount you borrowed and the interest we charge." title="">
                 </a>
                 <div class="input-wrapper">
                  <span class="input-prefix">
                   £
                  </span>
                  <input id="mCalc-Repayment-ffra" maxlength="12" type="tel" value=""/>
                 </div>
                </div>
               </div>
              </fieldset>
             </div>
            </div>
            <div class="row mCalc-Component" style="">
             <div class="col-sm-8 col-sm-offset-2 col-md-6 col-md-offset-3 col-lg-4 col-lg-offset-4">
              <fieldset>
               <div class="field-row message-region">
                <div class="mCalc-Cost-Borrow" data-sitecat="Cost:Form:Borrow" data-tooltip="Enter the amount you need to buy the property. Don't include your deposit.">
                 <label class="label" for="mCalc-Borrow-ufrr">
                  I want to borrow
                 </label>
                 <a class="mCalc-Tooltip icon-tooltip icon-small" data-hasqtip="3" href="#" oldtitle="Enter the amount you need to buy the property. Don't include your deposit." title="">
                 </a>
                 <div class="input-wrapper">
                  <span class="input-prefix">
                   £
                  </span>
                  <input id="mCalc-Borrow-ufrr" maxlength="12" type="tel" value=""/>
                 </div>
                </div>
               </div>
              </fieldset>
             </div>
            </div>
            <div class="row" style="display: none;">
             <div class="col-sm-8 col-sm-offset-2 col-md-6 col-md-offset-3 col-lg-4 col-lg-offset-4">
              <fieldset>
               <div class="field-row message-region">
                <label>
                 Total borrowing
                </label>
                <p>
                 <span class="mCalc-Cost-TotalBorrowing">
                  £20,000
                 </span>
                </p>
               </div>
              </fieldset>
             </div>
            </div>
            <div class="row mCalc-Component" style="display: none;">
             <div class="col-sm-8 col-sm-offset-2 col-md-6 col-md-offset-3 col-lg-4 col-lg-offset-4">
              <fieldset class="horizontal">
               <div class="field-row message-region notification-error">
                <div class="mCalc-Cost-FlatMaisonette" data-sitecat="Cost:Form:FlatOrMaisonette">
                 <legend class="label">
                  Is this property a flat (or maisonette)?
                 </legend>
                 <input id="mCalc-FlatMaisonette-lwsl-yes" name="mCalc-FlatMaisonette-lwsl" type="radio" value="yes"/>
                 <label for="mCalc-FlatMaisonette-lwsl-yes">
                  Yes
                 </label>
                 <input id="mCalc-FlatMaisonette-lwsl-no" name="mCalc-FlatMaisonette-lwsl" type="radio" value="no"/>
                 <label for="mCalc-FlatMaisonette-lwsl-no">
                  No
                 </label>
                </div>
                <div aria-live="polite" class="alert" role="alert">
                 Please make a selection.
                </div>
               </div>
              </fieldset>
             </div>
            </div>
            <div class="row">
             <div class="col-sm-8 col-sm-offset-2 col-md-6 col-md-offset-3 col-lg-4 col-lg-offset-4">
              <fieldset>
               <div class="field-row message-region">
                <label>
                 Loan to value
                 <a class="mCalc-Tooltip mCalc-LTV-Tooltip icon-tooltip icon-small" data-hasqtip="7" href="#" oldtitle="The proportion of the property value you want to borrow expressed as a percentage. To work it out we divide the amount you want to borrow by the property value and multiply the result by 100." title="">
                 </a>
                </label>
                <p>
                 <span class="mCalc-Cost-LTV" data-tooltip="The proportion of the property value you want to borrow expressed as a percentage. To work it out we divide the amount you want to borrow by the property value and multiply the result by 100.">
                  50%
                 </span>
                 <span class="mCalc-Subtext">
                  The lower your loan to value, the more deals you can choose from.
                 </span>
                </p>
                <div class="mCalc-Cost-LTV-Error">
                 <p style="margin-top: 1rem">
                  If your loan to value is over 85%, the most you can borrow is
                 </p>
                 <ul>
                  <li>
                   £220,000 for a flat or maisonette
                  </li>
                  <li>
                   £500,000 for all other property types
                  </li>
                 </ul>
                </div>
               </div>
              </fieldset>
             </div>
            </div>
            <div class="row mCalc-Component">
             <div class="col-sm-8 col-sm-offset-2 col-md-6 col-md-offset-3 col-lg-4 col-lg-offset-4">
              <fieldset>
               <div class="field-row message-region">
                <div class="mCalc-Cost-Term" data-sitecat="Cost:Form:TermYear|Cost:Form:TermMonth" data-tooltip="The number of years and months before you'll pay off this mortgage.">
                 <label for="mCalc-TermYears-xh3v">
                  Pay back mortgage over
                 </label>
                 <a class="mCalc-Tooltip icon-tooltip icon-small" data-hasqtip="6" href="#" oldtitle="The number of years and months before you'll pay off this mortgage." title="">
                 </a>
                 <div class="mCalc-DoubleSelect">
                  <div class="mCalc-DoubleSelect-Wrapper">
                   <label class="label hidden" for="mCalc-TermYears-xh3v">
                    Years
                   </label>
                   <div class="input-wrapper">
                    <div class="select-field">
                     <select class="large" id="mCalc-TermYears-xh3v" name="mCalc-TermYears-xh3v">
                      <option class="option-default" disabled="" selected="" value="">
                       Years
                      </option>
                      <option value="40">
                       40 years
                      </option>
                      <option value="39">
                       39 years
                      </option>
                      <option value="38">
                       38 years
                      </option>
                      <option value="37">
                       37 years
                      </option>
                      <option value="36">
                       36 years
                      </option>
                      <option value="35">
                       35 years
                      </option>
                      <option value="34">
                       34 years
                      </option>
                      <option value="33">
                       33 years
                      </option>
                      <option value="32">
                       32 years
                      </option>
                      <option value="31">
                       31 years
                      </option>
                      <option value="30">
                       30 years
                      </option>
                      <option value="29">
                       29 years
                      </option>
                      <option value="28">
                       28 years
                      </option>
                      <option value="27">
                       27 years
                      </option>
                      <option value="26">
                       26 years
                      </option>
                      <option value="25">
                       25 years
                      </option>
                      <option value="24">
                       24 years
                      </option>
                      <option value="23">
                       23 years
                      </option>
                      <option value="22">
                       22 years
                      </option>
                      <option value="21">
                       21 years
                      </option>
                      <option value="20">
                       20 years
                      </option>
                      <option value="19">
                       19 years
                      </option>
                      <option value="18">
                       18 years
                      </option>
                      <option value="17">
                       17 years
                      </option>
                      <option value="16">
                       16 years
                      </option>
                      <option value="15">
                       15 years
                      </option>
                      <option value="14">
                       14 years
                      </option>
                      <option value="13">
                       13 years
                      </option>
                      <option value="12">
                       12 years
                      </option>
                      <option value="11">
                       11 years
                      </option>
                      <option value="10">
                       10 years
                      </option>
                      <option value="9">
                       9 years
                      </option>
                      <option value="8">
                       8 years
                      </option>
                      <option value="7">
                       7 years
                      </option>
                      <option value="6">
                       6 years
                      </option>
                      <option value="5">
                       5 years
                      </option>
                      <option value="4">
                       4 years
                      </option>
                      <option value="3">
                       3 years
                      </option>
                      <option value="2">
                       2 years
                      </option>
                      <option value="1">
                       1 year
                      </option>
                      <option value="0">
                       0 years
                      </option>
                     </select>
                     <span>
                     </span>
                    </div>
                   </div>
                  </div>
                  <div class="mCalc-DoubleSelect-Wrapper">
                   <label class="label hidden" for="mCalc-TermMonths-mbwu">
                    Months
                   </label>
                   <div class="input-wrapper">
                    <div class="select-field">
                     <select class="large" id="mCalc-TermMonths-mbwu" name="mCalc-TermMonths-mbwu">
                      <option class="option-default" disabled="" value="">
                       Months
                      </option>
                      <option selected="selected" value="0">
                       0 months
                      </option>
                      <option value="1">
                       1 month
                      </option>
                      <option value="2">
                       2 months
                      </option>
                      <option value="3">
                       3 months
                      </option>
                      <option value="4">
                       4 months
                      </option>
                      <option value="5">
                       5 months
                      </option>
                      <option value="6">
                       6 months
                      </option>
                      <option value="7">
                       7 months
                      </option>
                      <option value="8">
                       8 months
                      </option>
                      <option value="9">
                       9 months
                      </option>
                      <option value="10">
                       10 months
                      </option>
                      <option value="11">
                       11 months
                      </option>
                     </select>
                     <span>
                     </span>
                    </div>
                   </div>
                  </div>
                 </div>
                </div>
               </div>
              </fieldset>
             </div>
            </div>
            <div class="row">
             <div class="col-sm-8 col-sm-offset-2 col-md-6 col-md-offset-3 col-lg-4 col-lg-offset-4">
              <ul class="btn-holder">
               <li>
                <button class="btn btn-primary btn-calculate" type="submit">
                 Calculate
                </button>
               </li>
              </ul>
             </div>
            </div>
           </form>
           <div class="mCalc-Cost-ErrorMsg">
           </div>
           <div class="promo-wrapper promo-wrapper-three">
            <article class="promo">
             <div class="promo-content">
              <div class="promo-body">
               <h3 class="promo-title">
                Get an Agreement in Principle
               </h3>
               <p>
                Find out if we can lend the amount you need without affecting your credit score. It usually takes 15 to 30 minutes.
               </p>
              </div>
              <div class="promo-footer">
               <a class="btn btn-primary" data-sitecat="Cost:AipCTA" href="/mortgages/agreement-in-principle/" title="Get an AiP">
                Get an AiP
               </a>
              </div>
             </div>
            </article>
            <article class="promo">
             <div class="promo-content">
              <div class="promo-body">
               <h3 class="promo-title">
                How much can I borrow?
               </h3>
               <p>
                Get a rough idea of how much you may be able to borrow for a property you'll live in.
               </p>
              </div>
              <div class="promo-footer">
               <a class="btn btn-primary" data-sitecat="Cost:BorrowCTA" href="/mortgages/mortgage-calculator/borrowing-calculator/#/borrow/" title="What could I borrow?">
                What could I borrow?
               </a>
              </div>
             </div>
            </article>
            <article class="promo">
             <div class="promo-content">
              <div class="promo-body">
               <h3 class="promo-title">
                Switch to a new rate
               </h3>
               <p>
                If you already have a mortgage with us, take a look at our exclusive rates - there are no legal or valuation fees, and no income assessments.
               </p>
              </div>
              <div class="promo-footer">
               <a class="btn btn-primary" data-sitecat="Cost:RatesCTA" href="/mortgages/existing-customer-centre/" title="See our rates">
                See our rates
               </a>
              </div>
             </div>
            </article>
           </div>
          </div>
          <div class="mCalc-module mCalc-CostResults" style="display: block;">
           <div class="row">
            <div class="col-xs-12">
             <div class="mCalc-SummaryBox">
              <div class="row">
               <div class="col-sm-2 text-right-md">
                <p class="mCalc-SummaryBox-Heading">
                 Your situation
                </p>
               </div>
               <div class="col-sm-8">
                <p aria-level="5" class="mCalc-SummaryBox-Col mCalc-CostResults-SummaryText h5" role="heading">
                 I am looking to
                 <span>
                  buy a first home
                 </span>
                 . My estimated property value is
                 <span>
                  £40,000
                 </span>
                 , my loan amount is
                 <span>
                  £20,000
                 </span>
                 , my term is
                 <span>
                  7 years and 8 months
                 </span>
                 and my payment type is
                 <span>
                  repayment
                 </span>
                 .
                </p>
               </div>
               <div class="col-sm-2 text-right-md">
                <a class="btn btn-sm btn-secondary mCalc-link mCalc-CostResults-Edit" href="#mCalc-Cost">
                 Update
                </a>
               </div>
              </div>
             </div>
            </div>
           </div>
           <div class="mortgage-table-component" data-config-json="/content/dam/json-files/mortgages/mortgage-table-conf-r11.json">
            <div class="amortisation-heading" style="display: none;">
             <div class="summary-container">
              <div class="row">
               <div class="col-sm-3 col-md-2">
                <div class="summary-section text-right-sm">
                 <p aria-level="5" class="summary-heading h5" role="heading">
                  Product
                 </p>
                </div>
               </div>
               <div class="col-sm-9 col-md-4">
                <div class="summary-section h5">
                 <div class="amortisation-mortgage-name">
                 </div>
                 <div class="amortisation-followon-rate">
                 </div>
                </div>
               </div>
               <div class="col-sm-3 col-md-2">
                <div class="summary-section text-right-sm">
                 <p aria-level="5" class="summary-heading h5" role="heading">
                  Monthly payment
                 </p>
                </div>
               </div>
               <div class="col-sm-9 col-md-4">
                <div class="summary-section h5">
                 <div class="amortisation-initial-repayment">
                 </div>
                 <div class="amortisation-followon-repayment">
                 </div>
                </div>
               </div>
              </div>
             </div>
            </div>
            <div class="loading-json-container text-centre hidden">
             <div class="tables-loader">
             </div>
             <h5>
              Loading results. Please wait...
             </h5>
            </div>
            <div class="mortgage-filters-tables" id="mortgageTableTop">
             <div class="mortgage-filters-actions clearfix">
              <p aria-level="5" class="h5 mCalc-CostResults-AvailableText pull-left" data-template="You could apply for  &lt;span&gt;${total} mortgage${pluralS}&lt;/span&gt; " role="heading">
               You could apply for
               <span>
                21 mortgages
               </span>
              </p>
              <p class="mCalc-CostResults-Actions pull-right">
               <a aria-expanded="false" class="mCalc-Terms-Toggle" data-alt-text="Hide mortgage terms" href="#">
                Mortgage terms explained
               </a>
               <a class="btn btn-sm btn-secondary">
                <span class="show-filters">
                 Show filters
                </span>
                <span class="hide-filters">
                 Hide filters
                </span>
               </a>
              </p>
             </div>
             <div aria-hidden="true" class="mCalc-Terms">
              <div class="mCalc-Terms-Container">
               <h4 class="mCalc-Terms-Title">
                Mortgage terms
               </h4>
               <div class="mCalc-Terms-Card">
                <p>
                 <strong>
                  Initial payments and rate
                 </strong>
                </p>
                <p>
                 The monthly payment and rate you'll pay until your introductory period ends.
                </p>
               </div>
               <div class="mCalc-Terms-Card">
                <p>
                 <strong>
                  Follow-on payments and rate
                 </strong>
                </p>
                <p>
                 The payments and rate you'll pay after your introductory period ends if you don’t change anything.
                </p>
               </div>
               <div class="mCalc-Terms-Card">
                <p>
                 <strong>
                  APRC
                 </strong>
                </p>
                <p>
                 Use the annual percentage rate of charge to compare the cost of our mortgages, including interest and fees, with those from other lenders.
                </p>
               </div>
               <div class="mCalc-Terms-Card">
                <p>
                 <strong>
                  Mortgage fee
                 </strong>
                </p>
                <p>
                 You can pay this fee when you submit a mortgage application, or add it to the amount you borrow.
                </p>
               </div>
               <div class="mCalc-Terms-Card">
                <p>
                 <strong>
                  Total of monthly payments
                 </strong>
                </p>
                <p>
                 The information below shows roughly how your monthly payments will affect your mortgage balance over time. But they don't include any other fees or payments you may need to make.
                </p>
               </div>
               <div class="mCalc-Terms-Card">
                <p>
                 <strong>
                  Loan to value
                 </strong>
                </p>
                <p>
                 The percentage of the property value that you're going to borrow. We divide your mortgage amount by the property value to work out the LTV.
                </p>
               </div>
               <div class="mCalc-Terms-Card">
                <p>
                 <strong>
                  Early repayment charge
                 </strong>
                </p>
                <p>
                 The amount you'll pay if you want to pay off the mortgage early or make an overpayment that's more than we've agreed to.
                </p>
               </div>
               <div class="mCalc-Terms-Card">
                <p>
                 <strong>
                  Fixed-rate
                 </strong>
                </p>
                <p>
                 Your rate stays the same for a set period, so your monthly payments remain the same even if our base rate changes.
                </p>
               </div>
               <div class="mCalc-Terms-Card">
                <p>
                 <strong>
                  Tracker
                 </strong>
                </p>
                <p>
                 Your rate is a certain amount above our base rate. If base rate goes up or down, your payments will too (it's sometimes called a 'variable rate').
                </p>
               </div>
               <div class="mCalc-Terms-Card">
                <p>
                 <strong>
                  Offset
                 </strong>
                </p>
                <p>
                 Money you have in another account with us is used to lower the mortgage balance we charge interest on. All our offset mortgages are trackers.
                </p>
               </div>
              </div>
             </div>
             <div class="mortgage-filters">
              <div class="row">
               <div class="col-md-2 col-sm-12">
                <div class="mortgage-filter-section clearfix">
                 <h4 class="heading">
                  Filter your results
                 </h4>
                </div>
               </div>
               <div class="col-md-4 col-sm-12 mortgageTerm-filter" data-table-column="1">
                <div class="mortgage-filter-section clearfix">
                 <h6>
                  Initial period
                 </h6>
                 <input checked="" id="mCalc-Filter-2mortgage-table-21" name="2 years" type="checkbox" value="2"/>
                 <label for="mCalc-Filter-2mortgage-table-21">
                  2 years
                 </label>
                 <input checked="" id="mCalc-Filter-3mortgage-table-21" name="3 years" type="checkbox" value="3"/>
                 <label for="mCalc-Filter-3mortgage-table-21">
                  3 years
                 </label>
                 <input checked="" id="mCalc-Filter-5mortgage-table-21" name="5 years" type="checkbox" value="5"/>
                 <label for="mCalc-Filter-5mortgage-table-21">
                  5 years
                 </label>
                 <input checked="" id="mCalc-Filter-7mortgage-table-21" name="7 years" type="checkbox" value="7"/>
                 <label for="mCalc-Filter-7mortgage-table-21">
                  7 years
                 </label>
                 <input checked="" id="mCalc-Filter-10mortgage-table-21" name="10 years" type="checkbox" value="10"/>
                 <label for="mCalc-Filter-10mortgage-table-21">
                  10 years
                 </label>
                </div>
               </div>
               <div class="col-md-4 col-sm-12 mortgageType-filter" data-table-column="2">
                <div class="mortgage-filter-section clearfix">
                 <h6>
                  Deal type
                 </h6>
                 <input checked="" id="fixed-filtermortgage-table-21" name="Fixed" type="checkbox" value="fixed"/>
                 <label for="fixed-filtermortgage-table-21">
                  Fixed
                 </label>
                 <input checked="" id="tracker-filtermortgage-table-21" name="Tracker/Offset Tracker" type="checkbox" value="tracker"/>
                 <label for="tracker-filtermortgage-table-21">
                  Tracker/Offset Tracker
                 </label>
                </div>
               </div>
               <div class="col-md-2 col-sm-12 freeLegal-filter" data-table-column="5">
                <div class="mortgage-filter-section clearfix">
                 <h6>
                  Charges
                 </h6>
                 <input checked="" id="noFee-filtermortgage-table-21" name="Yes" type="checkbox" value="false"/>
                 <label for="noFee-filtermortgage-table-21">
                  No fee
                 </label>
                 <input checked="" id="fee-filtermortgage-table-21" name="No" type="checkbox" value="true"/>
                 <label for="fee-filtermortgage-table-21">
                  Fee
                 </label>
                </div>
               </div>
              </div>
             </div>
            </div>
            <form action="https://www.apply.barclays.co.uk/forms/onlineaip/gettingstarted" class="mCalc-AIP-Form mod-form" method="POST">
             <input name="enquiryType" type="hidden" value="FTBP"/>
             <input name="repayTermYear" type="hidden" value="7"/>
             <input name="combinedDeposit" type="hidden" value="20000"/>
             <input name="propertyValue" type="hidden" value="40000"/>
             <input name="mortgageAmount" type="hidden" value="20000"/>
             <input name="applicants" type="hidden" value="1"/>
             <div class="dataTables_wrapper" id="mortgage-table-21_wrapper">
              <table class="table table-mortgage display responsive nowrap dataTable dtr-column collapsed" data-rateswitch-type="interest-only" id="mortgage-table-21" role="grid">
               <thead>
                <tr role="row">
                 <th aria-controls="mortgage-table-21" aria-label="
                            Initial payments
                        : activate to sort column ascending" class="all sorting" colspan="1" data-datafield="initialRepayment" rowspan="1" tabindex="0">
                  Initial payments
                  <div class="sorter-wrapper">
                   <span class="sort-arrow-up">
                   </span>
                   <span class="sort-arrow-down">
                   </span>
                  </div>
                 </th>
                 <th aria-controls="mortgage-table-21" aria-label="
                            Mortgage fee
                        : activate to sort column ascending" class="all sorting" colspan="1" data-datafield="applicationFee" data-short-title="Fee" rowspan="1" tabindex="0">
                  Mortgage fee
                  <div class="sorter-wrapper">
                   <span class="sort-arrow-up">
                   </span>
                   <span class="sort-arrow-down">
                   </span>
                  </div>
                 </th>
                 <th aria-controls="mortgage-table-21" aria-label="
                            APRC
                        : activate to sort column ascending" class="all sorting" colspan="1" data-datafield="aprc" rowspan="1" tabindex="0">
                  APRC
                  <div class="sorter-wrapper">
                   <span class="sort-arrow-up">
                   </span>
                   <span class="sort-arrow-down">
                   </span>
                  </div>
                 </th>
                 <th aria-controls="mortgage-table-21" aria-label="
                            Initial rate
                        : activate to sort column ascending" class="tablet-landscape desktop sorting" colspan="1" data-datafield="initialRate" rowspan="1" tabindex="0">
                  Initial rate
                  <div class="sorter-wrapper">
                   <span class="sort-arrow-up">
                   </span>
                   <span class="sort-arrow-down">
                   </span>
                  </div>
                 </th>
                 <th aria-controls="mortgage-table-21" aria-label="
                            Follow-on rate
                        : activate to sort column ascending" class="desktop sorting" colspan="1" data-datafield="followOnRateTitle" rowspan="1" tabindex="0">
                  Follow-on rate
                  <div class="sorter-wrapper">
                   <span class="sort-arrow-up">
                   </span>
                   <span class="sort-arrow-down">
                   </span>
                  </div>
                 </th>
                 <th aria-controls="mortgage-table-21" aria-label="
                            Follow-on payments
                        : activate to sort column ascending" class="none sorting" colspan="1" data-datafield="followOnRepayment" rowspan="1" style="display: none;" tabindex="0">
                  Follow-on payments
                 </th>
                 <th aria-controls="mortgage-table-21" aria-label="
                            Total of monthly payments
                        : activate to sort column ascending" class="none sorting" colspan="1" data-datafield="totalPayment" rowspan="1" style="display: none;" tabindex="0">
                  Total of monthly payments
                 </th>
                 <th aria-controls="mortgage-table-21" aria-label="
                            Loan to value (LTV)
                        : activate to sort column ascending" class="none sorting" colspan="1" data-datafield="howMuchCanBeBorrowedNote" data-short-title="LTV" rowspan="1" style="display: none;" tabindex="0">
                  Loan to value (LTV)
                 </th>
                 <th aria-controls="mortgage-table-21" aria-label="
                            Early repayment charge
                        : activate to sort column ascending" class="none sorting" colspan="1" data-datafield="earlyRepaymentCharges" rowspan="1" style="display: none;" tabindex="0">
                  Early repayment charge
                 </th>
                </tr>
               </thead>
               <tfoot>
                <tr>
                 <th colspan="1" rowspan="1">
                  Initial payments
                 </th>
                 <th colspan="1" rowspan="1">
                  Mortgage fee
                 </th>
                 <th colspan="1" rowspan="1">
                  APRC
                 </th>
                 <th colspan="1" rowspan="1">
                  Initial rate
                 </th>
                 <th colspan="1" rowspan="1">
                  Follow-on rate
                 </th>
                 <th colspan="1" rowspan="1" style="display: none;">
                  Follow-on payments
                 </th>
                 <th colspan="1" rowspan="1" style="display: none;">
                  Total of monthly payments
                 </th>
                 <th colspan="1" rowspan="1" style="display: none;">
                  Loan to value (LTV)
                 </th>
                 <th colspan="1" rowspan="1" style="display: none;">
                  Early repayment charge
                 </th>
                </tr>
               </tfoot>
               <tbody>
                <tr class="group odd">
                 <td colspan="50">
                  <span>
                   1.34%
                  </span>
                  <div class="product-name">
                   2 Year Fixed
                  </div>
                  <div class="product-tools">
                   <a class="" data-product-id="5b7e94d66afad93d467cb3b1" href="javascript:;">
                    <span class="show-more">
                    </span>
                    <span class="more">
                     More details
                    </span>
                    <span class="less">
                     Hide details
                    </span>
                   </a>
                   <input id="16-5b7e94d66afad93d467cb3b1" name="2 Year Fixed" type="checkbox" value="5b7e94d66afad93d467cb3b1"/>
                   <label for="16-5b7e94d66afad93d467cb3b1">
                    Compare
                   </label>
                  </div>
                 </td>
                </tr>
                <tr class="odd hovered" role="row">
                 <td>
                  <div>
                   £228.87
                   <span>
                    (27 months)
                   </span>
                  </div>
                 </td>
                 <td>
                  <div>
                   £999
                   <span>
                   </span>
                  </div>
                 </td>
                 <td>
                  <div>
                   4%
                   <span>
                   </span>
                  </div>
                 </td>
                 <td>
                  <div data-initial-rate="1.34" data-is-offset="undefined">
                   1.34%
                   <span>
                    until 31st January 2023
                   </span>
                  </div>
                 </td>
                 <td>
                  <div>
                   3.59%
                   <span>
                    variable for the remaining term *
                   </span>
                  </div>
                 </td>
                 <td style="display: none;">
                  <div>
                   £243.08
                   <span>
                    for 65 months
                   </span>
                  </div>
                 </td>
                 <td style="display: none;">
                  <div>
                   £21,979.69
                  </div>
                 </td>
                 <td style="display: none;">
                  <div>
                   60%
                   <span>
                    <span>
                     (Min loan £5,000, Max loan £5,000,000)
                    </span>
                   </span>
                  </div>
                 </td>
                 <td style="display: none;">
                  <div>
                   2%
                   <span>
                    of the balance repaid until 31 January 2023
                   </span>
                  </div>
                 </td>
                </tr>
                <tr class="group">
                 <td colspan="50">
                  <span>
                   1.62%
                  </span>
                  <div class="product-name">
                   Residential Premier Exclusive: 7 Year Fixed
                  </div>
                  <div class="product-tools">
                   <a class="" data-product-id="5f4e153195494a8bf33445fb" href="javascript:;">
                    <span class="show-more">
                    </span>
                    <span class="more">
                     More details
                    </span>
                    <span class="less">
                     Hide details
                    </span>
                   </a>
                   <input id="19-5f4e153195494a8bf33445fb" name="Residential Premier Exclusive: 7 Year Fixed" type="checkbox" value="5f4e153195494a8bf33445fb"/>
                   <label for="19-5f4e153195494a8bf33445fb">
                    Compare
                   </label>
                  </div>
                 </td>
                </tr>
                <tr class="even" role="row">
                 <td>
                  <div>
                   £231.32
                   <span>
                    (87 months)
                   </span>
                  </div>
                 </td>
                 <td>
                  <div>
                   £499
                   <span>
                   </span>
                  </div>
                 </td>
                 <td>
                  <div>
                   2.5%
                   <span>
                   </span>
                  </div>
                 </td>
                 <td>
                  <div data-initial-rate="1.62" data-is-offset="undefined">
                   1.62%
                   <span>
                    until 31st January 2028
                   </span>
                  </div>
                 </td>
                 <td>
                  <div>
                   3.59%
                   <span>
                    variable for the remaining term *
                   </span>
                  </div>
                 </td>
                 <td style="display: none;">
                  <div>
                   £231.44
                   <span>
                    for 5 months
                   </span>
                  </div>
                 </td>
                 <td style="display: none;">
                  <div>
                   £21,282.04
                  </div>
                 </td>
                 <td style="display: none;">
                  <div>
                   60%
                   <span>
                    <span>
                     (Min loan £5,000, Max loan £2,000,000)
                    </span>
                   </span>
                  </div>
                 </td>
                 <td style="display: none;">
                  <div>
                   5%
                   <span>
                    of the balance repaid until 31 January 2028
                   </span>
                  </div>
                 </td>
                </tr>
                <tr class="group odd">
                 <td colspan="50">
                  <span>
                   1.65%
                  </span>
                  <div class="product-name">
                   5 Year Fixed
                  </div>
                  <div class="product-tools">
                   <a class="" data-product-id="5f575e2e0f7700dc2f128bb5" href="javascript:;">
                    <span class="show-more">
                    </span>
                    <span class="more">
                     More details
                    </span>
                    <span class="less">
                     Hide details
                    </span>
                   </a>
                   <input id="20-5f575e2e0f7700dc2f128bb5" name="5 Year Fixed" type="checkbox" value="5f575e2e0f7700dc2f128bb5"/>
                   <label for="20-5f575e2e0f7700dc2f128bb5">
                    Compare
                   </label>
                  </div>
                 </td>
                </tr>
                <tr class="odd" role="row">
                 <td>
                  <div>
                   £231.58
                   <span>
                    (63 months)
                   </span>
                  </div>
                 </td>
                 <td>
                  <div>
                   £999
                   <span>
                   </span>
                  </div>
                 </td>
                 <td>
                  <div>
                   3.4%
                   <span>
                   </span>
                  </div>
                 </td>
                 <td>
                  <div data-initial-rate="1.65" data-is-offset="undefined">
                   1.65%
                   <span>
                    until 31st January 2026
                   </span>
                  </div>
                 </td>
                 <td>
                  <div>
                   3.59%
                   <span>
                    variable for the remaining term *
                   </span>
                  </div>
                 </td>
                 <td style="display: none;">
                  <div>
                   £237.09
                   <span>
                    for 29 months
                   </span>
                  </div>
                 </td>
                 <td style="display: none;">
                  <div>
                   £21,465.15
                  </div>
                 </td>
                 <td style="display: none;">
                  <div>
                   60%
                   <span>
                    <span>
                     (Min loan £5,000, Max loan £5,000,000)
                    </span>
                   </span>
                  </div>
                 </td>
                 <td style="display: none;">
                  <div>
                   3%
                   <span>
                    of the balance repaid until 31 January 2026
                   </span>
                  </div>
                 </td>
                </tr>
                <tr class="group">
                 <td colspan="50">
                  <span>
                   1.69%
                  </span>
                  <div class="product-name">
                   2 Year Tracker
                  </div>
                  <div class="product-tools">
                   <a class="" data-product-id="5ecd2a179225587a4c76d5b0" href="javascript:;">
                    <span class="show-more">
                    </span>
                    <span class="more">
                     More details
                    </span>
                    <span class="less">
                     Hide details
                    </span>
                   </a>
                   <input id="17-5ecd2a179225587a4c76d5b0" name="2 Year Tracker" type="checkbox" value="5ecd2a179225587a4c76d5b0"/>
                   <label for="17-5ecd2a179225587a4c76d5b0">
                    Compare
                   </label>
                  </div>
                 </td>
                </tr>
                <tr class="even" role="row">
                 <td>
                  <div>
                   £231.93
                   <span>
                    (24 months)
                   </span>
                  </div>
                 </td>
                 <td>
                  <div>
                   £999
                   <span>
                   </span>
                  </div>
                 </td>
                 <td>
                  <div>
                   4.3%
                   <span>
                   </span>
                  </div>
                 </td>
                 <td>
                  <div data-initial-rate="1.69" data-is-offset="undefined">
                   1.69% (BEBR + 1.59%)
                   <span>
                    variable for 2 years *
                   </span>
                  </div>
                 </td>
                 <td>
                  <div>
                   3.59%
                   <span>
                    variable for the remaining term *
                   </span>
                  </div>
                 </td>
                 <td style="display: none;">
                  <div>
                   £244.53
                   <span>
                    for 68 months
                   </span>
                  </div>
                 </td>
                 <td style="display: none;">
                  <div>
                   £22,194.36
                  </div>
                 </td>
                 <td style="display: none;">
                  <div>
                   60%
                   <span>
                    <span>
                     (Min loan £5,000, Max loan £2,000,000)
                    </span>
                   </span>
                  </div>
                 </td>
                 <td style="display: none;">
                  <div>
                   None
                  </div>
                 </td>
                </tr>
                <tr class="group odd">
                 <td colspan="50">
                  <span>
                   1.72%
                  </span>
                  <div class="product-name">
                   2 Year Offset Tracker
                  </div>
                  <div class="product-tools">
                   <a class="" data-product-id="5ecd2aef9225587a4c76d5b4" href="javascript:;">
                    <span class="show-more">
                    </span>
                    <span class="more">
                     More details
                    </span>
                    <span class="less">
                     Hide details
                    </span>
                   </a>
                   <input id="8-5ecd2aef9225587a4c76d5b4" name="2 Year Offset Tracker" type="checkbox" value="5ecd2aef9225587a4c76d5b4"/>
                   <label for="8-5ecd2aef9225587a4c76d5b4">
                    Compare
                   </label>
                  </div>
                 </td>
                </tr>
                <tr class="odd" role="row">
                 <td>
                  <div>
                   £232.20
                   <span>
                    (24 months)
                   </span>
                  </div>
                 </td>
                 <td>
                  <div>
                   £1749
                   <span>
                   </span>
                  </div>
                 </td>
                 <td>
                  <div>
                   5.5%
                   <span>
                   </span>
                  </div>
                 </td>
                 <td>
                  <div data-initial-rate="1.72" data-is-offset="undefined">
                   1.72% (BEBR + 1.62%)
                   <span>
                    variable for 2 years *
                   </span>
                  </div>
                 </td>
                 <td>
                  <div>
                   3.59%
                   <span>
                    variable for the remaining term *
                   </span>
                  </div>
                 </td>
                 <td style="display: none;">
                  <div>
                   £244.63
                   <span>
                    for 68 months
                   </span>
                  </div>
                 </td>
                 <td style="display: none;">
                  <div>
                   £22,207.64
                  </div>
                 </td>
                 <td style="display: none;">
                  <div>
                   75%
                   <span>
                    <span>
                     (Min loan £5,000, Max loan £2,000,000)
                    </span>
                   </span>
                  </div>
                 </td>
                 <td style="display: none;">
                  <div>
                   Full redemption: 1%
                   <span>
                    of the original balance for 2 years
                   </span>
                  </div>
                 </td>
                </tr>
                <tr class="group">
                 <td colspan="50">
                  <span>
                   1.72%
                  </span>
                  <div class="product-name">
                   2 Year Tracker
                  </div>
                  <div class="product-tools">
                   <a class="" data-product-id="5f8d8eb385ba5be1ed31f910" href="javascript:;">
                    <span class="show-more">
                    </span>
                    <span class="more">
                     More details
                    </span>
                    <span class="less">
                     Hide details
                    </span>
                   </a>
                   <input id="9-5f8d8eb385ba5be1ed31f910" name="2 Year Tracker" type="checkbox" value="5f8d8eb385ba5be1ed31f910"/>
                   <label for="9-5f8d8eb385ba5be1ed31f910">
                    Compare
                   </label>
                  </div>
                 </td>
                </tr>
                <tr class="even" role="row">
                 <td>
                  <div>
                   £232.20
                   <span>
                    (24 months)
                   </span>
                  </div>
                 </td>
                 <td>
                  <div>
                   £999
                   <span>
                   </span>
                  </div>
                 </td>
                 <td>
                  <div>
                   4.3%
                   <span>
                   </span>
                  </div>
                 </td>
                 <td>
                  <div data-initial-rate="1.72" data-is-offset="undefined">
                   1.72% (BEBR + 1.62%)
                   <span>
                    variable for 2 years *
                   </span>
                  </div>
                 </td>
                 <td>
                  <div>
                   3.59%
                   <span>
                    variable for the remaining term *
                   </span>
                  </div>
                 </td>
                 <td style="display: none;">
                  <div>
                   £244.63
                   <span>
                    for 68 months
                   </span>
                  </div>
                 </td>
                 <td style="display: none;">
                  <div>
                   £22,207.64
                  </div>
                 </td>
                 <td style="display: none;">
                  <div>
                   75%
                   <span>
                    <span>
                     (Min loan £5,000, Max loan £2,000,000)
                    </span>
                   </span>
                  </div>
                 </td>
                 <td style="display: none;">
                  <div>
                   None
                  </div>
                 </td>
                </tr>
                <tr class="group odd">
                 <td colspan="50">
                  <span>
                   1.79%
                  </span>
                  <div class="product-name">
                   2 Year Fixed
                  </div>
                  <div class="product-tools">
                   <a class="" data-product-id="5f8d996239ab24f1ef18f242" href="javascript:;">
                    <span class="show-more">
                    </span>
                    <span class="more">
                     More details
                    </span>
                    <span class="less">
                     Hide details
                    </span>
                   </a>
                   <input id="11-5f8d996239ab24f1ef18f242" name="2 Year Fixed" type="checkbox" value="5f8d996239ab24f1ef18f242"/>
                   <label for="11-5f8d996239ab24f1ef18f242">
                    Compare
                   </label>
                  </div>
                 </td>
                </tr>
                <tr class="odd" role="row">
                 <td>
                  <div>
                   £232.81
                   <span>
                    (27 months)
                   </span>
                  </div>
                 </td>
                 <td>
                  <div>
                   £999
                   <span>
                   </span>
                  </div>
                 </td>
                 <td>
                  <div>
                   4.3%
                   <span>
                   </span>
                  </div>
                 </td>
                 <td>
                  <div data-initial-rate="1.79" data-is-offset="undefined">
                   1.79%
                   <span>
                    until 31st January 2023
                   </span>
                  </div>
                 </td>
                 <td>
                  <div>
                   3.59%
                   <span>
                    variable for the remaining term *
                   </span>
                  </div>
                 </td>
                 <td style="display: none;">
                  <div>
                   £244.27
                   <span>
                    for 65 months
                   </span>
                  </div>
                 </td>
                 <td style="display: none;">
                  <div>
                   £22,163.42
                  </div>
                 </td>
                 <td style="display: none;">
                  <div>
                   75%
                   <span>
                    <span>
                     (Min loan £5,000, Max loan £2,000,000)
                    </span>
                   </span>
                  </div>
                 </td>
                 <td style="display: none;">
                  <div>
                   2%
                   <span>
                    of the balance repaid until 31 January 2023
                   </span>
                  </div>
                 </td>
                </tr>
                <tr class="group">
                 <td colspan="50">
                  <span>
                   1.85%
                  </span>
                  <div class="product-name">
                   2 Year Tracker
                  </div>
                  <div class="product-tools">
                   <a class="" data-product-id="5976ffbdb7fa8b526193132b" href="javascript:;">
                    <span class="show-more">
                    </span>
                    <span class="more">
                     More details
                    </span>
                    <span class="less">
                     Hide details
                    </span>
                   </a>
                   <input id="14-5976ffbdb7fa8b526193132b" name="2 Year Tracker" type="checkbox" value="5976ffbdb7fa8b526193132b"/>
                   <label for="14-5976ffbdb7fa8b526193132b">
                    Compare
                   </label>
                  </div>
                 </td>
                </tr>
                <tr class="even" role="row">
                 <td>
                  <div>
                   £233.34
                   <span>
                    (24 months)
                   </span>
                  </div>
                 </td>
                 <td>
                  <div>
                   £0
                   <span>
                   </span>
                  </div>
                 </td>
                 <td>
                  <div>
                   3%
                   <span>
                   </span>
                  </div>
                 </td>
                 <td>
                  <div data-initial-rate="1.85" data-is-offset="undefined">
                   1.85% (BEBR + 1.75%)
                   <span>
                    variable for 2 years *
                   </span>
                  </div>
                 </td>
                 <td>
                  <div>
                   3.59%
                   <span>
                    variable for the remaining term *
                   </span>
                  </div>
                 </td>
                 <td style="display: none;">
                  <div>
                   £244.92
                   <span>
                    for 68 months
                   </span>
                  </div>
                 </td>
                 <td style="display: none;">
                  <div>
                   £22,254.72
                  </div>
                 </td>
                 <td style="display: none;">
                  <div>
                   60%
                   <span>
                    <span>
                     (Min loan £5,000, Max loan £2,000,000)
                    </span>
                   </span>
                  </div>
                 </td>
                 <td style="display: none;">
                  <div>
                   1%
                   <span>
                    of the balance repaid for the initial 2 year period
                   </span>
                  </div>
                 </td>
                </tr>
                <tr class="group odd">
                 <td colspan="50">
                  <span>
                   1.89%
                  </span>
                  <div class="product-name">
                   5 Year Fixed (Purchase Only)
                  </div>
                  <div class="product-tools">
                   <a class="" data-product-id="5f4e13bf95494a8bf33445f7" href="javascript:;">
                    <span class="show-more">
                    </span>
                    <span class="more">
                     More details
                    </span>
                    <span class="less">
                     Hide details
                    </span>
                   </a>
                   <input id="18-5f4e13bf95494a8bf33445f7" name="5 Year Fixed (Purchase Only)" type="checkbox" value="5f4e13bf95494a8bf33445f7"/>
                   <label for="18-5f4e13bf95494a8bf33445f7">
                    Compare
                   </label>
                  </div>
                 </td>
                </tr>
                <tr class="odd" role="row">
                 <td>
                  <div>
                   £233.69
                   <span>
                    (63 months)
                   </span>
                  </div>
                 </td>
                 <td>
                  <div>
                   £0
                   <span>
                   </span>
                  </div>
                 </td>
                 <td>
                  <div>
                   2.2%
                   <span>
                   </span>
                  </div>
                 </td>
                 <td>
                  <div data-initial-rate="1.89" data-is-offset="undefined">
                   1.89%
                   <span>
                    until 31st January 2026
                   </span>
                  </div>
                 </td>
                 <td>
                  <div>
                   3.59%
                   <span>
                    variable for the remaining term *
                   </span>
                  </div>
                 </td>
                 <td style="display: none;">
                  <div>
                   £238.50
                   <span>
                    for 29 months
                   </span>
                  </div>
                 </td>
                 <td style="display: none;">
                  <div>
                   £21,638.97
                  </div>
                 </td>
                 <td style="display: none;">
                  <div>
                   60%
                   <span>
                    <span>
                     (Min loan £5,000, Max loan £5,000,000)
                    </span>
                   </span>
                  </div>
                 </td>
                 <td style="display: none;">
                  <div>
                   3%
                   <span>
                    of the balance repaid until 31 January 2026
                   </span>
                  </div>
                 </td>
                </tr>
                <tr class="group">
                 <td colspan="50">
                  <span>
                   1.89%
                  </span>
                  <div class="product-name">
                   5 Year Fixed
                  </div>
                  <div class="product-tools">
                   <a class="" data-product-id="5f8d9b9139ab24f1ef18f244" href="javascript:;">
                    <span class="show-more">
                    </span>
                    <span class="more">
                     More details
                    </span>
                    <span class="less">
                     Hide details
                    </span>
                   </a>
                   <input id="12-5f8d9b9139ab24f1ef18f244" name="5 Year Fixed" type="checkbox" value="5f8d9b9139ab24f1ef18f244"/>
                   <label for="12-5f8d9b9139ab24f1ef18f244">
                    Compare
                   </label>
                  </div>
                 </td>
                </tr>
                <tr class="even" role="row">
                 <td>
                  <div>
                   £233.69
                   <span>
                    (63 months)
                   </span>
                  </div>
                 </td>
                 <td>
                  <div>
                   £999
                   <span>
                   </span>
                  </div>
                 </td>
                 <td>
                  <div>
                   3.6%
                   <span>
                   </span>
                  </div>
                 </td>
                 <td>
                  <div data-initial-rate="1.89" data-is-offset="undefined">
                   1.89%
                   <span>
                    until 31st January 2026
                   </span>
                  </div>
                 </td>
                 <td>
                  <div>
                   3.59%
                   <span>
                    variable for the remaining term *
                   </span>
                  </div>
                 </td>
                 <td style="display: none;">
                  <div>
                   £238.50
                   <span>
                    for 29 months
                   </span>
                  </div>
                 </td>
                 <td style="display: none;">
                  <div>
                   £21,638.97
                  </div>
                 </td>
                 <td style="display: none;">
                  <div>
                   75%
                   <span>
                    <span>
                     (Min loan £5,000, Max loan £2,000,000)
                    </span>
                   </span>
                  </div>
                 </td>
                 <td style="display: none;">
                  <div>
                   3%
                   <span>
                    of the balance repaid until 31 January 2026
                   </span>
                  </div>
                 </td>
                </tr>
               </tbody>
              </table>
             </div>
             <p style="margin-top:30px;">
              The information below shows roughly how your monthly payments will affect your mortgage balance over time. But they don't include any other fees or payments you may need to make.
             </p>
             <div class="table-mortgage-amortisation-container hidden">
              <h4 class="amortisation-title">
              </h4>
              <div class="table-shadow no-shadow">
               <table class="table table-mortgage table-mortgage-amortisation">
                <thead>
                 <tr>
                  <th>
                   id
                  </th>
                  <th class="all" data-datafield="year">
                   Year
                  </th>
                  <th class="all" data-datafield="annualPayment">
                   Annual payment
                  </th>
                  <th class="tablet-l desktop" data-datafield="repayment">
                   Mortgage balance repaid
                  </th>
                  <th class="tablet-l desktop" data-datafield="interest">
                   Interest repaid
                  </th>
                  <th class="all" data-datafield="balance">
                   Remaining balance
                  </th>
                 </tr>
                </thead>
                <tbody>
                </tbody>
                <tfoot>
                 <tr>
                  <th>
                   id
                  </th>
                  <th>
                   Year
                  </th>
                  <th>
                   Annual payment
                  </th>
                  <th>
                   Mortgage balance repaid
                  </th>
                  <th>
                   Interest repaid
                  </th>
                  <th>
                   Remaining balance
                  </th>
                 </tr>
                </tfoot>
               </table>
              </div>
              <ul class="btn-holder text-centre-md">
               <li>
                <a class="btn btn-secondary back-button-amortisation">
                 See all products
                </a>
               </li>
               <li>
                <a class="btn btn-primary btn-aip" href="/mortgages/agreement-in-principle">
                 Get Agreement in Principle
                </a>
               </li>
              </ul>
             </div>
             <div class="table-mortgage-compare-container hidden">
              <h4 class="comparison-title">
              </h4>
              <div class="table-shadow no-shadow">
               <table class="table table-mortgage-compare">
                <thead>
                </thead>
                <tbody>
                </tbody>
                <tfoot>
                </tfoot>
               </table>
              </div>
             </div>
             <div class="sticky-anchor">
             </div>
             <div class="compare-button-wrapper sticky hidden stick" style="">
              <a class="btn btn-secondary compare-button">
              </a>
              <a class="btn btn-secondary back-button hidden">
               See all products
              </a>
             </div>
             <div class="mortgage-pagination text-centre-md">
              <button class="btn btn-primary mortgage-pagination-all">
               Show all 21 mortgages
              </button>
             </div>
            </form>
           </div>
           <div class="promo-wrapper promo-wrapper-three">
            <article class="promo">
             <div class="promo-content">
              <div class="promo-body">
               <h3 class="promo-title">
                Get an Agreement in Principle
               </h3>
               <p>
                Find out if we can lend the amount you need without affecting your credit score. It usually takes 15 to 30 minutes.
               </p>
              </div>
              <div class="promo-footer">
               <a class="btn btn-secondary" data-sitecat="CostResults:AipCTA" href="/mortgages/agreement-in-principle/" title="Get an AiP">
                Get an AiP
               </a>
              </div>
             </div>
            </article>
            <article class="promo">
             <div class="promo-content">
              <div class="promo-body">
               <h3 class="promo-title">
                How much can I borrow?
               </h3>
               <p>
                Get a rough idea of how much you may be able to borrow for a property you'll live in.
               </p>
              </div>
              <div class="promo-footer">
               <a class="btn btn-secondary" data-sitecat="CostResults:BorrowCTA" href="/mortgages/mortgage-calculator/borrowing-calculator/#/borrow/" title="What could I borrow?">
                What could I borrow?
               </a>
              </div>
             </div>
            </article>
            <article class="promo">
             <div class="promo-content">
              <div class="promo-body">
               <h3 class="promo-title">
                Switch to a new rate
               </h3>
               <p>
                If you already have a mortgage with us, take a look at our exclusive rates - there are no legal or valuation fees, and no income assessments.
               </p>
              </div>
              <div class="promo-footer">
               <a class="btn btn-secondary" data-sitecat="CostResults:RatesCTA" href="/mortgages/existing-customer-centre/" title="See our rates">
                See our rates
               </a>
              </div>
             </div>
            </article>
           </div>
          </div>
          <div class="mCalc-Loading-Container">
           <div class="mCalc-Loading-Spinner">
           </div>
          </div>
         </div>
        </div>
       </div>
      </div>
     </div>
    </section>
    <section class="wrapper">
     <div class="container-fluid">
      <div class="row">
       <div class="col-xs-12">
        <div class="row">
         <div class="col-sm-6 col-sm-offset-3">
          <div class="wrapper-heading">
           <h2>
            Cover for the things that matter most
           </h2>
           <div class="aem-rte">
           </div>
          </div>
         </div>
        </div>
        <div class="promo-wrapper promo-wrapper-two">
         <article class="promo multi">
          <div class="promo-media">
           <picture>
            <source media="(min-width: 1024px)" srcset="/content/dam/lifestyle-images/personal/insurance/Home_Insurance_Defaqto_Expert_Rated_16_9.small.medium_quality.jpg">
             <source media="(min-width: 480px)" srcset="/content/dam/lifestyle-images/personal/insurance/Home_Insurance_Defaqto_Expert_Rated_16_9.xsmall.medium_quality.jpg">
              <source srcset="/content/dam/lifestyle-images/personal/insurance/Home_Insurance_Defaqto_Expert_Rated_16_9.xxsmall.medium_quality.jpg">
               <img alt="" role="presentation" src="/content/dam/lifestyle-images/personal/insurance/Home_Insurance_Defaqto_Expert_Rated_16_9.xsmall.medium_quality.jpg"/>
              </source>
             </source>
            </source>
           </picture>
          </div>
          <div class="promo-content">
           <div class="promo-body">
            <h3>
             Barclays Home Insurance
            </h3>
            <div class="aem-rte">
             <p>
              Get Defaqto 5 Star-rated buildings and contents cover by answering just a few simple questions. Our home insurance gives you a range of cover options and, with our award-winning customer service, you know you’re in safe hands.
             </p>
            </div>
           </div>
           <div class="promo-footer">
            <div class="o-buttons o-buttons--full-width-xs" data-component-type="CTA">
             <div class="o-buttons__item">
              <a class="m-button aem-button m-button--default m-button--full-width m-button--primary" data-add-query-params="false" href="/insurance/home-insurance/" role="button">
               <span class="m-button__text aem-button__text">
                Explore home insurance
               </span>
              </a>
             </div>
            </div>
           </div>
          </div>
         </article>
         <article class="promo multi">
          <div class="promo-media">
           <picture>
            <source media="(min-width: 1024px)" srcset="/content/dam/lifestyle-images/personal/insurance/life_insurance_family_16_9.small.medium_quality.jpg">
             <source media="(min-width: 480px)" srcset="/content/dam/lifestyle-images/personal/insurance/life_insurance_family_16_9.xsmall.medium_quality.jpg">
              <source srcset="/content/dam/lifestyle-images/personal/insurance/life_insurance_family_16_9.xxsmall.medium_quality.jpg">
               <img alt="" role="presentation" src="/content/dam/lifestyle-images/personal/insurance/life_insurance_family_16_9.xsmall.medium_quality.jpg"/>
              </source>
             </source>
            </source>
           </picture>
          </div>
          <div class="promo-content">
           <div class="promo-body">
            <h3>
             Life insurance for mortgage holders
            </h3>
            <div class="aem-rte">
             <p>
              You could consider taking out life, or life and critical illness insurance alongside your mortgage. These covers are designed to offer some financial protection against the unexpected. Your loved ones would receive a lump-sum payment if you died and, depending on your cover, could receive a lump sum if you were diagnosed with a critical illness, which could help repay your mortgage.
             </p>
            </div>
           </div>
           <div class="promo-footer">
            <div class="o-buttons o-buttons--full-width-xs" data-component-type="CTA">
             <div class="o-buttons__item">
              <a class="m-button aem-button m-button--default m-button--full-width m-button--primary" data-add-query-params="false" href="/insurance/life-insurance/barclays-life-insurance-for-mortgage-holders/" role="button">
               <span class="m-button__text aem-button__text">
                Explore life insurance
               </span>
              </a>
             </div>
            </div>
           </div>
          </div>
         </article>
        </div>
       </div>
      </div>
     </div>
    </section>
    <section class="wrapper">
     <div class="container-fluid">
      <div class="row">
       <div class="col-xs-12">
        <div class="row">
         <div class="col-sm-6 col-sm-offset-3">
          <div class="wrapper-heading">
           <h2>
            Need some help?
           </h2>
           <div class="aem-rte">
           </div>
          </div>
         </div>
        </div>
        <div class="promo-wrapper promo-wrapper-two">
         <article class="promo multi">
          <div class="promo-content">
           <div class="promo-body">
            <h3>
             Chat to us online
            </h3>
            <div class="aem-rte">
             <p>
              Chat to us online if you have a question about using our mortgage calculator.
              <br/>
             </p>
            </div>
           </div>
           <div class="promo-footer">
            <div class="o-buttons o-buttons--full-width-xs" data-component-type="CTA">
             <div class="o-buttons__item">
              <a class="m-button aem-button m-button--default m-button--full-width m-button--primary" data-add-query-params="false" href="https://unauth.chat.secure.barclays.com/captureDetails.html?product=Mortgage1&amp;pagename=ManageMortgageOnline" role="button" target="_blank">
               <span class="m-button__text aem-button__text">
                Start web chat
               </span>
              </a>
             </div>
            </div>
           </div>
          </div>
         </article>
         <article class="promo multi">
          <div class="promo-media">
          </div>
          <div class="promo-content">
           <div class="promo-body">
            <h3 class="promo-title">
             Call us
            </h3>
            <h4>
             0333 202 7580
             <br/>
            </h4>
            <p>
             Lines are open 8am to 8pm, every day. To maintain a quality service, we may monitor and record phone calls.
             <a href="https://www.barclays.co.uk/Generalinformation/Readourcallchargesandinformation/P1242558125005" target="_blank" title="Opens in a new window">
              Call charges
             </a>
             .
            </p>
           </div>
           <div class="promo-footer">
           </div>
          </div>
         </article>
        </div>
       </div>
      </div>
     </div>
    </section>
    <section class="wrapper hidden" id="legal-statements">
     <div class="container-fluid">
      <div class="row">
       <div class="col-sm-6 col-sm-offset-3 wrapper-heading">
        <h2>
         Important information
        </h2>
       </div>
       <div class="row">
        <div class="col-xs-12">
         <div id="legals-placeholder">
         </div>
        </div>
       </div>
      </div>
     </div>
    </section>
   </div>
  </main>
  <div class="footer iparsys parsys">
   <div class="section">
    <div class="new">
    </div>
   </div>
   <div class="iparys_inherited">
    <div class="footer iparsys parsys">
     <div class="reference parbase section">
      <div>
       <footer class="footer" id="globalfooter">
        <!-- Placeholder <a> tag to ensure footer receives focus with skip link -->
        <div class="skipwrapper">
         <a id="skip-main" name="skip-main">
          -
         </a>
        </div>
        <div aria-label="Footer navigation" class="footer-links" role="navigation">
         <div class="container-fluid">
          <div class="row">
           <div class="col-xs-6 col-md-3 col-lg-2 col-lg-offset-2">
            <div class="links" data-component-type="Footer">
             <ul data-component-type="Link">
              <li>
               <a href="/current-accounts/" target="_self" title="Current accounts">
                Current accounts
               </a>
              </li>
              <li>
               <a href="/savings/" target="_self" title="Savings accounts">
                Savings accounts
               </a>
              </li>
              <li>
               <a href="/savings/isas/" target="_self" title="ISAs">
                ISAs
               </a>
              </li>
              <li>
               <a href="/loans/" target="_self" title="Loans">
                Loans
               </a>
              </li>
              <li>
               <a href="/mortgages/" target="_self" title="Mortgages">
                Mortgages
               </a>
              </li>
              <li>
               <a href="/mortgages/mortgage-calculator/" target="_self" title="Mortgage calculator">
                Mortgage calculator
               </a>
              </li>
              <li>
               <a href="/insurance/" target="_self" title="Insurance">
                Insurance
               </a>
              </li>
              <li>
               <a href="/credit-cards/" target="_self" title="Credit cards">
                Credit cards
               </a>
              </li>
              <li>
               <a href="/insurance/home-insurance/" target="_self" title="Home and contents insurance">
                Home and contents insurance
               </a>
              </li>
             </ul>
            </div>
           </div>
           <div class="col-xs-6 col-md-3 col-lg-2">
            <div class="links" data-component-type="Footer">
             <ul data-component-type="Link">
              <li>
               <a href="/help/" target="_self" title="Help and FAQs">
                Help and FAQs
               </a>
              </li>
              <li>
               <a href="/current-accounts/switch-bank-account/" target="_self" title="Switch to Barclays">
                Switch to Barclays
               </a>
              </li>
              <li>
               <a href="/digisafe/reporting-fraud/" target="_self" title="How to report fraud">
                How to report fraud
               </a>
              </li>
              <li>
               <a href="/digisafe/financial-fraud/" target="_self" title="Protect your money">
                Protect your money
               </a>
              </li>
             </ul>
            </div>
           </div>
           <div class="col-xs-6 col-md-3 col-lg-2">
            <div class="links" data-component-type="Footer">
             <ul data-component-type="Link">
              <li>
               <a href="/important-information/" target="_self" title="Important information">
                Important information
               </a>
              </li>
              <li>
               <a href="/accessibility/" target="_blank" title="Accessibility">
                Accessibility
               </a>
              </li>
              <li>
               <a href="/important-information/privacy-policy/" target="_self" title="Privacy policy">
                Privacy policy
               </a>
              </li>
              <li>
               <a href="/important-information/cookies-policy/" target="_self" title="Cookies">
                Cookies
               </a>
              </li>
              <li>
               <a href="/digisafe/" target="_self" title="Security">
                Security
               </a>
              </li>
              <li>
               <a href="https://jobs.barclays.co.uk/" target="_blank" title="Careers">
                Careers
               </a>
              </li>
             </ul>
            </div>
           </div>
           <div class="col-xs-6 col-md-3 col-lg-2">
            <div class="links" data-component-type="Footer">
             <ul data-component-type="Link">
              <li>
               <a href="/branch-finder/" target="_self" title="Find a branch">
                Find a branch
               </a>
              </li>
              <li>
               <a href="https://status.uk.barclays/" target="_self" title="Service status">
                Service status
               </a>
              </li>
              <li>
               <a href="/help/customer-services/contact_service/" target="_self" title="Send us a message">
                Send us a message
               </a>
              </li>
              <li>
               <a href="http://www.m.me/barclaysuk" target="_self" title="Chat online now">
                Chat online now
               </a>
              </li>
              <li>
               <a href="https://twitter.com/barclaysukhelp" target="_blank" title="Find us on Twitter">
                Find us on Twitter
               </a>
              </li>
             </ul>
            </div>
           </div>
          </div>
         </div>
        </div>
        <div class="footer-legal" role="contentinfo">
         <div class="container-fluid">
          <div class="row">
           <div class="col-md-8 col-md-offset-2 legal">
            <div class="text section">
             <div class="aem-rte">
              <p style="text-align: center;">
               Fees may be charged for our products and services.
              </p>
              <p style="text-align: center;">
               Barclays Bank UK PLC and Barclays Bank PLC are each authorised by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the Prudential Regulation Authority.
              </p>
              <p style="text-align: center;">
               Barclays Insurance Services Company Limited and Barclays Investment Solutions Limited are each authorised and regulated by the Financial Conduct Authority.
              </p>
              <p style="text-align: center;">
               Registered office for all: 1 Churchill Place, London E14 5HP
              </p>
             </div>
            </div>
           </div>
           <div class="col-xs-12 col-md-8 col-md-offset-2 sponsors">
            <div class="ftr-img-contnr text-centre">
             <div class="image parbase section">
              <div data-component-type="Image">
               <a class="no-text-decoration" data-component-type="Image" href="https://www.fscs.org.uk/" target="_blank" title="Opens in a new window">
                <picture>
                 <source media="(min-width: 1440px)" srcset="/content/dam/lifestyle-images/personal/miscellaneous/FSCS_logo_v3.large.medium_quality.jpg">
                  <source media="(min-width: 1024px)" srcset="/content/dam/lifestyle-images/personal/miscellaneous/FSCS_logo_v3.medium.medium_quality.jpg">
                   <source media="(min-width: 768px)" srcset="/content/dam/lifestyle-images/personal/miscellaneous/FSCS_logo_v3.small.medium_quality.jpg">
                    <source media="(min-width: 480px)" srcset="/content/dam/lifestyle-images/personal/miscellaneous/FSCS_logo_v3.xsmall.medium_quality.jpg">
                     <source srcset="/content/dam/lifestyle-images/personal/miscellaneous/FSCS_logo_v3.xxsmall.medium_quality.jpg">
                      <img alt="fscs protected" class="adaptive-image" src="/content/dam/lifestyle-images/personal/miscellaneous/FSCS_logo_v3.full.high_quality.jpg"/>
                     </source>
                    </source>
                   </source>
                  </source>
                 </source>
                </picture>
               </a>
              </div>
             </div>
             <div class="image parbase section">
              <div data-component-type="Image">
               <a class="no-text-decoration" data-component-type="Image" href="https://www.bsigroup.com/en-GB/" target="_blank" title="Opens in a new window">
                <picture>
                 <source media="(min-width: 1440px)" srcset="/content/dam/lifestyle-images/personal/miscellaneous/Kitemark_logo_v3.large.medium_quality.jpg">
                  <source media="(min-width: 1024px)" srcset="/content/dam/lifestyle-images/personal/miscellaneous/Kitemark_logo_v3.medium.medium_quality.jpg">
                   <source media="(min-width: 768px)" srcset="/content/dam/lifestyle-images/personal/miscellaneous/Kitemark_logo_v3.small.medium_quality.jpg">
                    <source media="(min-width: 480px)" srcset="/content/dam/lifestyle-images/personal/miscellaneous/Kitemark_logo_v3.xsmall.medium_quality.jpg">
                     <source srcset="/content/dam/lifestyle-images/personal/miscellaneous/Kitemark_logo_v3.xxsmall.medium_quality.jpg">
                      <img alt="bsi. Secure Digital Transactions. KITEMARK. Certificate number KM 616800" class="adaptive-image" src="/content/dam/lifestyle-images/personal/miscellaneous/Kitemark_logo_v3.full.high_quality.jpg"/>
                     </source>
                    </source>
                   </source>
                  </source>
                 </source>
                </picture>
               </a>
              </div>
             </div>
            </div>
           </div>
          </div>
         </div>
        </div>
       </footer>
      </div>
     </div>
    </div>
   </div>
  </div>
  <div class="section">
   <div class="new">
   </div>
  </div>
  <div class="iparys_inherited">
   <div class="custom_tags_footer_sitewide iparsys parsys">
   </div>
  </div>
  <script type="text/javascript">
   var bcpublic = bcpublic || {};
      bcpublic.helpandsupport = bcpublic.helpandsupport || {};
      bcpublic.helpandsupport.rootConfig = {
 "cookieWebchat": [],
 "cookieNav": [],
 "cookieSegment": [],
 "cookieSecure": [],
 "cookieColleague": []
 };
  </script>
  <script src="/etc/designs/componentlibrary/clientlib/js/libs/jquery.datatables.min.js">
  </script>
  <!-- TEST : theme.barclays -->
  <script src="/etc/designs/bdl1.7.4/clientlib.js" type="text/javascript">
  </script>
  <script src="/etc/designs/componentlibrary/componentlibraryBundle/clientlib.js" type="text/javascript">
  </script>
  <script src="/etc/designs/componentlibrary/profilecookie/clientlib.js" type="text/javascript">
  </script>
  <script src="/etc/designs/componentlibrary/clientlib.js" type="text/javascript">
  </script>
  <script src="/etc/designs/componentlibrary/commonlibs.js" type="text/javascript">
  </script>
  <script src="/etc/designs/bdl-next/clientlib.js" type="text/javascript">
  </script>
  <script src="/etc/designs/componentlibrary/theme.barclays/clientlib.js" type="text/javascript">
  </script>
  <script data-account="barukprod" data-channel="UKRBB" data-cookiedomainperiod="3" id="code-cookies-js">
   barclays.privacy.gateway({
            'cat': 'cat2',
            'code': '%3Cscript%20src%3D%22%2Fetc%2Fdesigns%2Fcomponentlibrary%2Fsitecatalyst%2Fs_codecookiesv2.js%22%3E%3C%2Fscript%3E',
            'replace': ''
        });
  </script>
  <script>
   var items = 'Personal,Mortgages,MortgageCalculator,CostCalculator'.split(',');
        var pageDepth = items.length;
        var querystring = window.location.search;

        if (querystring.charAt(0) === '?')
            querystring = querystring.substr(1);

        if (typeof s !== 'undefined') {
            // Branch finder changes
            if ((typeof branchFinder !== 'undefined') && branchFinder && branchFinder.analyticsPageHeader) {
                s.pageName = branchFinder.analyticsPageHeader;
                s.prop1 = "Public";
                s.prop2 = branchFinder.analyticsPageHeader;
            } else {
                s.pageName = items.join(':');
                s.prop1 = items[0];
                s.prop2 = pageDepth > 1 ? items.slice(0, 2).join(':') : '';
                s.prop3 = pageDepth > 2 ? items.slice(0, 3).join(':') : '';
            }


            s.prop16 = window.location.pathname;
            s.prop39 = 'Public';
            s.prop70 = window.location.protocol + '//' + window.location.host;
            s.prop71 = querystring;
            s.prop72 = window.location.hash;
            s.eVar41 = s.pageName;
            events = 'event20';

        }
  </script>
  <script>
   barclays.privacy.gateway({
        'cat': 'cat2',
        'code': '%3Cscript%20type%3D%22text%2Fjavascript%22%3E%0D%0A%0D%0Avar%20s_code%3Ds.t%28%29%3B%0D%0A%0D%0Aif%20%28s_code%29document.write%28s_code%29%3B%0D%0A%0D%0A%3C%2Fscript%3E',
        'replace': ''
    });
  </script>
  <script src="/etc/designs/componentlibrary/sitecatalyst/linktracking.js">
  </script>
  <!-- this is the page sub footer libs -->
  <noscript>
   <img src="https://www.barclays.co.uk/akam/11/pixel_7000b060?a=dD01MDExNzg5MWEyOTljMDgwODRhNjhhNWQzZjU1MDk1MGNlMWU4OTYwJmpzPW9mZg==" style="visibility: hidden; position: absolute; left: -999px; top: -999px;"/>
  </noscript>
 </body>
</html>


'''
html_soup = BeautifulSoup(soup,'lxml')
container = html_soup.find('div', class_='dataTables_wrapper')
tbody = container.find('tbody')
tr_tag = tbody.find_all('tr', class_='child odd')
print(tr_tag)
