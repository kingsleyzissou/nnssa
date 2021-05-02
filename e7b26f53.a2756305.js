(window.webpackJsonp=window.webpackJsonp||[]).push([[65],{133:function(e,t,n){"use strict";n.r(t),n.d(t,"frontMatter",(function(){return i})),n.d(t,"metadata",(function(){return s})),n.d(t,"toc",(function(){return c})),n.d(t,"default",(function(){return u}));var r=n(3),a=n(7),o=(n(0),n(143)),i={id:"sr",title:"Sampling Rate",sidebar_label:"Sampling Rate",slug:"/sampling-rate"},s={unversionedId:"sr",id:"version-status-report/sr",isDocsHomePage:!1,title:"Sampling Rate",description:"How an increase in sample rate produces a more accurate digital representation of an analogue sound signal (Brown, 2019)",source:"@site/versioned_docs/version-status-report/sr.md",slug:"/sampling-rate",permalink:"/docs/status-report/sampling-rate",editUrl:"https://github.com/kingsleyzissou/nnssa/edit/master/website/versioned_docs/version-status-report/sr.md",version:"status-report",sidebar_label:"Sampling Rate",sidebar:"version-status-report/someSidebar",previous:{title:"Frequency",permalink:"/docs/status-report/frequency"},next:{title:"Time Domain",permalink:"/docs/status-report/time-domain"}},c=[],l={toc:c};function u(e){var t=e.components,n=Object(a.a)(e,["components"]);return Object(o.b)("wrapper",Object(r.a)({},l,n,{components:t,mdxType:"MDXLayout"}),Object(o.b)("p",null,Object(o.b)("img",Object(r.a)({parentName:"p"},{src:"https://www.izotope.com/en/learn/digital-audio-basics-sample-rate-and-bit-depth/_jcr_content/root/sectioncontainer_main/flexcontainer/flexcontainer_center/flexcontainer_center_top/image_1558274996.coreimg.82.1280.jpeg/1590799241393/reconstructing-the-original-signal.jpeg",alt:null}))),Object(o.b)("p",null,Object(o.b)("em",{parentName:"p"},"How an increase in sample rate produces a more accurate digital representation of an analogue sound signal (Brown, 2019)")),Object(o.b)("p",null,"Analogue sound signals are continuous, while their digital recreations are discrete. To overcome this issue, a number of samples of the analogue signal are taken per second to digitally recreate the sound. The number of samples per second is known as the sampling rate, measured in Hertz (Brown, 2019)."),Object(o.b)("p",null,"The highest frequency audible to the human ear is around 20,000Hz. The highest frequency that can be accurately represented digitally is given by the sampling rate divided by two. This is known as the Nyquist frequency which stems from the Nyquist theorem. An example of this theory in practice is CD quality audio, which has a sampling rate of 44,100Hz. The reason for the choice of sampling rate given by the inventors at Sony was that it matched the sampling rate used in Sony\u2019s video technology for their PCM-1600 adapter (Doi, Itoh and Ogawa, 1979), resulting in a Nyquist frequency greater than the human hearing range (Oshana, 2006)."))}u.isMDXComponent=!0},143:function(e,t,n){"use strict";n.d(t,"a",(function(){return p})),n.d(t,"b",(function(){return f}));var r=n(0),a=n.n(r);function o(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function i(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);t&&(r=r.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,r)}return n}function s(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?i(Object(n),!0).forEach((function(t){o(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):i(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function c(e,t){if(null==e)return{};var n,r,a=function(e,t){if(null==e)return{};var n,r,a={},o=Object.keys(e);for(r=0;r<o.length;r++)n=o[r],t.indexOf(n)>=0||(a[n]=e[n]);return a}(e,t);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);for(r=0;r<o.length;r++)n=o[r],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(a[n]=e[n])}return a}var l=a.a.createContext({}),u=function(e){var t=a.a.useContext(l),n=t;return e&&(n="function"==typeof e?e(t):s(s({},t),e)),n},p=function(e){var t=u(e.components);return a.a.createElement(l.Provider,{value:t},e.children)},m={inlineCode:"code",wrapper:function(e){var t=e.children;return a.a.createElement(a.a.Fragment,{},t)}},d=a.a.forwardRef((function(e,t){var n=e.components,r=e.mdxType,o=e.originalType,i=e.parentName,l=c(e,["components","mdxType","originalType","parentName"]),p=u(n),d=r,f=p["".concat(i,".").concat(d)]||p[d]||m[d]||o;return n?a.a.createElement(f,s(s({ref:t},l),{},{components:n})):a.a.createElement(f,s({ref:t},l))}));function f(e,t){var n=arguments,r=t&&t.mdxType;if("string"==typeof e||r){var o=n.length,i=new Array(o);i[0]=d;var s={};for(var c in t)hasOwnProperty.call(t,c)&&(s[c]=t[c]);s.originalType=e,s.mdxType="string"==typeof e?e:r,i[1]=s;for(var l=2;l<o;l++)i[l]=n[l];return a.a.createElement.apply(null,i)}return a.a.createElement.apply(null,n)}d.displayName="MDXCreateElement"}}]);