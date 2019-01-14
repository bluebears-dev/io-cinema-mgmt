import getters from '@/store/getters'

describe('getters.js', () => {
  it('getCurrentCinema should return correct value', () => {
    const state = {currentCinema: 'cinema'}
    getters.getCurrentCinema(state)

    expect(state.currentCinema).to.equal('cinema')
  })
})
