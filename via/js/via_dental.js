// Dental annotation configuration
VIA_DENTAL = {
    tools: ['select', 'polygon', 'point', 'rect'],
    
    attributes: {
        tooth: {
            type: 'dropdown',
            options: Array.from({length: 32}, (_,i) => String(i+11)), // FDI numbering
            default: '11'
        },
        condition: {
            type: 'dropdown',
            options: ['Healthy', 'Caries', 'Filling', 'Crown', 'Root Canal', 'Implant', 'Missing'],
            default: 'Healthy'
        },
        gum_health: {
            type: 'dropdown',
            options: ['Normal', 'Gingivitis', 'Periodontitis'],
            default: 'Normal'
        }
    },
    
    init: function() {
        // Override VIA defaults
        _via.attributes = this.attributes;
        _via.toolbar = this.tools;
        
        // Dental-specific shortcuts
        document.addEventListener('keydown', (e) => {
            if (e.key === 't') _via.set_active_tool('polygon');
            if (e.key === 's') _via.save_project();
        });
    }
};

// Initialize when VIA loads
if (typeof _via !== 'undefined') VIA_DENTAL.init();
else document.addEventListener('via-loaded', VIA_DENTAL.init);