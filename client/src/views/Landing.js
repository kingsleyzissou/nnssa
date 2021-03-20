import { Layout } from '../layouts/Layout';
import { Dropzone } from '../components/Dropzone';

export function Landing({ setLanding }) {

  return (
    <Layout
      title="Title"
      subtitle="Lorem ipsum"
      text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"
      Component={() => <Dropzone setLanding={setLanding} />}
    />
  )

}