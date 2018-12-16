export default {
  methods: {
    cinemas () {
      return this.$store.getters['getCinemas']
    },
    setCinemaCookie () {
      this.$cookie.set('cinema', this.currentCinema)
    }
  },
  computed: {
    currentCinema: {
      get () {
        return this.$store.getters['getCurrentCinema']
      },
      set (newValue) {
        this.$store.dispatch('setCurrentCinema', newValue)
      }
    }
  },
  created () {
    this.$store.dispatch('requestCinemas')
      .then(() => {
        if (this.cinemas().map(v => v.id).indexOf(this.currentCinema) === -1) {
          this.$cookie.remove('cinema')
          this.$router.replace({name: 'CinemaSelection'})
        }
      })
  }
}
