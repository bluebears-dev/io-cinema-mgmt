import mutations from '@/store/mutations'

describe('mutations.js', () => {
  it('SET_CURRENT_CINEMA should work correctly', () => {
    const state = {currentCinema: null}
    const cinema = 'cinema'
    mutations.SET_CURRENT_CINEMA(state, cinema)

    expect(state.currentCinema).to.equal(cinema)
  })

  it('SET_CINEMAS should work correctly', () => {
    const state = { cinemas: [] }
    const cinemas = [{ name: 'cinema 1', id: 1 }, { name: 'cinema 2', id: 2 }]
    mutations.SET_CINEMAS(state, cinemas)

    expect(state.cinemas).have.deep.members([{ name: 'cinema 1', id: 1 }, { name: 'cinema 2', id: 2 }])
  })

  it('SET_MOVIES should work correctly', () => {
    const state = { movies: [] }
    const movies = [{ title: 'movie 1', id: 1 }, { title: 'movie 2', id: 2 }]
    mutations.SET_MOVIES(state, movies)

    expect(state.movies).have.deep.members([{ title: 'movie 1', id: 1 }, { title: 'movie 2', id: 2 }])
  })

  it('SET_TICKET_TYPES should work correctly', () => {
    const state = { ticketTypes: [] }
    const ticketTypes = [{ title: 'type 1', price: 12.00 }, { title: 'type 2', price: 15.00 }]
    mutations.SET_TICKET_TYPES(state, ticketTypes)

    expect(state.ticketTypes).have.deep.members([{ title: 'type 2', price: 15.00 }, { title: 'type 1', price: 12.00 }])
  })

  it('SET_SHOWINGS should work correctly', () => {
    const state = { showings: [] }
    const showings = [{ movie: 3, date: '2020-11-11' }, { movie: 8, date: '2019-03-23' }]
    mutations.SET_SHOWINGS(state, showings)

    expect(state.showings).have.deep.members([{ movie: 8, date: '2019-03-23' }, { movie: 3, date: '2020-11-11' }])
  })

  it('SET_MOVIE_DETAILS should work correctly', () => {
    const state = { movieDetails: [] }
    const movieDetails = [{ detail1: 'a', detail2: 'b' }]
    mutations.SET_MOVIE_DETAILS(state, movieDetails)

    expect(state.movieDetails).have.deep.members([{ detail1: 'a', detail2: 'b' }])
  })

  it('SET_SELECTED_DATE should work correctly', () => {
    const state = { selectedDate: {} }
    const selectedDate = { title: 'Pn', date: '2018-09-08' }
    mutations.SET_SELECTED_DATE(state, selectedDate)

    expect(state.selectedDate.title).to.be.equal('Pn')
    expect(state.selectedDate.date).to.be.equal('2018-09-08')
  })
})
