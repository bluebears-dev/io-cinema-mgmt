import { createLocalVue, mount } from '@vue/test-utils'
import ToolbarWrapper from '@/components/ToolbarWrapper'
import Vuetify from 'vuetify'
import router from '@/router'

describe('ToolbarWrapper.vue', () => {
  const localVue = createLocalVue()
  localVue.use(router)
  localVue.use(Vuetify)
  const component = mount(ToolbarWrapper, {localVue, router})

  it('should have correct title', () => {
    expect(component.contains('.toolbar__desktop-layout')).to.equal(true)
  })

  it('should have mobile layout', () => {
    expect(component.contains('.toolbar__mobile-layout')).to.equal(true)
  })
})
