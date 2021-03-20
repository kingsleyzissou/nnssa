const times = [5.454512, 52.31636445, 85.42290845, 124.03679645,
  162.67052595, 170.94487929, 173.70702329, 206.78101529]

export const markers = times.map((time, index) => {
  const position = (index % 2 === 0) ? 'top' : 'bottom'
  return {
    time,
    color: '#2bffc6',
    // label: 'Chorus',
    position
  }
})