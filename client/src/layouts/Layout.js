import { Title, SubTitle, Text } from '../components/Styled';

/**
 * Re-usable Layout component
 * 
 */
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