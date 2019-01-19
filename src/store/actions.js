import axios from 'axios'

const actions = {
  setCurrentCinema ({commit, dispatch}, cinema) {
    commit('SET_CURRENT_CINEMA', cinema)
    dispatch('requestMovies', cinema)
  },
  requestCinemas ({state, commit}) {
    if (state.cinemas.length === 0) {
      return axios.get('cinemas/')
        .then((response) => {
          commit('SET_CINEMAS', response.data)
        })
    }
  },
  requestMovies ({state, commit}) {
    return axios.get(state.currentCinema + '/' + state.selectedDate.date + '/movies')
      .then((response) => {
        commit('SET_MOVIES', response.data)
      })
  },
  requestTicketTypes ({state, commit}) {
    if (state.ticketTypes.length === 0) {
      return axios.get('prices/')
        .then((response) => {
          commit('SET_TICKET_TYPES', response.data)
        })
    }
  },
  requestMovieDetails ({state, commit}, id) {
    return axios.get('movies/' + id)
      .then(response => {
        commit('SET_MOVIE_DETAILS', response.data)
      })
  },
  requestShowings ({state, commit}, id) {
    return axios.get(state.currentCinema + '/' + id + '/' + state.selectedDate.date + '/showings')
      .then(response => {
        commit('SET_SHOWINGS', response.data)
      })
  },
  requestShowingDetails ({state, commit}, id) {
    return axios.get(`showings/${id}`)
      .then(response => {
        commit('ADD_SHOWING', response.data)
      })
  },
  requestRoom ({state, commit}, showingId) {
    return axios.get(`rooms/${showingId}`)
      .then(response => {
        commit('SET_ROOM', response.data)
      })
  },
  requestOccupiedSeats ({state, commit}, showingId) {
    return axios.get(`showings/${showingId}/occupied/seats`)
      .then(response => {
        commit('SET_OCCUPIED_SEATS', response.data.map(v => v.seat))
      })
  },
  createBooking ({state, commit}, showingId) {
    return axios.post(`showings/${showingId}/book/`)
  },
  cancelBooking ({state, commit}, {bookingId, token}) {
    return axios.delete(
      `bookings/${bookingId}`,
      {
        params: {
          token: token
        }
      }
    )
  },
  bookTickets ({state, commit}, {bookingId, token, tickets}) {
    return axios.put(`bookings/${bookingId}/tickets`, {
      token: token,
      tickets: tickets
    })
  },
  updateClientData ({state, commit}, data) {
    return axios.put(`bookings/${data.bookingId}/client`, {
      token: data.token,
      client_data: {
        first_name: data.firstName,
        last_name: data.lastName,
        email: data.email,
        phone_number: data.phoneNumber
      }
    })
  },
  bookingTimeoutWebhook ({state, commit}, {bookingId, token}) {
    return axios.post(`webhook/bookings/${bookingId}/timeout/`, {
      token: token
    })
  },
  requestOAuthToken ({state, commit}) {
    return axios.post(
      'payment/oauth',
      {
        client_id: state.payuOAuthClientId,
        client_secret: state.payuOAuthClientSecret
      }
    ).then(response => response.data.access_token)
  },
  requestPayMethods ({state, commit}, oauth) {
    return axios.get(
      'payment/paymethods',
      {
        headers: {
          'X-AUTHORIZATION': `Bearer ${oauth}`
        }
      }
    )
  },
  finalizeBooking ({state, commit}, {bookingId, token}) {
    return axios.post(`bookings/${bookingId}/finish`, {
      token: token
    })
  },
  createOrder ({state, commit}, {bookingId, token, method, oauth}) {
    return axios.post(
      `payment/order/${bookingId}`,
      {
        token,
        method
      },
      {
        headers: {
          'X-AUTHORIZATION': `Bearer ${oauth}`
        }
      }
    )
  },
  getTransaction ({state, commit}, {bookingId, token, oauth}) {
    return axios.get(
      `payment/order/${bookingId}/${token}`,
      {
        headers: {
          'X-AUTHORIZATION': `Bearer ${oauth}`
        }
      }
    )
  }
}

export default actions
