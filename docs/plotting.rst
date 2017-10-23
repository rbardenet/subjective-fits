Automatically insert your project plots
=======================================

``matplotlib`` provides already a plot directive to generate and include plots inside a read the docs document. For that, you will need to add the extension ``'matplotlib.sphinxext.plot_directive'`` in your conf.py and use one of the following alternatives:


Put the plot code in a separate file::

  .. plot:: plots/example_plot.py
    :include-source:
    
.. plot:: plots/example_plot.py
  :include-source:

   
Inline code inside a block like::

  .. plot::

     import matplotlib.pyplot as plt
     import numpy as np
     x = np.random.randn(1000)
     plt.hist( x, 20)
     plt.grid()
     plt.title(r'Normal: $\mu=%.2f, \sigma=%.2f$'%(x.mean(), x.std()))
     plt.show()

Will generate

.. plot::

   import matplotlib.pyplot as plt
   import numpy as np
   x = np.random.randn(1000)
   plt.hist( x, 20)
   plt.grid()
   plt.title(r'Normal: $\mu=%.2f, \sigma=%.2f$'%(x.mean(), x.std()))
   plt.show()