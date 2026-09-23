import { fireEvent, render, screen, waitFor } from '@testing-library/react'
import { vi } from 'vitest'
import SlotPicker from '../pages/SlotPicker.jsx'

test('เลือกแพ็กเกจแล้วโหลดช่วงเวลาว่างใหม่ตามแพ็กเกจ', async () => {
  const client = {
    getSlots: vi.fn()
      .mockResolvedValueOnce([
        { id: 1, slot_date: '2026-09-23', start_time: '09:00', remaining: 2, package_code: 'STD' },
      ])
      .mockResolvedValueOnce([
        { id: 2, slot_date: '2026-09-23', start_time: '10:00', remaining: 1, package_code: 'PREMIUM' },
      ]),
  }

  render(<SlotPicker client={client} initialPackageCode="STD" />)

  expect(screen.getByText('เลือกแพ็กเกจ')).toBeTruthy()

  await waitFor(() => {
    expect(client.getSlots).toHaveBeenCalledWith({
      dateFrom: expect.any(String),
      packageCode: 'STD',
    })
  })

  fireEvent.click(screen.getByRole('button', { name: /แพ็กเกจพรีเมียม/i }))

  await waitFor(() => {
    expect(client.getSlots).toHaveBeenLastCalledWith({
      dateFrom: expect.any(String),
      packageCode: 'PREMIUM',
    })
  })

  expect(screen.getByText(/10:00/i)).toBeTruthy()
  expect(screen.getByText(/มีที่นั่งคงเหลือ: 1/i)).toBeTruthy()
})
