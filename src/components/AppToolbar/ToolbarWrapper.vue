<template>
  <v-toolbar
    flat
    app
    :height="toolbarHeight"
    class="border--gold toolbar--background"
  >
    <v-toolbar-title class="alegreya-sc--regular white--text display-1">{{ title.toUpperCase() }}</v-toolbar-title>
    <slot/>
  </v-toolbar>
</template>

<script>
  export default {
    name: 'ToolbarWrapper',
    computed: {
      toolbarHeight () {
        let breakpoint = this.$vuetify.breakpoint.name
        if (breakpoint === 'xs' || breakpoint === 'sm') {
          return 55
        } else {
          return 76
        }
      }
    },
    data () {
      return {
        title: 'KAPPA'
      }
    }
  }
</script>

<style scoped lang="stylus">
  .border--gold
    border-bottom: 2px solid var(--v-gold-base)

  .toolbar
    &--background
      background-color: var(--v-black-base) !important
</style>
