import { Title, SubTitle, Text } from '../components/Styled';

const style = {
  'height': '100vh',
  'width': '100vw',
  'display': 'flex',
  'justifyContent': 'center',
  'alignItems': 'center'
};

export function Layout({ title, subtitle, text, Component }) {
  return (
    <div style={style}>
      <div style={{ display: 'block', width: '50%' }}>
        <SubTitle>{subtitle}</SubTitle>
        <Title>{title}</Title>
        <Text>{text}</Text>
        <Component />
      </div>
    </div>
  )
}