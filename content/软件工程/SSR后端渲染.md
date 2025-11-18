---
title: SSR 后端渲染
---

## 关键词

- 服务端渲染 SSR，全称 `Server Side Render`
- 客户端渲染 CSR，全称 `Client Side Render`，预渲染
- 单页面应用程序 SPA,全称 `Single Page Application`：使用单个 HTML 完成多个页面切换的应用

  - 只需加载一次 html，js，css 资源
  - 路由定义页面跳转，通过 js 监控 url 的变化，判断页面到底是显示哪个组件，清除不需要的，显示需要的组件
- 多页应用又称 MPA（Multi Page Application）指有多个独立的页面的应用，每个页面必须重复加载 js,css 等相关资源。多页应用跳转，需要整页资源刷新。

  - 路由由后端实现
- 营销页面的 SEO:<strong>SEO（英文 Search Engine Optimization）字面理解很简单的，就是[搜索引擎优化]</strong>

## 单页面 VS 多页面

<table>
<tr>
<td><strong>维度</strong><br/></td><td><strong>单页应用</strong><br/></td><td><strong>多页应用</strong><br/></td></tr>
<tr>
<td>结构<br/></td><td>一个主页面 + 许多模块的组件<br/></td><td>许多完整的页面<br/></td></tr>
<tr>
<td>过渡动画<br/></td><td>Vue 提供了 transition 的封装组件，容易实现<br/></td><td>很难实现<br/></td></tr>
<tr>
<td>内容更新<br/></td><td>通过相关组件的切换实现（局部更新），具备更好的体验度和流畅度<br/></td><td>整体 HTML 的切换，消耗更多网络资源，且流畅度较差<br/></td></tr>
<tr>
<td>路由模式<br/></td><td>可以使用 hash ，也可以使用 history<br/></td><td>普通链接跳转<br/></td></tr>
<tr>
<td>数据传递<br/></td><td>因为单页面，可以直接使用全局变量（Vuex）<br/><br/></td><td>需要使用cookie 、localStorage 等缓存方案、URL 参数，调用接口保存等<br/></td></tr>
<tr>
<td>相关成本<br/></td><td>前期开发成本较高，后期维护较为容易<br/></td><td>前期开发成本低，后期维护就比较麻烦，因为可能一个功能需要改很多地方<br/></td></tr>
<tr>
<td>html文件请求<br/></td><td>第一次进入页面的时候会请求一个html文件，刷新清除一下。切换到其他组件，此时路径也相应变化，但是并没有新的html文件请求，页面内容也变化了<br/></td><td>每一次页面跳转的时候，后台服务器都会给返回一个新的html文档<br/></td></tr>
<tr>
<td><em>适用场景(SEO)</em><br/><br/></td><td>因页面是通过js动态生成的，不利于SEO<br/></td><td>主要是静态页面，利于SEO<br/><br/></td></tr>
<tr>
<td><em>首屏时间</em><br/></td><td>首屏时间慢，首屏时需要请求一次html，同时还要发送一次js请求，两次请求回来了，首屏才会展示出来<br/></td><td>首屏时间快，访问页面的时候，服务器返回一个 html，页面就会展示出来，这个过程只经历了一个HTTP请求<br/></td></tr>
</table>

## 应用场景

- 多页面应用：flower 应用，django admin 应用
