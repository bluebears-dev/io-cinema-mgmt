<template>
  <v-layout
      class="form--layout"
      justify-center row
      wrap
  >
    <v-flex class="cinema--name alegreya-sc--light" xs10>
      {{cinemaDetails.name}}
    </v-flex>
    <v-flex class="booking--information" md3>
      <v-flex class="section">
        <div class="section--name alegreya-sc--light">Seans</div>
        <div class="section--information roboto--regular">
          {{showing.name}} <br> {{showing.pictureType}}, {{showing.audioType}} <br> {{showing.date}} - {{showing.start}}
          <br> Sala: {{showing.room}}
        </div>
      </v-flex>
      <v-flex class="section" v-if="formStep>1">
        <div class="section--name alegreya-sc--light">Miejsca</div>
        <div class="section--information roboto--regular">{{ticketAmount}}</div>
      </v-flex>
      <v-flex class="section" v-if="formStep>2">
        <div class="section--name alegreya-sc--light">Bilety</div>
        <div :key="price"
             class="section--information roboto--regular"
             v-for="price in prices"
             v-if="ticketTypesAmount[price.id-1]>0">
          {{ticketTypesAmount[price.id-1]}}x {{price.ticketType}}
        </div>
      </v-flex>
      <v-flex class="section last--section" v-if="formStep>3">
        <div class="section--name alegreya-sc--light">Dane Osobowe</div>
        <div class="section--information roboto--regular">
          {{customerName}} {{customerSurname}} <br> {{customerEmail}} <br> {{customerPhone}}
        </div>
      </v-flex>
    </v-flex>
    <v-flex class="booking--form" md5>
      <v-stepper class="form--height" v-model="formStep">
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
            <v-flex xs12>
              <div class="alegreya-sc--regular text-capitalize step--title">Wybierz Miejsca</div>
            </v-flex>
            <v-text-field
                color="gold"
                label="Ilość biletów"
                min="0"
                type="number"
                v-model="ticketAmount"
            ></v-text-field>
            <v-btn
                :disabled="ticketAmount<=0"
                @click="formStep = 2"
                class="alegreya-sc--regular text-capitalize form--button"
                color=gold
            >
              Dalej
            </v-btn>
            <v-btn
                class="alegreya-sc--regular text-capitalize form--button"
                flat
            >
              Anuluj
            </v-btn>
          </v-stepper-content>
          <v-stepper-content class="form--height" step="2">
            <v-flex xs12>
              <div class="alegreya-sc--regular text-capitalize step--title">Wybierz Typ Biletów</div>
            </v-flex>
            <v-flex
                :key="price.id"
                v-for="(price, i) in prices"
            >
              <v-layout
                  justify-center
              >
                <v-flex
                    class="ticket--type" md4 sm4
                    xs7
                >
                  <div class="alegreya-sc--regular text-capitalize form--button">{{price.ticketType}}</div>
                </v-flex>
                <v-flex md2 sm3 xs3>
                  <v-text-field
                      color="gold"
                      label="ilość"
                      min="0"
                      type="number"
                      v-model="ticketTypesAmount[i]"
                  ></v-text-field>
                </v-flex>
              </v-layout>
            </v-flex>
            <v-btn
                :disabled="!validateTicketsAmount"
                @click="formStep = 3"
                class="alegreya-sc--regular text-capitalize form--button"
                color=gold

            >
              Dalej
            </v-btn>
            <v-btn
                @click="formStep = 1"
                class="alegreya-sc--regular text-capitalize form--button"
                flat
            >
              Wstecz
            </v-btn>
            <v-btn
                class="alegreya-sc--regular text-capitalize form--button"
                flat
            >
              Anuluj
            </v-btn>
          </v-stepper-content>
          <v-stepper-content class="form--height" step="3">
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
            <v-btn
                :disabled="!validateAll"
                @click="formStep = 4"
                class="alegreya-sc--regular text-capitalize form--button"
                color=gold
            >
              Dalej
            </v-btn>
            <v-btn
                @click="formStep = 2"
                class="alegreya-sc--regular text-capitalize form--button"
                flat
            >
              Wstecz
            </v-btn>
            <v-btn
                class="alegreya-sc--regular text-capitalize form--button"
                flat
            >
              Anuluj
            </v-btn>
          </v-stepper-content>
          <v-stepper-content class="form--height" step="4">

            <v-btn
                @click="formStep = 3"
                class="alegreya-sc--regular text-capitalize form--button"
                flat
            >
              Wstecz
            </v-btn>
            <v-btn
                class="alegreya-sc--regular text-capitalize form--button"
                flat
            >
              Anuluj
            </v-btn>
          </v-stepper-content>
        </v-stepper-items>
      </v-stepper>
    </v-flex>
  </v-layout>
</template>

<script>
  export default {
    name: 'AppBookingForm',
    data () {
      return {
        formStep: 0,
        ticketAmount: 0,
        ticketTypesAmount: [],
        showing: {
          name: 'Bohemian Rhapsody',
          room: 'A',
          audioType: 'Napisy',
          pictureType: '2D',
          date: '09.11.2018',
          start: '18:00'
        },
        customerName: '',
        customerSurname: '',
        customerEmail: '',
        customerPhone: ''
      }
    },

    created () {
      this.$store.dispatch('requestTicketTypes')
    },
    computed: {
      prices () {
        return this.$store.getters['getTicketTypes']
      },
      cinemaDetails () {
        return this.$store.getters['getCinemaDetails']
      },
      validateTicketsAmount () {
        let totalAmount = this.ticketTypesAmount.reduce((a, b) => Number(a) + Number(b), 0)
        return Number(this.ticketAmount) === totalAmount
      },
      validateEmail () {
        if (this.customerEmail == null || this.customerEmail === '') {
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
      }
    }
  }
</script>

<style scoped lang="stylus">
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
    min-height: 450px

  .form--layout
    padding-top: 110px

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
</style>
