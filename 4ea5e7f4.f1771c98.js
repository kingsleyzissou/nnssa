(window.webpackJsonp=window.webpackJsonp||[]).push([[36],{104:function(e,t,r){"use strict";r.r(t),r.d(t,"frontMatter",(function(){return a})),r.d(t,"metadata",(function(){return c})),r.d(t,"toc",(function(){return s})),r.d(t,"default",(function(){return p}));var n=r(3),i=r(7),o=(r(0),r(143)),a={id:"metrics",title:"Metrics",sidebar_label:"Metrics",slug:"/metrics"},c={unversionedId:"metrics",id:"version-final-report/metrics",isDocsHomePage:!1,title:"Metrics",description:"The image above highlights the difference between accuracy and precision (Miessler, 2019)",source:"@site/versioned_docs/version-final-report/metrics.md",slug:"/metrics",permalink:"/docs/metrics",editUrl:"https://github.com/kingsleyzissou/nnssa/edit/master/website/versioned_docs/version-final-report/metrics.md",version:"final-report",sidebar_label:"Metrics",sidebar:"version-final-report/someSidebar",previous:{title:"Digital Signal Processing 201",permalink:"/docs/dsp_201"},next:{title:"Imbalanced Data",permalink:"/docs/imbalance"}},s=[{value:"Accuracy",id:"accuracy",children:[]},{value:"Precision",id:"precision",children:[]}],l={toc:s};function p(e){var t=e.components,a=Object(i.a)(e,["components"]);return Object(o.b)("wrapper",Object(n.a)({},l,a,{components:t,mdxType:"MDXLayout"}),Object(o.b)("p",null,Object(o.b)("img",{src:r(210).default})),Object(o.b)("p",null,Object(o.b)("em",{parentName:"p"},"The image above highlights the difference between accuracy and precision (Miessler, 2019)")),Object(o.b)("p",null,"Metrics are an important key in understanding the performance of a model. It is necessary to cover this to gain an understanding of the metrics used to measure a neural network model and understand the literature review in the following section."),Object(o.b)("h2",{id:"accuracy"},"Accuracy"),Object(o.b)("p",null,"The simplest approach is to take the percentage of correct predictions from the model (Ghoneim, 2019). This, however, poses problems in the case of imbalanced data."),Object(o.b)("h2",{id:"precision"},"Precision"),Object(o.b)("p",null,"Precision is the measure of correctly predicted positive cases divided by the number of total positive cases (both true positives and false positives) (Ghoneim, 2019)."),Object(o.b)("p",null,"##\xa0Recall\nThe recall metric tells us the ratio of correctly predicted observations by the total number of positive cases (Ghoneim, 2019)."),Object(o.b)("p",null,"##\xa0F-Score\nThe F1 score is the weighted average of the precision and the recall (Ghoneim, 2019). The F1-score was the main metric of evaluation for the model."))}p.isMDXComponent=!0},143:function(e,t,r){"use strict";r.d(t,"a",(function(){return u})),r.d(t,"b",(function(){return m}));var n=r(0),i=r.n(n);function o(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}function a(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,n)}return r}function c(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?a(Object(r),!0).forEach((function(t){o(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):a(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}function s(e,t){if(null==e)return{};var r,n,i=function(e,t){if(null==e)return{};var r,n,i={},o=Object.keys(e);for(n=0;n<o.length;n++)r=o[n],t.indexOf(r)>=0||(i[r]=e[r]);return i}(e,t);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);for(n=0;n<o.length;n++)r=o[n],t.indexOf(r)>=0||Object.prototype.propertyIsEnumerable.call(e,r)&&(i[r]=e[r])}return i}var l=i.a.createContext({}),p=function(e){var t=i.a.useContext(l),r=t;return e&&(r="function"==typeof e?e(t):c(c({},t),e)),r},u=function(e){var t=p(e.components);return i.a.createElement(l.Provider,{value:t},e.children)},d={inlineCode:"code",wrapper:function(e){var t=e.children;return i.a.createElement(i.a.Fragment,{},t)}},f=i.a.forwardRef((function(e,t){var r=e.components,n=e.mdxType,o=e.originalType,a=e.parentName,l=s(e,["components","mdxType","originalType","parentName"]),u=p(r),f=n,m=u["".concat(a,".").concat(f)]||u[f]||d[f]||o;return r?i.a.createElement(m,c(c({ref:t},l),{},{components:r})):i.a.createElement(m,c({ref:t},l))}));function m(e,t){var r=arguments,n=t&&t.mdxType;if("string"==typeof e||n){var o=r.length,a=new Array(o);a[0]=f;var c={};for(var s in t)hasOwnProperty.call(t,s)&&(c[s]=t[s]);c.originalType=e,c.mdxType="string"==typeof e?e:n,a[1]=c;for(var l=2;l<o;l++)a[l]=r[l];return i.a.createElement.apply(null,a)}return i.a.createElement.apply(null,r)}f.displayName="MDXCreateElement"},210:function(e,t,r){"use strict";r.r(t),t.default=r.p+"assets/images/accuracy_precision-ef200555360a9a3158afa729a8644556.png"}}]);