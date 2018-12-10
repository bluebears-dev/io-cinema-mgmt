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
        let cinema = this.$store.getters['getCurrentCinema']
        if (this.cinemas().map(v => v.id).indexOf(cinema) !== -1) {
          return this.$store.getters['getCurrentCinema']
        } else {
          this.$cookie.remove('cinema')
          return -1
        }
      },
      set (newValue) {
        this.$store.dispatch('setCurrentCinema', newValue)
      }
    }
  },
  created () {
    this.$store.dispatch('requestCinemas')
  }
}
