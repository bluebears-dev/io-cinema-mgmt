<template>
  <v-layout
      class="form--layout"
      justify-center row
      wrap
  >
    <v-flex class="hidden-sm-and-down" xs12>
      <v-layout justify-center>
        <v-flex class="cinema--name alegreya-sc--light margin text-xs-center" lg3 md4>
          {{cinemaDetails.name}}
        </v-flex>
        <v-flex md7/>
      </v-layout>
    </v-flex>
    <v-flex xs12>
      <v-layout justify-center>
        <v-flex class="booking--information hidden-sm-and-down" lg3 md4>
          <v-fade-transition group>
            <v-flex class="section" key="1">
              <div class="section--name alegreya-sc--light">Seans</div>
              <div class="section--information roboto--regular">
                {{movieDetails.title}} <br> {{showing.picture_type}}, {{showing.audio_type}} <br> {{convertedDate}} -
                {{showing.hour}}
                <br> Sala: {{room.name}}
              </div>
            </v-flex>
            <v-flex class="section" key="2" v-if="formStep>1">
              <div class="section--name alegreya-sc--light">Miejsca</div>
              <div class="section--information roboto--regular">
                <span>{{selectedSeats.map(v => v.row_label + v.col_label).join(', ')}}</span>
              </div>
            </v-flex>
            <v-flex class="section" key="3" v-if="formStep>2">
              <div class="section--name alegreya-sc--light">Bilety</div>
              <div :key="price"
                   class="section--information roboto--regular"
                   v-for="price in prices"
                   v-if="ticketTypesAmount[price.ticketType]>0">
                {{ticketTypesAmount[price.ticketType]}}x {{price.ticketType}}
              </div>
            </v-flex>
            <v-flex class="section last--section" key="4" v-if="formStep>3">
              <div class="section--name alegreya-sc--light">Dane Osobowe</div>
              <div class="section--information roboto--regular">
                {{customerName}} {{customerSurname}} <br> {{customerEmail}} <br> {{customerPhone}}
              </div>
            </v-flex>
          </v-fade-transition>
        </v-flex>
        <v-flex class="booking--form" md7>
          <v-stepper v-model="formStep">
            <v-stepper-header>
              <v-stepper-step :complete="formStep > 1" color="gold" step="1"></v-stepper-step>
              <v-divider></v-divider>
              <v-stepper-step :complete="formStep > 2" color="gold" step="2"></v-stepper-step>
              <v-divider></v-divider>
              <v-stepper-step :complete="formStep > 3" color="gold" step="3"></v-stepper-step>
              <v-divider></v-divider>
              <v-stepper-step :complete="formStep > 4" color="gold" step="4"></v-stepper-step>
            </v-stepper-header>

            <v-stepper-items>
              <v-stepper-content class="form--height" step="1">
                <v-layout class="layout--fill" column>
                  <div class="alegreya-sc--regular text-capitalize step--title">Wybierz Miejsca</div>
                  <v-flex>
                    <BookingFormRoomLayout
                        :roomId="showing.room"
                        v-model="selectedSeats"
                        :refresh="forceLayoutRefresh"
                    />
                  </v-flex>
                  <v-flex>
                    <v-layout
                        align-content-end
                        fill-height row
                        wrap
                    >
                      <v-btn
                          :disabled="selectedSeats.length<=0"
                          @click="goToStepTwo()"
                          class="alegreya-sc--regular text-capitalize form--button block-xs-only"
                          color=gold
                      >
                        Dalej
                      </v-btn>
                      <v-spacer class="hidden-xs-only"/>
                      <v-btn
                          class="alegreya-sc--regular text-capitalize form--button block-xs-only"
                          flat
                          :to="{name: 'MovieDetails', params: {id: movieDetails.id}}"
                      >
                        Anuluj
                      </v-btn>
                    </v-layout>
                  </v-flex>
                </v-layout>
              </v-stepper-content>
              <v-stepper-content class="form--height" step="2">
                <v-layout class="layout--fill" column>
                  <v-flex xs12>
                    <div class="alegreya-sc--regular text-capitalize step--title">Wybierz Typ Biletów</div>
                  </v-flex>
                  <v-form
                      ref="stepTwoForm"
                      v-model="stepTwoFormState"
                  >
                    <v-flex
                        :key="price.id"
                        v-for="price in prices"
                        xs12
                    >
                      <v-layout justify-center row wrap>
                        <v-flex
                            class="ticket--type"
                            md5 sm4 xs7
                        >
                          <div class="alegreya-sc--regular text-capitalize form--button">
                            {{price.ticketType}}
                          </div>
                        </v-flex>
                        <v-flex md3 sm4 xs4>
                          <v-text-field
                              :min="0"
                              :rules="[
                            v => (Number(v) >= 0 || v == null) || 'Niepoprawna wartość',
                            validateTicketsAmount
                          ]"
                              color="gold"
                              label="Ilość"
                              type="number"
                              v-model="ticketTypesAmount[price.ticketType]"
                          ></v-text-field>
                        </v-flex>
                      </v-layout>
                    </v-flex>
                  </v-form>
                  <v-flex>
                    <v-layout
                        align-content-end
                        fill-height row
                        wrap
                    >
                      <v-btn
                          :disabled="!stepTwoFormState"
                          @click="goToStepThree()"
                          class="alegreya-sc--regular text-capitalize form--button block-xs-only"
                          color=gold
                      >
                        Dalej
                      </v-btn>
                      <v-btn
                          @click="backToStepOne()"
                          class="alegreya-sc--regular text-capitalize form--button block-xs-only"
                          flat
                      >
                        Wstecz
                      </v-btn>
                      <v-spacer class="hidden-xs-only"/>
                      <v-btn
                          class="alegreya-sc--regular text-capitalize form--button block-xs-only"
                          flat
                          :to="{name: 'MovieDetails', params: {id: movieDetails.id}}"
                      >
                        Anuluj
                      </v-btn>
                    </v-layout>
                  </v-flex>
                </v-layout>
              </v-stepper-content>
              <v-stepper-content class="form--height" step="3">
                <v-layout class="layout--fill" column>
                  <v-layout
                      justify-center
                      row wrap
                  >
                    <v-flex xs12>
                      <div class="alegreya-sc--regular text-capitalize step--title">Wprowadź Dane Osobowe</div>
                    </v-flex>
                    <v-flex class="margin"
                            xs5
                    >
                      <v-text-field
                          :rules="[validateName(customerName)]"
                          color="gold"
                          label="Imię"
                          placeholder="Imię"
                          v-model="customerName"
                      ></v-text-field>
                    </v-flex>
                    <v-flex xs5>
                      <v-text-field
                          :rules="[validateName(customerSurname)]"
                          color="gold"
                          label="Nazwisko"
                          placeholder="Nazwisko"
                          v-model="customerSurname"
                      ></v-text-field>
                    </v-flex>
                    <v-flex class="margin"
                            xs5
                    >
                      <v-text-field
                          :rules="[validateEmail]"
                          color="gold"
                          label="E-mail"
                          placeholder="E-mail"
                          v-model="customerEmail"
                      ></v-text-field>
                    </v-flex>
                    <v-flex xs5>
                      <v-text-field
                          :rules="[validatePhone]"
                          color="gold"
                          label="Numer telefonu"
                          placeholder="Numer telefonu"
                          v-model="customerPhone"
                      ></v-text-field>
                    </v-flex>
                  </v-layout>
                  <v-flex>
                    <v-layout
                        align-content-end
                        fill-height row
                        wrap
                    >
                      <v-btn
                          :disabled="!validateAll"
                          @click="formStep = 4"
                          class="alegreya-sc--regular text-capitalize form--button block-xs-only"
                          color=gold
                      >
                        Dalej
                      </v-btn>
                      <v-btn
                          @click="formStep = 2"
                          class="alegreya-sc--regular text-capitalize form--button block-xs-only"
                          flat
                      >
                        Wstecz
                      </v-btn>
                      <v-spacer class="hidden-xs-only"/>
                      <v-btn
                          class="alegreya-sc--regular text-capitalize form--button block-xs-only"
                          flat
                          :to="{name: 'MovieDetails', params: {id: movieDetails.id}}"
                      >
                        Anuluj
                      </v-btn>
                    </v-layout>
                  </v-flex>
                </v-layout>
              </v-stepper-content>
              <v-stepper-content class="form--height" step="4">
                <v-layout class="layout--fill" column>
                  <v-layout
                      align-content-end
                      fill-height row
                      wrap
                  >
                    <v-btn
                        @click="formStep = 3"
                        class="alegreya-sc--regular text-capitalize form--button block-xs-only"
                        flat
                    >
                      Wstecz
                    </v-btn>
                    <v-spacer class="hidden-xs-only"/>
                    <v-btn
                        class="alegreya-sc--regular text-capitalize form--button block-xs-only"
                        flat
                        :to="{name: 'MovieDetails', params: {id: movieDetails.id}}"
                    >
                      Anuluj
                    </v-btn>
                  </v-layout>
                </v-layout>
              </v-stepper-content>
            </v-stepper-items>
          </v-stepper>
        </v-flex>
      </v-layout>
    </v-flex>
  </v-layout>
