<template>
  <div>
    <v-layout
      justify-center
      row wrap
    >
      <v-flex
        xs11 md9
        class="section__bar"
      >
        <v-flex xs12 sm12 md5 lg4>
          <v-select
            class="select--cinema"
            solo
            light
            flat
            hide-details
            dense
            color="gold"
            label="Kino"
            background-color="black"
            :items="cinemas()"
            item-text="name"
            item-value="id"
            :menu-props="{'content-class': 'select__menu--black elevation-0'}"
            v-model="currentCinema"
            @change="setCinemaCookie()"
          ></v-select>
        </v-flex>
      </v-flex>
      <v-flex xs10 md8>
        <v-layout
          row wrap
          class="white--text pa-4"
        >
          <v-flex pt-2>
            <v-layout
              row wrap
            >
              <v-flex
                xs12 sm4 offset-sm1
                class=" alegreya-sc--regular cinema--details"
              >
                <span>Adres:</span>
              </v-flex>

              <v-flex
                xs12 sm6
                class="alegreya-sc--light cinema--details"
              >
                <span>{{cinemaDetails.address}}, {{cinemaDetails.postal_code}} {{cinemaDetails.city}}</span><br>
              </v-flex>
              <v-flex
                xs12 sm4 offset-sm1
                class="alegreya-sc--regular cinema--details"
              >
                <span>Numer telefonu:</span>
              </v-flex>

              <v-flex
                xs12 sm6
                class="alegreya-sc--light cinema--details"
              >
                <span>{{cinemaDetails.phone_number}}</span><br>
              </v-flex>
            </v-layout>
          </v-flex>
        </v-layout>
      </v-flex>
    </v-layout>

  </div>
</template>

<script>
  import ChangesCinema from '../mixins/ChangesCinema'

  export default {
    name: 'AppCinema',
    mixins: [ChangesCinema],
    computed: {
      cinemaDetails () {
        return this.$store.getters['getCinemaDetails']
      }
    }
  }
</script>

<style scoped lang="stylus">
  .section__bar
    padding-top: 100px
    border-bottom: 1.5px solid var(--v-gold-base)

  .cinema--details
    font-size: 1.6rem
    line-height: 38px
    letter-spacing: 4px
</style>
