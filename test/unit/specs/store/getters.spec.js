import getters from '@/store/getters'
import state from '@/store/state'

describe('getters.js', () => {
  it('getCurrentCinema should return correct value', () => {
    const state = {currentCinema: 'cinema'}
    const result = getters.getCurrentCinema(state)

    expect(result).to.equal('cinema')
  })

  it('getMovies should return correct value', () => {
    const state = {movies: ['movie 1', 'movie 2']}
    const result = getters.getMovies(state)

    expect(result).to.be.an('array')
    expect(result).to.have.members(['movie 1', 'movie 2'])
  })

  it('getTicketTypes should return correct value', () => {
    const state = {ticketTypes: ['type 1', 'type 2', 'type 3']}
    const result = getters.getTicketTypes(state)

    expect(result).to.be.an('array')
    expect(result).to.have.members(['type 1', 'type 2', 'type 3'])
  })

  it('getCinemas should return correct value', () => {
    const state = {cinemas: ['cinema 1', 'cinema 2']}
    const result = getters.getCinemas(state)

    expect(result).to.be.an('array')
    expect(result).to.have.members(['cinema 1', 'cinema 2'])
  })

  it('getShowings should return correct value', () => {
    const state = {showings: ['showing 1', 'showing 2']}
    const result = getters.getShowings(state)

    expect(result).to.be.an('array')
    expect(result).to.have.members(['showing 1', 'showing 2'])
  })

  it('getMovieDetails should return correct value', () => {
    const state = {movieDetails: ['detail 1', 'detail 2']}
    const result = getters.getMovieDetails(state)

    expect(result).to.be.an('array')
    expect(result).to.have.members(['detail 1', 'detail 2'])
  })

  it('getCinemaDetails should return correct value', () => {
    const state = {currentCinema: 2, cinemas: [{id: 1, name: 'cinema 1'}, {id: 2, name: 'cinema 2'}]}
    const result = getters.getCinemaDetails(state)

    expect(result.name).to.be.equal('cinema 2')
    expect(result.id).to.be.equal(2)
  })

  it('getSelectedDate  should return correct value', () => {
    const result = getters.getSelectedDate(state)
    const weekDays = ['Nd', 'Pn', 'Wt', 'Śr', 'Cz', 'Pt', 'So']

    expect(result.title).to.be.oneOf(weekDays)
    expect(result.date).to.match(/\d{4}-\d{2}-\d{2}/)
  })

  it('getRoom should return correct value', () => {
    const state = {
      room: {
        cinema: 1,
        cols: 20,
        id: 2
      }
    }
    const result = getters.getRoom(state)

    expect(result).to.be.an('object')
    expect(result).to.be.equal(state.room)
  })
})
