import cookie from '../utils/cookie'

const state = {
  currentCinema: Number(cookie.get('cinema').value),
  cinemas: [],
  movies: [],
  showings: [],
  ticketTypes: [],
  movieDetails: [],
  selectedDate: (new Date()).toISOString().split('T')[0]
}

export default state
