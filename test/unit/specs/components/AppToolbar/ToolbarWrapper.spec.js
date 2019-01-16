import { createLocalVue, mount } from '@vue/test-utils'
import ToolbarWrapper from '@/components/AppToolbar/ToolbarWrapper'
import Vuetify from 'vuetify'
import router from '@/router'

describe('ToolbarWrapper.vue', () => {
  const localVue = createLocalVue()
  localVue.use(router)
  localVue.use(Vuetify)
  const component = mount(ToolbarWrapper, {localVue, router})

  it('should have title element', () => {
    expect(component.contains('.v-toolbar__title')).to.equal(true)
  })

  const title = component.find('.v-toolbar__title')
  it('should have correct title', () => {
    expect(title.text()).to.equal(component.vm.$data.title)
  })
})
