export function configRouter (router) {
  router.map({
    '/': {
      component: require('./components/UserCenter.vue')
    }
  })
}
