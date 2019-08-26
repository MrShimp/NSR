<template>
  <a
    v-bind:href="href"
    v-bind:class="{ active: isActive , inactive : !isActive}"
    v-on:click="go"
  >
    <slot></slot>
  </a>
</template>

<script>
import routes from '@/router/index'
export default {
  props: {
    href: {
      type: String,
      required: true
    }
  },
  computed: {
    isActive () {
      return this.href === this.$root.currentRoute
    }
  },
  methods: {
    go (event) {
      event.preventDefault()
      this.$root.currentRoute = this.href
      this.$router.push(this.href)
      window.history.pushState(
        null,
        routes[this.href],
        this.href
      )
    }
  }
}
</script>

<style scoped>

  .inactive{
    text-decoration: none;
    font-family: 'Oswald', 'Helvetica Neue', Arial, Helvetica, sans-serif;
    font-size: 25px;
    color : #1C3854;
  }
  .active {
    text-decoration: none;
    font-family: 'Oswald', 'Helvetica Neue', Arial, Helvetica, sans-serif;
    font-size: 25px;
    color : #F68331;
  }
</style>
