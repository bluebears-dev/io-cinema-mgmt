export default {
  computed: {
    prices () {
      return this.$store.getters['getTicketTypes']
    }
  },
  created () {
    this.$store.dispatch('requestTicketTypes')
  }
}
