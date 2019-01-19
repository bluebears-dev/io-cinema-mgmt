import mutations from '@/store/mutations'

describe('mutations.js', () => {
  it('SET_CURRENT_CINEMA should work correctly', () => {
    const state = {currentCinema: null}
    const cinema = 'cinema'
    mutations.SET_CURRENT_CINEMA(state, cinema)

    expect(state.currentCinema).to.equal(cinema)
  })

  it('SET_CINEMAS should work correctly', () => {
    const state = {cinemas: []}
    const cinemas = [{name: 'cinema 1', id: 1}, {name: 'cinema 2', id: 2}]
    mutations.SET_CINEMAS(state, cinemas)

    expect(state.cinemas).have.deep.members([{name: 'cinema 1', id: 1}, {name: 'cinema 2', id: 2}])
  })

  it('SET_MOVIES should work correctly', () => {
    const state = {movies: []}
    const movies = [{title: 'movie 1', id: 1}, {title: 'movie 2', id: 2}]
    mutations.SET_MOVIES(state, movies)

    expect(state.movies).have.deep.members([{title: 'movie 1', id: 1}, {title: 'movie 2', id: 2}])
  })

  it('SET_TICKET_TYPES should work correctly', () => {
    const state = {ticketTypes: []}
    const ticketTypes = [{title: 'type 1', price: 12.00}, {title: 'type 2', price: 15.00}]
    mutations.SET_TICKET_TYPES(state, ticketTypes)

    expect(state.ticketTypes).have.deep.members([{title: 'type 2', price: 15.00}, {title: 'type 1', price: 12.00}])
  })

  it('SET_SHOWINGS should work correctly', () => {
    const state = {showings: []}
    const showings = [{movie: 3, date: '2020-11-11'}, {movie: 8, date: '2019-03-23'}]
    mutations.SET_SHOWINGS(state, showings)

    expect(state.showings).have.deep.members([{movie: 8, date: '2019-03-23'}, {movie: 3, date: '2020-11-11'}])
  })

  it('SET_MOVIE_DETAILS should work correctly', () => {
    const state = {movieDetails: []}
    const movieDetails = [{detail1: 'a', detail2: 'b'}]
    mutations.SET_MOVIE_DETAILS(state, movieDetails)

    expect(state.movieDetails).have.deep.members([{detail1: 'a', detail2: 'b'}])
  })

  it('SET_SELECTED_DATE should work correctly', () => {
    const state = {selectedDate: {}}
    const selectedDate = {title: 'Pn', date: '2018-09-08'}
    mutations.SET_SELECTED_DATE(state, selectedDate)

    expect(state.selectedDate.title).to.be.equal('Pn')
    expect(state.selectedDate.date).to.be.equal('2018-09-08')
  })

  it('SET_ROOM should work correctly and do not overwrite occupied seats', () => {
    const state = {
      room: {
        occupied: 'yeah'
      }
    }
    mutations.SET_ROOM(state, {id: 1})

    expect(state.room.id).to.be.equal(1)
    expect(state.room.occupied).to.be.equal('yeah')
  })

  it('ADD_SHOWING should work correctly and do not add duplicates', () => {
    const state = {
      showings: [
        {id: 1}
      ]
    }
    mutations.ADD_SHOWING(state, {id: 1})
    mutations.ADD_SHOWING(state, {id: 2})

    expect(state.showings).to.have.lengthOf(2)
    expect(state.showings).to.be.an('array').that.deep.includes.members([{id: 1}, {id: 2}])
  })

  it('SET_OCCUPIED_SEATS should work correctly', () => {
    const state = {
      room: {
        id: 1
      }
    }
    mutations.SET_OCCUPIED_SEATS(state, 'occupied')

    expect(state.room.id).to.be.equal(1)
    expect(state.room.occupied).to.be.equal('occupied')
  })
})