</template>

<script>
  import BookingFormRoomLayout from '../components/AppBookingForm/BookingFormRoomLayout'
  import UsesPrices from '../mixins/UsesPrices'

  export default {
    name: 'AppBookingForm',
    components: {BookingFormRoomLayout},
    mixins: [UsesPrices],
    props: {
      id: {
        required: true
      }
    },
    data () {
      return {
        selectedSeats: [],
        stepTwoFormState: false,
        formStep: 0,
        ticketTypesAmount: {},
        customerName: '',
        customerSurname: '',
        customerEmail: '',
        customerPhone: '',
        token: null,
        bookingId: null,
        forceLayoutRefresh: 0
      }
    },
    computed: {
      convertedSelectedSeats () {
        return this.selectedSeats.map(v => {
          return {
            row: v.seat[0],
            column: v.seat[1]
          }
        })
      },
      cinemaDetails () {
        return this.$store.getters['getCinemaDetails'] || {}
      },
      movieDetails () {
        return this.$store.getters['getMovieDetails'][0] || {genre: []}
      },
      showing () {
        return this.$store.getters['getShowings'].filter(v => v.id === Number(this.id))[0] || {}
      },
      room () {
        return this.$store.getters['getRoom']
      },
      convertedDate () {
        let date = ''
        if (this.showing.date) {
          date = this.showing.date.split('-').reverse().join('.')
        }
        return date
      },
      validateTicketsAmount () {
        let values = Object.values(this.ticketTypesAmount)
        let totalAmount = values.reduce((a, b) => Number(a) + Number(b), 0)
        return Number(this.selectedSeats.length) === totalAmount || 'Ilość biletów się nie zgadza się'
      },
      validateEmail () {
        let emailRegex = /\S+@\S+\.\S+/
        if (this.customerEmail == null || this.customerEmail === '' || !emailRegex.test(this.customerEmail)) {
          return 'Proszę wprowadzić poprawne dane'
        } else {
          return true
        }
      },
      validatePhone () {
        if (this.customerPhone == null || this.customerPhone === '' || this.customerPhone.match(/^[0-9]+$/) == null) {
          return 'Proszę wprowadzić poprawne dane'
        } else {
          return true
        }
      },
      validateAll () {
        return (this.validatePhone === true && this.validateEmail === true && this.validateName(this.customerName) === true && this.validateName(this.customerSurname) === true)
      }
    },
    methods: {
      validateName (name) {
        if (name === '' || name == null || /\d/.test(name)) {
          return 'Proszę wprowadzić poprawne dane'
        } else {
          return true
        }
      },
      bookTickets (bookingId, token, tickets) {
        return this.$store.dispatch('bookTickets', {
          bookingId,
          token,
          tickets
        })
      },
      goToStepTwo () {
        let promise = null
        if (!this.bookingId) {
          promise = this.$store.dispatch('createBooking', this.id)
            .then(response => {
              this.token = response.data.token
              this.bookingId = response.data.id
              return this.bookTickets(this.bookingId, this.token, this.convertedSelectedSeats)
            })
        } else {
          promise = this.bookTickets(this.bookingId, this.token, this.convertedSelectedSeats)
        }
        promise.then(() => {
          this.formStep = 2
        })
      },
      backToStepOne () {
        this.$store.dispatch('requestOccupiedSeats', this.id)
          .then(() => {
            let selected = this.selectedSeats.map(v => JSON.stringify(v.seat))
            let occupied = this.room.occupied.filter(v => selected.indexOf(JSON.stringify(v)) === -1)
            this.$store.commit('SET_OCCUPIED_SEATS', occupied)
            this.forceLayoutRefresh++
            this.formStep = 1
          })
      },
      goToStepThree () {
        if (this.$refs['stepTwoForm'].validate()) {
          let tickets = this.convertedSelectedSeats
          let types = Object.entries(this.ticketTypesAmount)
          let currentType = types.pop()
          for (let ticket of tickets) {
            ticket.ticket_type = this.prices.find(v => v.ticketType === currentType[0]).id
            currentType[1] = Number(currentType[1]) - 1
            if (!currentType[1]) {
              currentType = types.pop()
            }
          }
          this.bookTickets(this.bookingId, this.token, tickets).then(() => {
            this.formStep = 3
          })
        }
      }
    },
    created () {
      this.$store.dispatch('requestShowingDetails', this.id)
        .then(() => {
          this.$store.dispatch('requestCinemas')
          this.$store.dispatch('requestRoom', this.showing.room)
          this.$store.dispatch('requestOccupiedSeats', this.id)
          this.$store.dispatch('requestMovieDetails', this.showing.movie)
        })
        .catch(() => {
          this.$router.replace({name: 'NotFound'})
        })
    },
    beforeRouteUpdate (to, from, next) {
      this.$store.dispatch('requestShowingDetails', to.params.id)
        .then(() => {
          let showing = this.$store.getters['getShowings'].filter(v => v.id === Number(to.params.id))[0]
          this.$store.dispatch('requestCinemas')
          this.$store.dispatch('requestRoom', showing.room)
          this.$store.dispatch('requestOccupiedSeats', to.params.id)
          this.$store.dispatch('requestMovieDetails', showing.movie)
          next()
        })
        .catch(() => {
          this.$router.replace({name: 'NotFound'})
        })
    }
  }
</script>

<style scoped lang="stylus">
  @import "~vuetify/src/stylus/settings/_variables.styl"

  @media screen and (max-width: $grid-breakpoints.sm)
    .block-xs-only
      width: 100%
      display: block

  .booking--information
    border: 1px solid var(--v-gold-base)
    margin-right: 20px

  .section--name
    color: var(--v-gold-base)
    font-size: 1.5rem

  .section--information
    color: var(--v-white-base)
    font-size: 1.2rem
    padding-left: 25px
    letter-spacing: 2px

  .section
    padding-top: 20px
    padding-left: 30px

  .last--section
    padding-bottom: 20px

  .form--height
    min-height: 530px

  .form--layout
    padding-top: 100px

  .cinema--name
    color: var(--v-gold-base)
    font-size: 2rem

  .ticket--type
    display: flex
    justify-content: center
    flex-direction: column

  .margin
    margin-right: 20px

  .form--button
    letter-spacing: 2px
    font-size: 1.3rem

  .step--title
    letter-spacing: 2px
    font-size: 1.3rem
    margin-left: 20px
    margin-top: 15px
    margin-bottom: 5px

  .layout--fill
    min-height: inherit
</style>
