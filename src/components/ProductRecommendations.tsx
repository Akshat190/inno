import React, { useState } from 'react';
import ProductCard from './ProductCard';
import { Product } from '../types/Product';
import { ChevronLeft as ChevronLeftIcon, ChevronRight as ChevronRightIcon } from 'lucide-react';

interface ProductRecommendationsProps {
  skinTone: string;
  products: Product[];
  productsPerPage?: number;
}

const ProductRecommendations: React.FC<ProductRecommendationsProps> = ({
  skinTone,
  products,
  productsPerPage = 8 // Default to 8 products per page
}) => {
  const [currentPage, setCurrentPage] = useState(1);
  const totalPages = Math.ceil(products.length / productsPerPage);
  const indexOfLastProduct = currentPage * productsPerPage;
  const indexOfFirstProduct = indexOfLastProduct - productsPerPage;
  const currentProducts = products.slice(indexOfFirstProduct, indexOfLastProduct);

  // Handle page changes
  const handlePageChange = (pageNumber: number) => {
    setCurrentPage(pageNumber);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  // Generate page numbers array
  const pageNumbers = [];
  for (let i = 1; i <= totalPages; i++) {
    pageNumbers.push(i);
  }

  return (
    <div className="space-y-6">
      <h2 className="text-2xl font-bold text-gray-900">
        Recommended Products for {skinTone}
      </h2>
      
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
        {currentProducts.map((product, index) => (
          <div key={`product-${product.id || index}`}>
            <ProductCard
              id={product.id || index}
              name={product.name}
              brand={product.brand}
              price={product.price}
              rating={product.rating}
              image={product.image_url || ''}
              mst={product.mst}
              onAddToCart={() => console.log('Added to cart:', product.id, product.name)}
              onFavorite={() => console.log('Added to favorites:', product.id, product.name)}
            />
          </div>
        ))}
      </div>

      {products.length === 0 && (
        <div className="text-center text-gray-500">
          No products found for this skin tone.
        </div>
      )}

      {/* Pagination Controls */}
      {totalPages > 1 && (
        <div className="flex items-center justify-center space-x-2 mt-8">
          <button
            onClick={() => handlePageChange(currentPage - 1)}
            disabled={currentPage === 1}
            className="p-2 rounded-md border border-gray-300 disabled:opacity-50 disabled:cursor-not-allowed hover:bg-gray-50"
          >
            <ChevronLeftIcon className="h-5 w-5" />
          </button>

          <div className="flex space-x-1">
            {pageNumbers.map((number) => (
              <button
                key={number}
                onClick={() => handlePageChange(number)}
                className={`px-4 py-2 rounded-md ${
                  currentPage === number
                    ? 'bg-blue-600 text-white'
                    : 'border border-gray-300 hover:bg-gray-50'
                }`}
              >
                {number}
              </button>
            ))}
          </div>

          <button
            onClick={() => handlePageChange(currentPage + 1)}
            disabled={currentPage === totalPages}
            className="p-2 rounded-md border border-gray-300 disabled:opacity-50 disabled:cursor-not-allowed hover:bg-gray-50"
          >
            <ChevronRightIcon className="h-5 w-5" />
          </button>
        </div>
      )}
    </div>
  );
};

export default ProductRecommendations; 