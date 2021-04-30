(window.webpackJsonp=window.webpackJsonp||[]).push([[30],{112:function(e,t,n){"use strict";n.d(t,"a",(function(){return p})),n.d(t,"b",(function(){return f}));var r=n(0),i=n.n(r);function o(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function a(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);t&&(r=r.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,r)}return n}function s(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?a(Object(n),!0).forEach((function(t){o(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):a(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function c(e,t){if(null==e)return{};var n,r,i=function(e,t){if(null==e)return{};var n,r,i={},o=Object.keys(e);for(r=0;r<o.length;r++)n=o[r],t.indexOf(n)>=0||(i[n]=e[n]);return i}(e,t);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);for(r=0;r<o.length;r++)n=o[r],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(i[n]=e[n])}return i}var l=i.a.createContext({}),u=function(e){var t=i.a.useContext(l),n=t;return e&&(n="function"==typeof e?e(t):s(s({},t),e)),n},p=function(e){var t=u(e.components);return i.a.createElement(l.Provider,{value:t},e.children)},m={inlineCode:"code",wrapper:function(e){var t=e.children;return i.a.createElement(i.a.Fragment,{},t)}},d=i.a.forwardRef((function(e,t){var n=e.components,r=e.mdxType,o=e.originalType,a=e.parentName,l=c(e,["components","mdxType","originalType","parentName"]),p=u(n),d=r,f=p["".concat(a,".").concat(d)]||p[d]||m[d]||o;return n?i.a.createElement(f,s(s({ref:t},l),{},{components:n})):i.a.createElement(f,s({ref:t},l))}));function f(e,t){var n=arguments,r=t&&t.mdxType;if("string"==typeof e||r){var o=n.length,a=new Array(o);a[0]=d;var s={};for(var c in t)hasOwnProperty.call(t,c)&&(s[c]=t[c]);s.originalType=e,s.mdxType="string"==typeof e?e:r,a[1]=s;for(var l=2;l<o;l++)a[l]=n[l];return i.a.createElement.apply(null,a)}return i.a.createElement.apply(null,n)}d.displayName="MDXCreateElement"},98:function(e,t,n){"use strict";n.r(t),n.d(t,"frontMatter",(function(){return a})),n.d(t,"metadata",(function(){return s})),n.d(t,"toc",(function(){return c})),n.d(t,"default",(function(){return u}));var r=n(3),i=n(7),o=(n(0),n(112)),a={id:"compression-analysis",title:"Compression Analysis",sidebar_label:"Compression Analysis",slug:"/compression-analysis"},s={unversionedId:"compression-analysis",id:"compression-analysis",isDocsHomePage:!1,title:"Compression Analysis",description:"Waveform comparison",source:"@site/docs/compression.md",slug:"/compression-analysis",permalink:"/docs/compression-analysis",editUrl:"https://github.com/kingsleyzissou/nnssa/edit/master/website/docs/compression.md",version:"current",sidebar_label:"Compression Analysis",sidebar:"someSidebar",previous:{title:"Convolutional Neural Networks",permalink:"/docs/convolutional-neural-networks"},next:{title:"References",permalink:"/docs/references"}},c=[],l={toc:c};function u(e){var t=e.components,n=Object(i.a)(e,["components"]);return Object(o.b)("wrapper",Object(r.a)({},l,n,{components:t,mdxType:"MDXLayout"}),Object(o.b)("p",null,Object(o.b)("img",Object(r.a)({parentName:"p"},{src:"https://github.com/kingsleyzissou/nnssa/raw/main/img/wav_comparison.png",alt:"Waveform comparison",title:"Waveform comparison"}))),Object(o.b)("p",null,"YouTube compresses the audio for videos quite heavily using Lossy Compression. This essentially means that the compression is applied in a destructive manner and can\u2019t be reversed. It is unclear what effect this might have on the training of the neural network. To investigate this, I took a high quality audio file, uploaded it to YouTube and then downloaded the compressed audio file. I then did a side-by-side comparison of the YouTube file with the original using 2 mel-spectrograms. I then leveraged phase cancellation to try to get a more quantifiable measure of the difference in the audio. I inverted the phase of the compressed file and lined it up with the audio from the original quality audio. The phase cancellation results in an audio file that reveals the differences in the two audio files. This process is the backbone of active noise-cancellation used in noise-cancelling headphones for example (Triggs, 2020)."),Object(o.b)("p",null,Object(o.b)("img",Object(r.a)({parentName:"p"},{src:"https://github.com/kingsleyzissou/nnssa/raw/main/img/mel_comparison.png",alt:"Mel Spectrogram comparison",title:"Mel Spectrogram Comparison"}))),Object(o.b)("p",null,"Both images in this section show that the difference between the original audio and the compressed audio is small enough that I would be satisfied working with the YouTube quality audio. Additionally, in a survey published in the New Review in Hypermedia Multimedia journal in 2014, it was found that compressed audio was sufficient for music information retrieval, with the added benefit of reducing costs (Zampoglou and Malamos, 2014)."))}u.isMDXComponent=!0}}]);