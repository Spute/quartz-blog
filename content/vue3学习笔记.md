---
title:
publish: flase
category: 文章写作
date: 2025-12-14
alias: " lzm2yepqsqjj5pmk78cg"
tags:
---
# Vue 3 全局构建（CDN）写法简洁笔记

> 适用于 **不使用打包工具（Vite / Webpack）**，直接通过 `<script>` 引入 Vue 的场景

---

## 一、引入方式

```html
<script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
```

引入后，浏览器中会自动挂载一个全局对象：

```js
window.Vue
```

---

## 二、常见解构写法（推荐）

```js
const { createApp, ref, reactive, computed, watch } = Vue;
```

等价于：

```js
const createApp = Vue.createApp;
const ref = Vue.ref;
```

作用：

- 写法更简洁
    
- 更接近模块化（ESM）使用体验
    

---

## 三、创建应用实例

```js
const app = createApp({
  data() {
    return {
      count: 0
    }
  }
});
```

说明：

- `createApp` 用于创建一个 Vue 应用实例
    
- 传入的是 **根组件配置对象**
    

---

## 四、挂载应用

```js
app.mount('#app');
```

HTML 中需要有对应节点：

```html
<div id="app"></div>
```

---

## 五、Composition API 用法示例

```html
<div id="app">{{ count }}</div>

<script>
const { createApp, ref } = Vue;

createApp({
  setup() {
    const count = ref(0);
    return { count };
  }
}).mount('#app');
</script>
```

---

## 六、methods / computed / watch

```js
createApp({
  data() {
    return { num: 1 };
  },
  methods: {
    inc() {
      this.num++;
    }
  },
  computed: {
    double() {
      return this.num * 2;
    }
  }
}).mount('#app');
```

---

## 七、全局注册组件

```js
const app = createApp({});

app.component('MyButton', {
  template: `<button>按钮</button>`
});

app.mount('#app');
```

    

---

## 十、不适合的场景

- 大型项目
    
- 多页面复杂依赖
    
- 需要 Tree Shaking / TypeScript
    

> 以上场景建议使用 **Vite + ESM 构建模式**