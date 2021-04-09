import { Title, SubTitle, Text } from '../components/Styled';

export function Layout({ title, subtitle, text, Component }) {
  return (
    <>
      <SubTitle>{subtitle}</SubTitle>
      <Title>{title}</Title>
      <Text>{text}</Text>
      <Component />
    </>
  )
}