import cookie from '../utils/cookie'

const state = {
  currentCinema: Number(cookie.get('cinema').value),
  cinemas: [],
  movies: [],
  ticketTypes: []
}

export default state
