<template>
  <div>
    <div class="screen text-xs-center alegreya-sc--regular spacing mt-2 mx-auto">
      Ekran
    </div>
    <div class="overflow pt-2">
      <div :class="hasLayoutLoaded ? '' : 'hidden'" class="wrapper--layout">
        <div
            :key="Math.random() + row"
            class="row--wrapper"
            v-for="row in room.layout"
        >
          <div class="row" v-if="row != null">
            <div
                class="column label text-xs-center alegreya-sc--bold"
            >
              {{row.row}}
            </div>
            <div
                :class="(isSelected(row.seats[i]) ? 'selected' : 'free')"
                :key="Math.random() + row.seats[i]"
                @click="toggleSeat({row_label: row.row, col_label: row.seats[i].col, seat: row.seats[i].seat})"
                class="column seat text-xs-center roboto--regular"
                v-for="i in room.cols"
                v-if="row.seats[i]"
            >
              {{row.seats[i].col}}
            </div>
            <div
                class="column"
                v-else
            ></div>
          </div>
          <div class="row" v-else></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'BookingFormRoomLayout',
    props: {
      roomId: {
        type: Number,
        required: true
      },
      selectedSeats: {
        type: Array
      }
    },
    model: {
      prop: 'selectedSeats'
    },
    data () {
      return {
        hasLayoutLoaded: true
      }
    },
    computed: {
      room () {
        return this.$store.getters['getRoom']
      }
    },
    methods: {
      toggleSeat (seat) {
        let index = this.selectedSeats.findIndex(v => v.seat === seat.seat)
        if (index === -1) {
          this.selectedSeats.push(seat)
        } else {
          this.selectedSeats.splice(index, 1)
        }
      },
      isSelected (seat) {
        return this.selectedSeats.filter(v => v.seat === seat.seat).length === 1
      }
    }
  }
</script>

<style scoped lang="stylus">
  $seat-size = 20px
  $row-spacing = 3px
  $seat-spacing = 2px

  .row
    display: inline-flex
    white-space: nowrap
    height: $seat-size
    margin: $row-spacing 0

  .row--wrapper
    display: flex
    flex-direction: row
    flex-wrap: wrap
    justify-content: center

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
    margin: $seat-spacing
    height: $seat-size
    width: $seat-size
    line-height: $seat-size * 0.8
    font-size: 0.8rem

    &.seat
      color: transparent

    &.seat:hover
      color: black
      @extends .selected

  .label
    font-size: 0.9rem

  .screen
    background: #e0e0e0
    line-height: 25px
    height: 25px
    width: 90%

  .spacing
    letter-spacing: 2px

  .wrapper--layout
    display: inline-grid
    width: 100%

  .overflow
    height: 400px
    overflow: auto

  .hidden
    opacity: 0
</style>
