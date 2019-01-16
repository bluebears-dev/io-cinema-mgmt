import cookie from '../utils/cookie'

const weekDays = ['Nd', 'Pn', 'Wt', 'Śr', 'Cz', 'Pt', 'So']

const state = {
  currentCinema: Number(cookie.get('cinema').value),
  cinemas: [],
  movies: [],
  showings: [],
  ticketTypes: [],
  movieDetails: [],
  selectedDate: {title: weekDays[(new Date()).getDay() % 7], date: (new Date()).toISOString().split('T')[0]},
  room: {},
  payuOAuthClientId: '348348',
  payuOAuthClientSecret: '0a494446d180e225470a14fd4285d9e5'
}

export default state
