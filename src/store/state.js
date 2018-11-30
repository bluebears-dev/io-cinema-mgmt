import cookie from '../utils/cookie'

const state = {
  currentCinema: cookie.get('cinema').value,
  cinemas: ['Kraków', 'Rzeszów', 'Warszawa'],
  movies: []
}

export default state
