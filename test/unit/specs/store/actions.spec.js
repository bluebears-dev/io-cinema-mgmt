import actions from '@/store/actions'

describe('actions.js', () => {
  it('requestCinemas should return promise when empty', () => {
    let state = {
      cinemas: []
    }
    let result = actions.requestCinemas({state})
    expect(result).to.be.a('promise')

    state = {
      cinemas: [1]
    }
    result = actions.requestCinemas({state})
    expect(result).to.not.be.a('promise')
  })

  it('requestMovies should return promise', () => {
    const state = {
      selectedDate: {}
    }
    let result = actions.requestMovies({state})
    expect(result).to.be.a('promise')
  })

  it('requestTicketTypes should return promise when empty', () => {
    let state = {
      ticketTypes: []
    }
    let result = actions.requestTicketTypes({state})
    expect(result).to.be.a('promise')

    state = {
      ticketTypes: [1]
    }
    result = actions.requestTicketTypes({state})
    expect(result).to.not.be.a('promise')
  })

  it('requestMovieDetails should return promise', () => {
    const state = {}
    let result = actions.requestMovieDetails({state}, 1)
    expect(result).to.be.a('promise')
  })

  it('requestShowingDetails should return promise', () => {
    const state = {}
    let result = actions.requestShowingDetails({state}, 1)
    expect(result).to.be.a('promise')
  })

  it('requestRoom should return promise', () => {
    const state = {}
    let result = actions.requestRoom({state}, 1)
    expect(result).to.be.a('promise')
  })

  it('requestOccupiedSeats should return promise', () => {
    const state = {}
    let result = actions.requestOccupiedSeats({state}, 1)
    expect(result).to.be.a('promise')
  })

  it('createBooking should return promise', () => {
    const state = {}
    let result = actions.createBooking({state}, 1)
    expect(result).to.be.a('promise')
  })

  it('cancelBooking should return promise', () => {
    const state = {}
    let result = actions.cancelBooking({state}, 1)
    expect(result).to.be.a('promise')
  })

  it('bookTickets should return promise', () => {
    const state = {}
    let result = actions.bookTickets({state}, 1)
    expect(result).to.be.a('promise')
  })

  it('updateClientData should return promise', () => {
    const state = {}
    let result = actions.updateClientData({state}, 1)
    expect(result).to.be.a('promise')
  })

  it('bookingTimeoutWebhook should return promise', () => {
    const state = {}
    let result = actions.bookingTimeoutWebhook({state}, 1)
    expect(result).to.be.a('promise')
  })

  it('requestOAuthToken should return promise', () => {
    const state = {}
    let result = actions.requestOAuthToken({state})
    expect(result).to.be.a('promise')
  })

  it('requestPayMethods should return promise', () => {
    const state = {}
    let result = actions.requestPayMethods({state}, 1)
    expect(result).to.be.a('promise')
  })

  it('finalizeBooking should return promise', () => {
    const state = {}
    let result = actions.finalizeBooking({state}, 1)
    expect(result).to.be.a('promise')
  })

  it('createOrder should return promise', () => {
    const state = {}
    let result = actions.createOrder({state}, 1)
    expect(result).to.be.a('promise')
  })

  it('getTransaction should return promise', () => {
    const state = {}
    let result = actions.getTransaction({state}, 1)
    expect(result).to.be.a('promise')
  })
})
