<template>
  <div>
    <v-toolbar
      flat
      app
      height="76"
      class="toolbar border--gold toolbar--background"
      v-if="toggleOnBreakpoint"
    >
      <v-toolbar-title class="algreya--regular white--text display-1">{{ title.toUpperCase() }}</v-toolbar-title>
      <v-layout
        fill-height
        align-end
        justify-end
      >
        <v-btn
          v-for="button in buttons"
          flat
          large
          class="mx-3 button--main algreya--light"
          color="gold"
          :to="button.path"
          active-class="v-btn--active button--active"
        >
          <span class="button__text">{{ button.title }}</span>
        </v-btn>
      </v-layout>
    </v-toolbar>
    <v-toolbar
      flat
      app
      height="55"
      class="border--gold toolbar--background"
      v-else
    >
      <v-toolbar-title class="algreya--regular white--text display-1">{{ title.toUpperCase() }}</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-side-icon
        class="gold--text"
        @click="dropdownMenu = !dropdownMenu"
      ></v-toolbar-side-icon>
    </v-toolbar>
    <v-slide-y-transition>
      <menu v-if="dropdownMenu && !toggleOnBreakpoint" class="menu--mobile border--gold">
        <v-layout column>
          <v-flex v-for="button in buttons">
            <v-btn
              block
              flat
              large
              class="ma-0 button--main algreya--light"
              color="gold"
              :to="button.path"
              @click="dropdownMenu = !dropdownMenu"
              active-class="v-btn--active button--active"
            >
              <span class="button__text">{{ button.title }}</span>
            </v-btn>
          </v-flex>
        </v-layout>
      </menu>
    </v-slide-y-transition>
  </div>
</template>

<script>
  export default {
    name: 'AppToolbar',
    computed: {
      toggleOnBreakpoint () {
        let breakpoint = this.$vuetify.breakpoint.name
        return !(breakpoint === 'xs' || breakpoint === 'sm')
      }
    },
    data () {
      return {
        dropdownMenu: false,
        title: 'KAPPA',
        buttons: [
          {title: 'Repertuar', path: '/'},
          {title: 'Cennik', path: 'a'},
          {title: 'Kontakt', path: 'b'}
        ]
      }
    }
  }
</script>

<style scoped lang="stylus">
  .button--main
    font-size: 1.4rem
    text-align: center
    text-transform: capitalize
    border-radius: 0 0 0 0

  .border--gold
    border-bottom: 2px solid var(--v-gold-base)

  .toolbar
    &--background
      background-color: var(--v-black-base) !important

    .button--main
      border: 2px solid var(--v-gold-base)
      margin: 0
      width: 175px
      border-bottom-width: 0

      &:active
        @extends .toolbar .button--main

  .button__text
    color: var(--v-white-base)

  .menu--mobile
    position: relative
    top: 55px

  .button--active
    background: var(--v-gold-base) !important

    .button__text
      color: var(--v-black-base)
</style>
