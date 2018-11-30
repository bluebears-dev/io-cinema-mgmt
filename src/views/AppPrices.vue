<template>
  <v-layout
    justify-center
    row wrap
  >
    <v-flex
      xs11 md9
      class="text-xs-center gold--text section__title alegreya-sc--regular"
    >
      Cennik
    </v-flex>
    <v-flex
      xs10 md8
      class="section"
    >
      <v-layout
        row wrap
        class="white--text pa-4"
        v-for="price in prices"
      >
        <v-flex pt-2>
          <v-layout>
            <v-flex
              xs9
              class="alegreya-sc--regular price"
            >
              {{price.title}}
            </v-flex>
            <v-flex
              xs5
              class="alegreya-sc--regular price"
            >
              {{price.amount}}
            </v-flex>
          </v-layout>
        </v-flex>
        <v-flex
          xs12 md7
          pt-2
          class="alegreya-sc--light price"
        >
          {{price.description}}
        </v-flex>
      </v-layout>
    </v-flex>
  </v-layout>
</template>

<script>
  export default {
    name: 'AppPrices',
    data () {
      return {
        prices: [
          {
            title: 'Normalny',
            amount: '15zł',
            description: 'Regularny bilecik dla wszystkich w przystępnej cenie.'
          },
          {
            title: 'Ulgowy',
            amount: '10zł',
            description: 'Bilecik zniżkowy, dostępny dla osób z upoważniającym dokumentem.'
          }
        ]
      }
    }
  }
</script>

<style scoped lang="stylus">
  .section__title
    font-size: 2rem
    padding-top: 100px
    border-bottom: 1.5px solid var(--v-gold-base)

  .price
    font-size: 1.6rem
</style>
