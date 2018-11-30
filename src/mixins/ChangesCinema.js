export default {
  methods: {
    cinemas () {
      return this.$store.getters['getCinemas']
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
  }
}
