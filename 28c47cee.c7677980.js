(window.webpackJsonp=window.webpackJsonp||[]).push([[21],{143:function(e,t,n){"use strict";n.d(t,"a",(function(){return p})),n.d(t,"b",(function(){return b}));var r=n(0),o=n.n(r);function a(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function i(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);t&&(r=r.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,r)}return n}function s(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?i(Object(n),!0).forEach((function(t){a(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):i(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function l(e,t){if(null==e)return{};var n,r,o=function(e,t){if(null==e)return{};var n,r,o={},a=Object.keys(e);for(r=0;r<a.length;r++)n=a[r],t.indexOf(n)>=0||(o[n]=e[n]);return o}(e,t);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);for(r=0;r<a.length;r++)n=a[r],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(o[n]=e[n])}return o}var u=o.a.createContext({}),c=function(e){var t=o.a.useContext(u),n=t;return e&&(n="function"==typeof e?e(t):s(s({},t),e)),n},p=function(e){var t=c(e.components);return o.a.createElement(u.Provider,{value:t},e.children)},f={inlineCode:"code",wrapper:function(e){var t=e.children;return o.a.createElement(o.a.Fragment,{},t)}},d=o.a.forwardRef((function(e,t){var n=e.components,r=e.mdxType,a=e.originalType,i=e.parentName,u=l(e,["components","mdxType","originalType","parentName"]),p=c(n),d=r,b=p["".concat(i,".").concat(d)]||p[d]||f[d]||a;return n?o.a.createElement(b,s(s({ref:t},u),{},{components:n})):o.a.createElement(b,s({ref:t},u))}));function b(e,t){var n=arguments,r=t&&t.mdxType;if("string"==typeof e||r){var a=n.length,i=new Array(a);i[0]=d;var s={};for(var l in t)hasOwnProperty.call(t,l)&&(s[l]=t[l]);s.originalType=e,s.mdxType="string"==typeof e?e:r,i[1]=s;for(var u=2;u<a;u++)i[u]=n[u];return o.a.createElement.apply(null,i)}return o.a.createElement.apply(null,n)}d.displayName="MDXCreateElement"},156:function(e,t,n){"use strict";n.r(t),t.default=n.p+"assets/images/cnn-fa9280bfeb6b3dd90d1b572815c56d50.png"},89:function(e,t,n){"use strict";n.r(t),n.d(t,"frontMatter",(function(){return i})),n.d(t,"metadata",(function(){return s})),n.d(t,"toc",(function(){return l})),n.d(t,"default",(function(){return c}));var r=n(3),o=n(7),a=(n(0),n(143)),i={id:"cnn",title:"Convolutional Neural Networks",sidebar_label:"Convolutional Neural Networks",slug:"/convolutional-neural-networks"},s={unversionedId:"cnn",id:"version-status-report/cnn",isDocsHomePage:!1,title:"Convolutional Neural Networks",description:"The use of a convolutional layer to obtain a feature map of input data (Valueva and Chervyakov, 2020)",source:"@site/versioned_docs/version-status-report/cnn.md",slug:"/convolutional-neural-networks",permalink:"/docs/status-report/convolutional-neural-networks",editUrl:"https://github.com/kingsleyzissou/nnssa/edit/master/website/versioned_docs/version-status-report/cnn.md",version:"status-report",sidebar_label:"Convolutional Neural Networks",sidebar:"version-status-report/someSidebar",previous:{title:"Neural Networks & Deep Learning",permalink:"/docs/status-report/neural-networks"},next:{title:"Compression Analysis",permalink:"/docs/status-report/compression-analysis"}},l=[],u={toc:l};function c(e){var t=e.components,i=Object(o.a)(e,["components"]);return Object(a.b)("wrapper",Object(r.a)({},u,i,{components:t,mdxType:"MDXLayout"}),Object(a.b)("p",null,Object(a.b)("img",{src:n(156).default})),Object(a.b)("p",null,Object(a.b)("em",{parentName:"p"},"The use of a convolutional layer to obtain a feature map of input data (Valueva and Chervyakov, 2020)")),Object(a.b)("p",null,"Convolutional neural networks are neural networks that make use of convolutional layers. Convolu- tional layers apply a filter to the input in order to obtain a feature map of the data. The convolutional layer can be considered as the layer that is responsible for the extraction of the features from the input data (Valueva and Chervyakov, 2020). In addition to the convolution layer, a convolutional network consists of a max pooling layer which is responsible for downsampling the feature maps and summarising the features (Brownlee, 2019)."))}c.isMDXComponent=!0}}]);