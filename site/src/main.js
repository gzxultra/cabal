import Vue from 'vue'
import VueRouter from 'vue-router'
import { configRouter } from './routes'
import vendor from './vendor/vendor'

/* eslint-disable no-new */
vendor()

Vue.use(VueRouter)
const router = new VueRouter()
const app = Vue.extend({})
configRouter(router)
router.start(app, '#app')
