<template>
  <div class="width--static">
    <v-flex
        class="row wrap justify-center"
        mb-3
        mt-4
        xs12
    >
      <v-flex
          class="screen text-xs-center alegreya-sc--regular spacing"
          lg10
          md12
          sm10
          xs12
      >
        Ekran
      </v-flex>
    </v-flex>
    <v-flex
        :key="Math.random() + row"
        v-for="row in room.layout"
        xs12
    >
      <div class="row" v-if="row != null">
        <div class="column label text-xs-center alegreya-sc--bold">{{row.row}}</div>
        <div
            :class="isSelected(seat) ? 'selected' : 'free'"
            :key="Math.random() + seat"
            @click="toggleSeat(seat)"
            class="column seat text-xs-center roboto--regular"
            v-for="seat in row.seats"
            v-if="seat"
        >
          {{seat.col}}
        </div>
        <div
            class="column"
            v-else
        ></div>
      </div>
      <div class="row" v-else></div>
    </v-flex>
  </div>
</template>

<script>
  export default {
    name: 'BookingFormRoomLayout',
    props: {
      showingId: {
        type: Number,
        required: true
      },
      selectedSeats: {
        type: Array,
        required: true
      }
    },
    model: {
      prop: 'selectedSeats'
    },
    computed: {
      room () {
        return this.$store.getters['getRoom']
      }
    },
    methods: {
      toggleSeat (seat) {
        let index = this.selectedSeats.indexOf(seat)
        if (index === -1) {
          this.selectedSeats.push(seat)
        } else {
          this.selectedSeats.splice(index, 1)
        }
      },
      isSelected (seat) {
        return this.selectedSeats.indexOf(seat) !== -1
      }
    },
    created () {
      this.$store.dispatch('requestRoom', this.showingId)
    }
  }
</script>

<style scoped lang="stylus">
  .row
    display: flex
    height: 20px
    justify-content: center
    align-items: center
    margin: 1px 0

  .occupied
    background: aqua

  .selected
    border: 1px solid var(--v-gold-base)
    background: var(--v-gold-base)
    color: black !important
    cursor: pointer

  .free
    border: 1px solid black
    background: transparent
    cursor: pointer

  .column
    box-sizing: border-box
    display: inline-block
    height: 15px
    width: 15px
    margin: 2px
    line-height: 14px
    font-size: 0.7rem

    &.seat
      color: transparent

    &.seat:hover
      color: black
      @extends .selected

  .label
    font-size: 0.9rem
    padding-right: 20px

  .screen
    background: #e0e0e0
    line-height: 25px
    height: 25px

  .width--static
    min-width: 810px
    overflow-x: auto

  .spacing
    letter-spacing: 2px
</style>
