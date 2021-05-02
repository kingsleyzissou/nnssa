(window.webpackJsonp=window.webpackJsonp||[]).push([[50],{119:function(e,t,n){"use strict";n.r(t),n.d(t,"frontMatter",(function(){return a})),n.d(t,"metadata",(function(){return c})),n.d(t,"toc",(function(){return s})),n.d(t,"default",(function(){return u}));var r=n(3),o=n(7),i=(n(0),n(143)),a={id:"introduction",title:"Introduction",sidebar_label:"Introduction",slug:"/"},c={unversionedId:"introduction",id:"introduction",isDocsHomePage:!1,title:"Introduction",description:"Boundary Detection",source:"@site/docs/introduction.md",slug:"/",permalink:"/docs/next/",editUrl:"https://github.com/kingsleyzissou/nnssa/edit/master/website/docs/introduction.md",version:"current",sidebar_label:"Introduction",sidebar:"someSidebar",next:{title:"Abstract",permalink:"/docs/next/abstract"}},s=[{value:"Boundary Detection",id:"boundary-detection",children:[]},{value:"Background",id:"background",children:[]},{value:"Scope",id:"scope",children:[]},{value:"Problem Description",id:"problem-description",children:[]}],d={toc:s};function u(e){var t=e.components,n=Object(o.a)(e,["components"]);return Object(i.b)("wrapper",Object(r.a)({},d,n,{components:t,mdxType:"MDXLayout"}),Object(i.b)("h2",{id:"boundary-detection"},"Boundary Detection"),Object(i.b)("p",null,"Boundary Detection is a subset of music information retrieval aimed at analysing and detecting the transition points, or boundaries, between song sections. These boundaries are commonly referred to as cue points in the world of DJing. The area of interest would be to train a model to detect the different semantic segments within a song, i.e. differentiating between the intro and verse or the verse and the chorus."),Object(i.b)("h2",{id:"background"},"Background"),Object(i.b)("p",null,"The initial project proposal involved integrating aspects of music and artificial intelligence. During the Media Tools & Integration module, with Colm Dunphy, from the first semester of our fourth year, we made use of the Pioneer RekordBox DJ software. The software had a free trial of a premium feature that highlighted the song sections of a song and where the changes occurred. The feature did not work particularly well and sparked an interest in seeing if this feature could be replicated using artificial intelligence."),Object(i.b)("h2",{id:"scope"},"Scope"),Object(i.b)("p",null,"The initial project scope was beyond what could be done by a single student as a fourth-year project. An effort was made, from the very first meeting with my project supervisor, to narrow down the scope of the project to something more feasible. Once an idea had been identified, the approach to reduce and narrow down the problem area was aggressive, to find a simple, yet effective way for training a neural network model on audio data, without requiring vast resources. Through extensive research, an image-based representation of audio was identified as the key finding to simplifying the problem and training the model."),Object(i.b)("h2",{id:"problem-description"},"Problem Description"),Object(i.b)("p",null,"To find the boundaries in songs, in preparation for DJ sets, it is necessary to listen to the entire song from start to finish and count out the beats and set these points manually. The process is very manual and very time consuming, especially when having to prepare a large number of songs for a DJ performance. This project aims to assist the process of identifying these boundaries, with the aid of artificial intelligence, to speed up the preparation time for DJs."))}u.isMDXComponent=!0},143:function(e,t,n){"use strict";n.d(t,"a",(function(){return l})),n.d(t,"b",(function(){return b}));var r=n(0),o=n.n(r);function i(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function a(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);t&&(r=r.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,r)}return n}function c(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?a(Object(n),!0).forEach((function(t){i(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):a(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function s(e,t){if(null==e)return{};var n,r,o=function(e,t){if(null==e)return{};var n,r,o={},i=Object.keys(e);for(r=0;r<i.length;r++)n=i[r],t.indexOf(n)>=0||(o[n]=e[n]);return o}(e,t);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);for(r=0;r<i.length;r++)n=i[r],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(o[n]=e[n])}return o}var d=o.a.createContext({}),u=function(e){var t=o.a.useContext(d),n=t;return e&&(n="function"==typeof e?e(t):c(c({},t),e)),n},l=function(e){var t=u(e.components);return o.a.createElement(d.Provider,{value:t},e.children)},p={inlineCode:"code",wrapper:function(e){var t=e.children;return o.a.createElement(o.a.Fragment,{},t)}},f=o.a.forwardRef((function(e,t){var n=e.components,r=e.mdxType,i=e.originalType,a=e.parentName,d=s(e,["components","mdxType","originalType","parentName"]),l=u(n),f=r,b=l["".concat(a,".").concat(f)]||l[f]||p[f]||i;return n?o.a.createElement(b,c(c({ref:t},d),{},{components:n})):o.a.createElement(b,c({ref:t},d))}));function b(e,t){var n=arguments,r=t&&t.mdxType;if("string"==typeof e||r){var i=n.length,a=new Array(i);a[0]=f;var c={};for(var s in t)hasOwnProperty.call(t,s)&&(c[s]=t[s]);c.originalType=e,c.mdxType="string"==typeof e?e:r,a[1]=c;for(var d=2;d<i;d++)a[d]=n[d];return o.a.createElement.apply(null,a)}return o.a.createElement.apply(null,n)}f.displayName="MDXCreateElement"}}]);