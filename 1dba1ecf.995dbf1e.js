(window.webpackJsonp=window.webpackJsonp||[]).push([[19],{143:function(e,t,r){"use strict";r.d(t,"a",(function(){return p})),r.d(t,"b",(function(){return b}));var n=r(0),i=r.n(n);function c(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}function a(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,n)}return r}function o(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?a(Object(r),!0).forEach((function(t){c(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):a(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}function s(e,t){if(null==e)return{};var r,n,i=function(e,t){if(null==e)return{};var r,n,i={},c=Object.keys(e);for(n=0;n<c.length;n++)r=c[n],t.indexOf(r)>=0||(i[r]=e[r]);return i}(e,t);if(Object.getOwnPropertySymbols){var c=Object.getOwnPropertySymbols(e);for(n=0;n<c.length;n++)r=c[n],t.indexOf(r)>=0||Object.prototype.propertyIsEnumerable.call(e,r)&&(i[r]=e[r])}return i}var l=i.a.createContext({}),u=function(e){var t=i.a.useContext(l),r=t;return e&&(r="function"==typeof e?e(t):o(o({},t),e)),r},p=function(e){var t=u(e.components);return i.a.createElement(l.Provider,{value:t},e.children)},d={inlineCode:"code",wrapper:function(e){var t=e.children;return i.a.createElement(i.a.Fragment,{},t)}},m=i.a.forwardRef((function(e,t){var r=e.components,n=e.mdxType,c=e.originalType,a=e.parentName,l=s(e,["components","mdxType","originalType","parentName"]),p=u(r),m=n,b=p["".concat(a,".").concat(m)]||p[m]||d[m]||c;return r?i.a.createElement(b,o(o({ref:t},l),{},{components:r})):i.a.createElement(b,o({ref:t},l))}));function b(e,t){var r=arguments,n=t&&t.mdxType;if("string"==typeof e||n){var c=r.length,a=new Array(c);a[0]=m;var o={};for(var s in t)hasOwnProperty.call(t,s)&&(o[s]=t[s]);o.originalType=e,o.mdxType="string"==typeof e?e:n,a[1]=o;for(var l=2;l<c;l++)a[l]=r[l];return i.a.createElement.apply(null,a)}return i.a.createElement.apply(null,r)}m.displayName="MDXCreateElement"},201:function(e,t,r){"use strict";r.r(t),t.default=r.p+"assets/images/accuracy_precision-ef200555360a9a3158afa729a8644556.png"},87:function(e,t,r){"use strict";r.r(t),r.d(t,"frontMatter",(function(){return a})),r.d(t,"metadata",(function(){return o})),r.d(t,"toc",(function(){return s})),r.d(t,"default",(function(){return u}));var n=r(3),i=r(7),c=(r(0),r(143)),a={id:"metrics",title:"Metrics",sidebar_label:"Metrics",slug:"/metrics"},o={unversionedId:"metrics",id:"metrics",isDocsHomePage:!1,title:"Metrics",description:"The image above highlights the difference between accuracy and precision (Miessler, 2019)",source:"@site/docs/metrics.md",slug:"/metrics",permalink:"/docs/next/metrics",editUrl:"https://github.com/kingsleyzissou/nnssa/edit/master/website/docs/metrics.md",version:"current",sidebar_label:"Metrics",sidebar:"someSidebar",previous:{title:"Digital Signal Processing 201",permalink:"/docs/next/dsp_201"},next:{title:"Imbalanced Data",permalink:"/docs/next/imbalance"}},s=[{value:"Accuracy",id:"accuracy",children:[]},{value:"Precision",id:"precision",children:[]}],l={toc:s};function u(e){var t=e.components,a=Object(i.a)(e,["components"]);return Object(c.b)("wrapper",Object(n.a)({},l,a,{components:t,mdxType:"MDXLayout"}),Object(c.b)("p",null,Object(c.b)("img",{src:r(201).default})),Object(c.b)("p",null,Object(c.b)("em",{parentName:"p"},"The image above highlights the difference between accuracy and precision (Miessler, 2019)")),Object(c.b)("p",null,"Metrics are an important key in understanding the performance of a model. It is necessary to cover this to gain an understanding of the metrics used to measure a neural network model and understand the literature review in the following section."),Object(c.b)("h2",{id:"accuracy"},"Accuracy"),Object(c.b)("p",null,"The simplest approach is to take the percentage of correct predictions from the model (Ghoneim, 2019). This, however, poses problems in the case of imbalanced data."),Object(c.b)("h2",{id:"precision"},"Precision"),Object(c.b)("p",null,"Precision is the measure of correctly predicted positive cases divided by the number of total positive cases (both true positives and false positives) (Ghoneim, 2019)."),Object(c.b)("p",null,"##\xa0Recall\nThe recall metric tells us the ratio of correctly predicted observations by the total number of positive cases (Ghoneim, 2019)."),Object(c.b)("p",null,"##\xa0F-Score\nThe F1 score is the weighted average of the precision and the recall (Ghoneim, 2019). The F1-score was the main metric of evaluation for the model."))}u.isMDXComponent=!0}}]);