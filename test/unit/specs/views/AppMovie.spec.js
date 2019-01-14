import { createLocalVue, mount } from '@vue/test-utils'
import AppMovie from '@/views/AppMovie'
import Vuetify from 'vuetify'
import router from '@/router'
import store from '@/store'

describe('AppMovie.vue', () => {
  const localVue = createLocalVue()
  localVue.use(router)
  localVue.use(store)
  localVue.use(Vuetify)
  const component = mount(AppMovie, {localVue, router, store})

  it('should display all days of the week', () => {
    let days = component.vm.days
    expect(days).to.be.an('array').to.satisfy(
      (arr) => arr.every(v => v.title != null)
    )
    let dayLabels = days.map(v => v.title)
    expect(dayLabels).to.have.members(['Pn', 'Wt', 'Śr', 'Cz', 'Pt', 'So', 'Nd'])
  })

  it('should set correct color for buttons', () => {
    let days = component.vm.days
    component.vm.$store.state.selectedDate = days[0]

    expect(component.vm.buttonDayColor(days[0].title)).to.be.equal('gold')
    expect(component.vm.buttonDayColor(days[1].title)).to.be.equal('white')
  })
})
