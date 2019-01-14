import mutations from '@/store/mutations'

describe('mutations.js', () => {
  it('SET_CURRENT_CINEMA should work correctly', () => {
    const state = {currentCinema: null}
    const cinema = 'cinema'
    mutations.SET_CURRENT_CINEMA(state, cinema)

    expect(state.currentCinema).to.equal(cinema)
  })
})
