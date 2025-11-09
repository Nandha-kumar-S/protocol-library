import { useEffect } from 'react'
import { useNavigate } from 'react-router-dom'

/**
 * Custom hook for keyboard shortcuts
 */
export const useKeyboardShortcuts = () => {
  const navigate = useNavigate()

  useEffect(() => {
    const handleKeyDown = (event) => {
      // Only handle shortcuts when not typing in input fields
      if (event.target.tagName === 'INPUT' || 
          event.target.tagName === 'TEXTAREA' || 
          event.target.contentEditable === 'true') {
        return
      }

      // Check for Ctrl/Cmd key combinations
      const isCtrlOrCmd = event.ctrlKey || event.metaKey

      if (isCtrlOrCmd) {
        switch (event.key) {
          case 'h':
            event.preventDefault()
            navigate('/')
            break
          case 'p':
            event.preventDefault()
            navigate('/protocols')
            break
          case 's':
            event.preventDefault()
            navigate('/studies')
            break
          case 'j':
            event.preventDefault()
            navigate('/jobs')
            break
          case 'k':
            event.preventDefault()
            showShortcutsModal()
            break
          default:
            break
        }
      }

      // Handle single key shortcuts
      switch (event.key) {
        case 'Escape':
          // Close any open modals or clear selections
          const modals = document.querySelectorAll('[role="dialog"]')
          if (modals.length > 0) {
            const closeButton = modals[modals.length - 1].querySelector('[data-close]')
            if (closeButton) closeButton.click()
          }
          break
        case '?':
          if (!isCtrlOrCmd) {
            event.preventDefault()
            showShortcutsModal()
          }
          break
        default:
          break
      }
    }

    document.addEventListener('keydown', handleKeyDown)
    return () => document.removeEventListener('keydown', handleKeyDown)
  }, [navigate])

  const showShortcutsModal = () => {
    // Create and show shortcuts modal
    const modal = document.createElement('div')
    modal.style.cssText = `
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: rgba(0, 0, 0, 0.5);
      display: flex;
      align-items: center;
      justify-content: center;
      z-index: 10000;
    `
    
    modal.innerHTML = `
      <div style="
        background: white;
        border-radius: 12px;
        padding: 30px;
        max-width: 500px;
        width: 90%;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
      ">
        <h2 style="margin: 0 0 20px 0; color: #2c3e50;">Keyboard Shortcuts</h2>
        <div style="display: grid; gap: 12px; font-size: 0.9rem;">
          <div style="display: flex; justify-content: space-between;">
            <span><kbd style="background: #f8f9fa; padding: 2px 6px; border-radius: 3px; font-family: monospace;">Ctrl/Cmd + H</kbd></span>
            <span>Go to Dashboard</span>
          </div>
          <div style="display: flex; justify-content: space-between;">
            <span><kbd style="background: #f8f9fa; padding: 2px 6px; border-radius: 3px; font-family: monospace;">Ctrl/Cmd + P</kbd></span>
            <span>Go to Protocols</span>
          </div>
          <div style="display: flex; justify-content: space-between;">
            <span><kbd style="background: #f8f9fa; padding: 2px 6px; border-radius: 3px; font-family: monospace;">Ctrl/Cmd + S</kbd></span>
            <span>Go to Studies</span>
          </div>
          <div style="display: flex; justify-content: space-between;">
            <span><kbd style="background: #f8f9fa; padding: 2px 6px; border-radius: 3px; font-family: monospace;">Ctrl/Cmd + J</kbd></span>
            <span>Go to Jobs</span>
          </div>
          <div style="display: flex; justify-content: space-between;">
            <span><kbd style="background: #f8f9fa; padding: 2px 6px; border-radius: 3px; font-family: monospace;">Escape</kbd></span>
            <span>Close Modal</span>
          </div>
          <div style="display: flex; justify-content: space-between;">
            <span><kbd style="background: #f8f9fa; padding: 2px 6px; border-radius: 3px; font-family: monospace;">?</kbd></span>
            <span>Show Shortcuts</span>
          </div>
        </div>
        <button data-close style="
          margin-top: 20px;
          padding: 10px 20px;
          background: #007bff;
          color: white;
          border: none;
          border-radius: 6px;
          cursor: pointer;
          float: right;
        ">Close</button>
      </div>
    `
    
    const closeModal = () => {
      document.body.removeChild(modal)
    }
    
    modal.addEventListener('click', (e) => {
      if (e.target === modal || e.target.hasAttribute('data-close')) {
        closeModal()
      }
    })
    
    document.body.appendChild(modal)
  }
}

export default useKeyboardShortcuts
